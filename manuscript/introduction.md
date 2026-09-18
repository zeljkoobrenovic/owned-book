{mainmatter}

{id: introduction}
# 1. Introduction & Reading Guide

![Introduction & Reading Guide — logo](private-techuity/posts/introduction/assets/images/introduction/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn what this book is for, which route to take for the decision in front of you, and how to read its fictional examples and historical evidence.

> **KEY POINTS:**
>
> * Ownership changes the **conditions in which you lead**. Find out which money, decisions and expectations your product and engineering commitments depend on.
> * Different arrangements require **different choices**. A funding round, a buyout and a corporate acquisition can put the same roadmap under different constraints.
> * You remain **responsible for the company’s work**. Challenge assumptions, make feasible commitments and explain consequences for customers and teams.

Your company has new investors. The announcement promises growth and support. Within weeks, you are asked to hire faster, demonstrate a new product, reduce costs or connect to the owner’s systems. The requests may each sound reasonable. Together, they can exceed the company’s money, authority and ability to deliver.

**OWNED: Product & Engineering Leadership Under Investors** is for product and engineering leaders inside a company whose investors affect its funding, authority and expectations, including leaders who have joined an arrangement they didn’t choose. It assumes no finance training and explains the financial terms needed to question a plan, budget or ownership claim. It does assume an interest in fairly detailed questions about software delivery, architecture, organization and evidence, because those are where the investor’s expectations land. Founders, finance partners and investor advisers may find it useful as a shared vocabulary; the decisions it works through are the company leader’s.

The company’s ownership setting doesn’t remove your judgment or responsibility. Sometimes you can approve a change yourself. Sometimes you must negotiate funding, challenge a target or ask the board to choose between incompatible outcomes. The book helps you distinguish those situations and make the consequences clear.

{id: introduction--why-this-book-exists-and-how-it-is-written}
## Why This Book Exists, and How It Is Written

The financial, legal, and general business aspects of outside investment are well covered: there is no shortage of material on term sheets, valuations, fund structures, and deal mechanics. In the author’s experience as a technology leader and adviser, far less has been written about **what an external investment does to product and engineering**: which commitments it creates, which money and authority the team can actually count on, and how a roadmap, an architecture decision or a hiring plan should change once the ownership changes. That is an observation from practice, not a survey of the literature.

The same experience suggests what the gap costs. Inside companies it breeds **confusion**, and it **costs them opportunities**, because leaders who cannot read the arrangement cannot use it. It also **invites misuse**: a sentence that begins “investors want us to…” can carry an agenda nobody in the room has examined, sometimes without anyone knowing what the investors actually require or whether they were even asked. How often that happens is not measured here; that it happens at all is reason enough to be able to check.

This book is the response, written from the company leader’s side: the vocabulary to read the arrangement, working methods to test such claims, and worked decisions that show what a commitment the team can keep looks like.

This book is a living journal and a work in progress: a draft by [Željko Obrenović](https://obren.io), who keeps revising it as he learns more about its topics. Chapters change as better evidence, sharper examples, and reader questions arrive. Each chapter’s page carries a “View spec” link to the specification it was written against; the changelog at the end of that specification records what changed and why. Read the book as current thinking with its limits stated, not as a finished text.

{id: introduction--start-with-the-decision-in-front-of-you}
## Start With the Decision in Front of You

The six parts are ordered for learning, and the complete sequence is the default for a first reading. If a decision is already waiting, start with one of these routes and return to Part I when a financial term is unfamiliar.

| Your immediate need | Suggested route |
| --- | --- |
| A promised investment must become a budget | [An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget) → [Confirm the Cash Before You Commit](#obligations-before-budget) → [Decide Who Decides, Before You Disagree](#decide-who-decides) → [You Cannot Fund Every Good Project at Once](#cannot-fund-everything) → [Planning on Money That Hasn't Arrived](#the-financing-slipped) |
| An operating improvement needs a credible case | [You Cannot Fund Every Good Project at Once](#cannot-fund-everything) → [The Path From Roadmap to Revenue Is Fragile](#roadmap-to-revenue) → [Can the Team Deliver What the Plan Promises?](#can-the-team-deliver) → the relevant domain chapter in Part III → the [Practical Tools for Ownership and Technology Decisions](#toolkit) initiative and outcome records |
| Investor help is on offer | [Is the Investor’s Adviser Helping, Assessing or Deciding?](#investors-adviser) → [Find the Help That Changes What Your Team Can Do](#help-that-changes-capability) → [Turn an Offer of Help Into a Useful Engagement](#useful-engagement) |
| A transaction or ownership change is imminent | [Diligence Is Your Chance to Correct the Plan Before It Is Signed](#diligence-corrects-the-plan) → [The First Hundred Days: Turn Expectations Into a Funded Plan](#first-hundred-days) → [Hand Over the Obligations, Not Just the Company](#handover-of-obligations) |
| Owners want more growth or earnings than the team can support | [Match the Funding to the Work](#raise-what-you-need) → [You Cannot Fund Every Good Project at Once](#cannot-fund-everything) → [Headcount Is Not Capacity: Trace the Work Before You Hire](#fix-decisions-before-hiring) |
| Investor requests compete with customer needs | [The Path From Roadmap to Revenue Is Fragile](#roadmap-to-revenue) → [Decide Who Decides, Before You Disagree](#decide-who-decides) → [Judge an Investor by Their Behavior Under Pressure](#investor-under-pressure) → [Success for Whom, and for How Long?](#success-for-whom) |
| A corporate investor wants integration or access to data | [An Acquisition Adds Work Before It Adds Value](#acquisition-adds-work-first) → [Prove You Can Restore, Not Just That You Back Up](#prove-you-can-restore) → [Turn an Offer of Help Into a Useful Engagement](#useful-engagement) |
| The investor wants a leadership change | [Decide Who Decides, Before You Disagree](#decide-who-decides) → [Headcount Is Not Capacity: Trace the Work Before You Hire](#fix-decisions-before-hiring) → [Find the Help That Changes What Your Team Can Do](#help-that-changes-capability) → [Is the Investor’s Adviser Helping, Assessing or Deciding?](#investors-adviser) |
| We must reduce headcount | [Planning on Money That Hasn't Arrived](#the-financing-slipped) → [Anatomy of a Layoff](#anatomy-of-a-layoff) → [Management Equity, Fund Carry and Employee Jobs Are Different Bets](#different-bets) → the [Practical Tools for Ownership and Technology Decisions](#toolkit) workforce-decision record |

If your decision is the first one in the table — an announced investment that someone expects to become a hiring plan — read the chapter [An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget) now and the rest in order later.

{id: introduction--owners-rights-funding-and-change}
## Owners, Rights, Funding, and Change

This book focuses mainly on private companies working with **outside investors**. Founder self-funding serves as a point of comparison, and public markets come up where they influence financing or ownership changes, but leadership in public companies is not covered in detail.

To understand the impact of any outside investment, keep **four questions** separate: who the owners are, what rights they have, how the company is funded, and what is changing.

The first question, who the owners are, is where most of the labels come from. A **venture investor** typically funds a young company that is still proving its product or business model, though venture funds also invest in successive rounds of companies already scaling an established product. A **growth investor** funds the expansion of a business with established demand; the venture and growth labels overlap at that later stage, and the round’s terms matter more than its name. A **buyout investor** purchases control. A **corporate investor** is another operating business investing for financial or commercial reasons; it may hold a minority stake or acquire the company outright.

These labels tell you roughly what kind of investor you’re dealing with, but not the answers to the other three questions. Rights don’t automatically follow from stake size: a minority investment can carry important approval rights without conferring control. Funding doesn’t follow from deal type: borrowing is a way to raise money and isn’t confined to buyouts. And the nature of the change is separate again: a **carve-out** takes a business out of a larger company, a **turnaround** fixes serious business problems, and either can involve any of the owner types above.

The practical impact of any investment therefore depends on its actual terms, **established case by case**: the investor’s rights, the financing, the support available and the time horizon. The events a leader faces, from a first round to a sale or continued ownership, arrive in any order; each sends you to a different part of the book, which is why the routes above exist.

![A company commitment depends on four separate questions: who the owners are, what rights they have, how the company is funded and what is changing.](private-techuity/posts/introduction/assets/images/introduction/four-questions-before-a-commitment.jpeg)

**Figure 1:** *Keep the four questions separate before a commitment: who the owners are, what rights they have, how the company is funded and what is changing.*

{id: introduction--how-the-parts-build-on-each-other}
## How the Parts Build on Each Other

Part I supplies the financial tools to understand your owners and your available cash. Part II establishes authority, incentives and working relationships. Part III turns expectations into choices about product, engineering and people; it is the center of the book. Part IV helps you obtain useful help, from the investor or elsewhere. Part V follows one finding from diligence into a funded early plan, its review and a handover; its delayed-financing chapter, and the reduction chapter that continues it, are a separate illustration of how a dated cash forecast changes commitments and, when the money is late enough, the team. Part VI examines historical cases and closes with the book’s standard for success.

Each part introduction explains its chapters and the order. On a first pass, read in order, since each chapter builds on terms introduced earlier: the chapter [A Valuation Is an Estimate, Not a Fact](#valuation-is-an-estimate) teaches financial valuation, and the chapter [Turn “We Expect Growth” Into a Design Decision](#growth-into-design) later applies those concepts to a design choice once the product and engineering foundations are in place.

![The book moves from money and decisions through company work, support, ownership changes and field lessons.](private-techuity/posts/introduction/assets/images/introduction/owned-reading-journey.jpeg)

**Figure 2:** *The reading sequence builds the foundations before applying them to work, support and changing ownership.*

{id: introduction--meet-the-fictional-company}
## Meet the Fictional Company

**Larkspur** sells scheduling software to maintenance businesses. Its customers organize appointments and assign people to work. A recurring challenge is **customer onboarding**: the setup and help needed before a customer can use the product successfully.

Ines is the **chief executive officer (CEO)**, leading the company. Alex is the **chief technology officer (CTO)**, leading technology. Sam is the **chief financial officer (CFO)**, leading finance. Priya leads product. Morgan is the investor’s technology adviser in fund-backed scenarios.

The chapters place Larkspur in alternative situations: learning with limited cash, expanding with growth funding, operating after a buyout, or working with a corporate owner. These are fictional decision exercises, not a single company history. Each example states its own assumptions; its figures do not combine into one set of accounts.

One chain is a deliberate exception, and it is the only one. A single onboarding finding, that setting up a new customer depends on one specialist’s manual work, is carried through six chapters and the toolkit with the same identifiers:

1. the investigation before the investment, [Diligence Is Your Chance to Correct the Plan Before It Is Signed](#diligence-corrects-the-plan);
2. the funded early plan, [The First Hundred Days: Turn Expectations Into a Funded Plan](#first-hundred-days), which allocates one envelope, and [You Cannot Fund Every Good Project at Once](#cannot-fund-everything), which chooses within it and revises the choice when a test fails;
3. the recovery test funded beside the pilot, [Prove You Can Restore, Not Just That You Back Up](#prove-you-can-restore);
4. the investor’s support for the pilot, [Find the Help That Changes What Your Team Can Do](#help-that-changes-capability) and [Turn an Offer of Help Into a Useful Engagement](#useful-engagement);
5. the pilot’s measured outcome and the decision it supports, [The Path From Roadmap to Revenue Is Fragile](#roadmap-to-revenue);
6. the handover of what was paid, owed and left undone, [Hand Over the Obligations, Not Just the Company](#handover-of-obligations).

The [Practical Tools for Ownership and Technology Decisions](#toolkit) shows the record those chapters write, stage by stage. Follow that chain to see one decision carried all the way through, from evidence to money to what was left undone.

The delayed-financing chapter ([Planning on Money That Hasn't Arrived](#the-financing-slipped)) and the reduction chapter that continues it ([Anatomy of a Layoff](#anatomy-of-a-layoff)) are not part of that chain. They are a separate illustration of how a dated cash forecast changes commitments when expected money arrives late, and what a reduction costs by date; their cash, burn, people and dates are their own and do not add to the chain’s figures. “€m” means millions of euros.

{id: introduction--choose-a-reading-format}
## Choose a Reading Format

Each main chapter provides an **Article** and a 300–500-word **TL;DR** summary. TL;DR means “too long; didn’t read.” All thirty-one main chapters also have a six-panel **Comic**, illustrated, with captions and dialogue transcripts. The six part introductions and the reference pages have no TL;DR or comic.

For a shorter first pass, read the part introductions and the summaries. The formats are companions rather than substitutes. Each one is written to reach the same decision and to keep the conditions that decide whether that decision holds; what varies is depth: the article gives the fullest calculations, the discussion of sources and the alternative cases, while every format keeps the conditions that would change the decision. The summaries and comics of this September 2026 revision are still being reconciled chapter by chapter, so where a short format and the article disagree, the article is the one to trust.

{id: introduction--read-the-evidence-with-its-limits}
## Read the Evidence With Its Limits

This living manuscript was first drafted in September 2026 and revised the same month. Its historical cases examine specified periods at Hilton, Skype, Visma, Toys R Us and TeamSystem. The evidence concentrates on private equity and related ownership transitions, and doesn’t establish how all venture, growth or corporate investors behave or perform.

Institutional funding guides support descriptions of other arrangements. The comparative Larkspur exercises are the author’s illustrations of decisions under stated assumptions. Company filings, investor accounts and research answer different questions; none makes an unobserved customer or employee outcome known.

The [Bibliography and Evidence Guide](#bibliography) records consultation scope and evidence limits. The chapter-end “To Probe Further” lists are optional reading for going deeper; the bibliography identifies which resources were also used as evidence, since a few appear in both places. A chapter’s argument rests only on the sources cited inline.

{id: introduction--contents}
## Contents

The site navigation lists the same chapters; this list is here for lookup.

{id: introduction--part-i-understanding-financing-and-ownership-money-authority-and-returns}
### Part I — Understanding Financing and Ownership: Money, Authority and Returns

- [PART I — Understanding Financing and Ownership](#part-1) — part introduction
- **1.** [Customers, Lenders and Investors: What Each Expects in Return](#customers-lenders-investors)
- **2.** [An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget)
- **3.** [A Valuation Is an Estimate, Not a Fact](#valuation-is-an-estimate)
- **4.** [Same Company, Same Performance, Three Different Investor Returns](#three-different-returns)
- **5.** [Match the Funding to the Work](#raise-what-you-need)
- **6.** [Confirm the Cash Before You Commit](#obligations-before-budget)

{id: introduction--part-ii-how-investor-ownership-changes-decisions}
### Part II — How Investor Ownership Changes Decisions

- [PART II — How Investor Ownership Changes Decisions](#part-2) — part introduction
- **7.** [Decide Who Decides, Before You Disagree](#decide-who-decides)
- **8.** [Management Equity, Fund Carry and Employee Jobs Are Different Bets](#different-bets)
- **9.** [Judge an Investor by Their Behavior Under Pressure](#investor-under-pressure)

{id: introduction--part-iii-turning-investor-expectations-into-commitments}
### Part III — Turning Investor Expectations Into Commitments

- [PART III — Turning Investor Expectations Into Commitments](#part-3) — part introduction
- **10.** [You Cannot Fund Every Good Project at Once](#cannot-fund-everything)
- **11.** [The Path From Roadmap to Revenue Is Fragile](#roadmap-to-revenue)
- **12.** [Can the Team Deliver What the Plan Promises?](#can-the-team-deliver)
- **13.** [Headcount Is Not Capacity: Trace the Work Before You Hire](#fix-decisions-before-hiring)
- **14.** [Turn “We Expect Growth” Into a Design Decision](#growth-into-design)
- **15.** [Why a Cheaper Cloud Bill Can Be Bad News](#cheaper-cloud-bill)
- **16.** [Prove You Can Restore, Not Just That You Back Up](#prove-you-can-restore)
- **17.** [An AI Strategy Hides Three Investment Questions](#ai-strategy-three-questions)
- **18.** [An Acquisition Adds Work Before It Adds Value](#acquisition-adds-work-first)

{id: introduction--part-iv-beyond-money-getting-useful-help-from-your-investor}
### Part IV — Beyond Money: Getting Useful Help From Your Investor

- [PART IV — Beyond Money: Getting Useful Help From Your Investor](#part-4) — part introduction
- **19.** [Is the Investor’s Adviser Helping, Assessing or Deciding?](#investors-adviser)
- **20.** [Find the Help That Changes What Your Team Can Do](#help-that-changes-capability)
- **21.** [Turn an Offer of Help Into a Useful Engagement](#useful-engagement)

{id: introduction--part-v-leading-through-funding-and-ownership-changes}
### Part V — Leading Through Funding and Ownership Changes

- [PART V — Leading Through Funding and Ownership Changes](#part-5) — part introduction
- **22.** [Diligence Is Your Chance to Correct the Plan Before It Is Signed](#diligence-corrects-the-plan)
- **23.** [The First Hundred Days: Turn Expectations Into a Funded Plan](#first-hundred-days)
- **24.** [Planning on Money That Hasn't Arrived](#the-financing-slipped)
- **25.** [Anatomy of a Layoff](#anatomy-of-a-layoff)
- **26.** [Hand Over the Obligations, Not Just the Company](#handover-of-obligations)

{id: introduction--part-vi-lessons-from-the-field}
### Part VI — Lessons from the Field

- [PART VI — Lessons from the Field](#part-6) — part introduction
- **27.** [Hilton and Skype: A Successful Exit Still Needs Explaining](#hilton-and-skype)
- **28.** [Visma: Continuity of Manager Is Not Continuity of Money](#visma)
- **29.** [Toys R Us: Positive Operating Earnings, Too Little Cash](#toys-r-us)
- **30.** [TeamSystem: Each New Owner Inherits Progress and Unfinished Work](#teamsystem)
- **31.** [Success for Whom, and for How Long?](#success-for-whom)

{id: introduction--reference-material}
### Reference Material

- [Practical Tools for Ownership and Technology Decisions](#toolkit) — practical decision and support records, with one finding followed all the way through.
- [Fund Economics: Fees, Distributions and Performance Reports](#fund-economics) — optional depth on fund fees, distributions and performance reports.
- [Glossary](#glossary) — plain-language definitions and an alphabetical index.
- [Bibliography and Evidence Guide](#bibliography) — sources, consultation dates and evidence limits.
