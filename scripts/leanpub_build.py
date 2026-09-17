#!/usr/bin/env python3
"""Trigger a Leanpub build via the API and download the resulting PDF and EPUB.

Usage:
    python scripts/leanpub_build.py [--slug SLUG] [--publish] [--out DIR]

Configuration (env vars or flags):
    LEANPUB_API_KEY   required, from https://leanpub.com/author_dashboard/settings
    LEANPUB_SLUG      book slug, i.e. the part after leanpub.com/ (or --slug)

Uses only the Python standard library.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://leanpub.com"
DEFAULT_SLUG = "owned"
DEFAULT_OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")


def api_request(method, path, api_key, data=None):
    """Perform a JSON API request and return the decoded body (or {} if empty)."""
    url = f"{BASE_URL}{path}?{urllib.parse.urlencode({'api_key': api_key})}"
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, method=method)
    if body is not None:
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8").strip()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        sys.exit(f"HTTP {e.code} for {method} {path}: {detail}")
    return json.loads(raw) if raw else {}


def wait_for_job(slug, api_key, poll_seconds, timeout_seconds):
    """Poll job_status.json until the build completes. Leanpub returns {} when done."""
    deadline = time.time() + timeout_seconds
    last_message = None
    while time.time() < deadline:
        status = api_request("GET", f"/{slug}/job_status.json", api_key)
        if not status:
            print("Build complete.")
            return
        message = status.get("message") or status.get("status") or ""
        num, total = status.get("num"), status.get("total")
        progress = f" ({num}/{total})" if num is not None and total is not None else ""
        line = f"{message}{progress}"
        if line != last_message:
            print(f"  {line}")
            last_message = line
        if status.get("status") == "error" or status.get("backtrace"):
            sys.exit(f"Build failed: {json.dumps(status, indent=2)}")
        time.sleep(poll_seconds)
    sys.exit(f"Timed out after {timeout_seconds}s waiting for the build to finish.")


def download(url, dest):
    tmp = dest + ".part"
    req = urllib.request.Request(url, headers={"User-Agent": "leanpub-build-script"})
    with urllib.request.urlopen(req, timeout=300) as resp, open(tmp, "wb") as fh:
        while True:
            chunk = resp.read(1 << 16)
            if not chunk:
                break
            fh.write(chunk)
    os.replace(tmp, dest)
    print(f"  saved {dest} ({os.path.getsize(dest) / 1024 / 1024:.1f} MB)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--slug", default=os.environ.get("LEANPUB_SLUG", DEFAULT_SLUG), help="Leanpub book slug")
    parser.add_argument("--api-key", default=os.environ.get("LEANPUB_API_KEY"), help="Leanpub API key")
    parser.add_argument("--out", default=DEFAULT_OUT, help="output directory (default: ./docs)")
    parser.add_argument("--publish", action="store_true", help="publish instead of building a preview")
    parser.add_argument("--email-readers", action="store_true", help="with --publish: notify readers")
    parser.add_argument("--release-notes", default="", help="with --publish: release notes text")
    parser.add_argument("--poll", type=int, default=10, help="seconds between status checks")
    parser.add_argument("--timeout", type=int, default=1800, help="max seconds to wait for the build")
    parser.add_argument("--no-build", action="store_true", help="skip the build, only download the latest files")
    args = parser.parse_args()

    if not args.api_key:
        sys.exit("Missing API key: set LEANPUB_API_KEY or pass --api-key.")

    if not args.no_build:
        if args.publish:
            print(f"Publishing {args.slug} ...")
            data = {"publish[email_readers]": "true" if args.email_readers else "false"}
            if args.release_notes:
                data["publish[release_notes]"] = args.release_notes
            api_request("POST", f"/{args.slug}/publish.json", args.api_key, data)
        else:
            print(f"Starting preview build for {args.slug} ...")
            api_request("POST", f"/{args.slug}/preview.json", args.api_key, {})
        time.sleep(3)  # give Leanpub a moment to register the job
        wait_for_job(args.slug, args.api_key, args.poll, args.timeout)

    print("Fetching download URLs ...")
    book = api_request("GET", f"/{args.slug}.json", args.api_key)
    kind = "published" if args.publish else "preview"
    files = {
        "book.pdf": book.get(f"pdf_{kind}_url"),
        "book.epub": book.get(f"epub_{kind}_url"),
    }

    os.makedirs(args.out, exist_ok=True)
    missing = [name for name, url in files.items() if not url]
    for name, url in files.items():
        if url:
            print(f"Downloading {name} ...")
            download(url, os.path.join(args.out, name))
    if missing:
        sys.exit(f"No {kind} URL returned for: {', '.join(missing)}. "
                 f"Check that the {kind} build exists and that this format is enabled in Leanpub.")


if __name__ == "__main__":
    main()
