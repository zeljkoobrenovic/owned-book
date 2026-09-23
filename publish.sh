# export LEANPUB_API_KEY=...
bash update.sh

python3 scripts/leanpub_build.py

git add .
git commit -m "latest update PDF and EPUB"
git push