{mainmatter}

{id: introduction}
# 1. Introduction & Reading Guide

![Introduction & Reading Guide — logo](private-techuity/posts/introduction/assets/images/introduction/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn what this book is for, which route to take for the decision in front of you, and how to read its fictional examples and historical evidence.

> **KEY POINTS:**
>
> * Ownership changes the **conditions in which you lead**. Find out which money, decisions and expectations your product and engineering commitments depend on.
> * Different arrangements require **different choices**. Raising money from investors, a buyout in which an investor buys the power to direct the company, and a purchase by another business can put the same roadmap, the plan of what the team builds next, under different constraints.
> * You remain **responsible for the company’s work**. Challenge assumptions, make feasible commitments and explain consequences for customers and teams.

Your company has new investors. The announcement promises growth and support. Within weeks, you are asked to hire faster, demonstrate a new product, reduce costs or connect to the owner’s systems. The requests may each sound reasonable. Together, they can exceed the company’s money, authority and ability to deliver.

**OWNED: Product & Engineering Leadership Under Investors** is for product and engineering leaders inside a company whose investors affect its funding, authority and expectations, including leaders who have joined an arrangement they didn’t choose. It assumes no finance training and explains the financial terms needed to question a plan, budget or ownership claim. It does assume an interest in fairly detailed questions about how software is built and released, how systems are structured, how teams are organized and what counts as evidence, because those are where the investor’s expectations land. Founders, finance colleagues and investor advisers may find it useful as a shared vocabulary.

The company’s ownership setting doesn’t remove your judgment or responsibility. Sometimes you can approve a change yourself. Sometimes you must negotiate funding, challenge a target or ask the board, the directors who oversee the company on behalf of its owners, to choose between incompatible outcomes. The book helps you distinguish those situations and make the consequences clear.

{id: introduction--why-this-book-exists-and-how-it-is-written}
## Why This Book Exists, and How It Is Written

The financial, legal, and general business aspects of outside investment are well covered. There is no shortage of material on term sheets (the documents that propose an investment’s main conditions), valuations (estimates of what a company is worth), fund structures (how investors’ pooled money is organized and managed) and deal mechanics (the steps that complete an investment or a purchase). In the author’s experience as a technology leader and adviser, far less has been written about **what an external investment does to product and engineering**: which commitments it creates, which money and authority the team can actually count on, and how a roadmap, a decision about how the software is structured, or a hiring plan should change once the ownership changes.

The same experience suggests what the gap costs. Inside companies it breeds **confusion**, and it **costs them opportunities**, because leaders who cannot read the arrangement cannot use it. It also **invites misuse**: a sentence that begins “investors want us to…” can carry an agenda nobody in the room has examined, sometimes without anyone knowing what the investors actually require or whether they were even asked.

This book is the response, written from the company leader’s side: the vocabulary to read the arrangement, working methods to test such claims, and worked decisions that show what a commitment the team can keep looks like.

This book is a living journal and a work in progress: a draft by [Željko Obrenović](https://obren.io), who keeps revising it as he learns more about its topics. Chapters change as better evidence, sharper examples, and reader questions arrive. Each chapter’s page carries a “View spec” link to the specification it was written against; the changelog at the end of that specification records what changed and why. Read the book as current thinking with its limits stated, not as a finished text.

{id: introduction--start-with-the-decision-in-front-of-you}
## Start With the Decision in Front of You

The eight parts are ordered for learning, and the complete sequence is the default for a first reading. If a decision is already waiting, pick the row that matches it, read the chapter in the **Start with** column, and return to Part I when a financial term is unfamiliar. The **Then** column is optional further reading, in a suggested order.

The chapter titles in the table appear in full on this page, and a few of them use words that Part I explains properly. Until then, read them this way:

- **Money words.** **Revenue** is the money a company earns from selling its product, before any costs are taken off. **Profit** is what remains after costs. **Cash** is the money actually available to spend, which can run short even when revenue and profit look healthy, and **cash flow** is money moving into and out of the company over time. **Operating earnings** are a profit figure from the company’s ordinary business, worked out under accounting rules; they are not cash in the bank. A **lender** provides money that must be repaid, usually with **interest**, the extra charge for borrowing it.
- **Ownership words.** **Equity** means ownership; an owner’s equity is its share of the company. **Carry** is short for carried interest: the share of investment profits that the firm managing a fund can receive under the fund’s agreed conditions, separate from what the fund’s own investors earn. **Diligence** is short for due diligence, the investigation of a business before investing in or buying it. An **exit** is an investor selling or otherwise cashing in its investment; it is not the company closing.
- **People and systems words.** **Headcount** is the number of employees; **capacity** is the amount of work those people can actually handle, which is not the same thing. **Resilience** is the ability of the company’s systems to withstand and recover from disruption, and a **backup** is a saved copy of data or software kept for that recovery. **Cloud costs** are the charges for computing services rented from an outside provider.

The [Glossary](#glossary) covers the rest.

| Your immediate need | Start with | Then |
| --- | --- | --- |
| A promised investment must become a budget | [Understand Funding and Control: An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget) | [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget), [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides), [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything), [Manage Funding Delays: Revise the Cash Plan and Commitments](#the-financing-slipped) |
| A change to how the business works needs a credible case | [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything) | [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue), [Assess Capability: Can the Team Deliver?](#can-the-team-deliver), the Part IV, V or VI chapter for your area, and the [Practical Tools for Ownership and Technology Decisions](#toolkit) records of an initiative and its outcome |
| The investor has its own technology adviser (a “technology operating partner”) or a specialist in artificial intelligence (AI): software that generates text or makes predictions from patterns in data | [Understand Technology Operating Partners: How They Work With Your Team](#tech-operating-partner) | [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#investors-adviser), [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement) |
| Agree or reset how we work with the investor | [Plan Investor Support: Match the Help to Company Priorities](#operating-model-blueprints) | [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides), [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement) |
| Investor help is on offer | [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#investors-adviser) | [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability), [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement) |
| Explore the investor’s network: its events, and the leaders of the other companies it has invested in | [Learn Through Your Investor’s Network: Knowledge, Peers and New Perspectives](#learn-through-investors-network) | the [Practical Tools for Ownership and Technology Decisions](#toolkit) learning brief, then [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability) when a specific need emerges |
| The investor wants better reporting, or we keep arguing about what a number means | [Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards](#have-your-numbers-ready) | the [Practical Tools for Ownership and Technology Decisions](#toolkit) measure record, then [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue) for the benefit arithmetic |
| The investor wants to oversee technology across all the companies it has invested in (its portfolio) | [Appendix: Grounded Architecture Across an Investment Portfolio](#grounded-architecture-portfolio) | [Plan Investor Support: Match the Help to Company Priorities](#operating-model-blueprints), [Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards](#have-your-numbers-ready) |
| The company is about to be bought, or to take new investment | [Use Diligence: Correct the Plan Before It Is Signed](#diligence-corrects-the-plan) | [Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days), [Manage the Handover: Carry Forward the Evidence and Obligations](#handover-of-obligations) |
| Owners want more growth or profit than the team can support | [Understand Funding Choices: Match the Money to the Work](#raise-what-you-need) | [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything), [Scale the Team Up: Headcount Is Not Capacity](#fix-decisions-before-hiring) |
| Investor requests compete with customer needs | [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue) | [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides), [Assess Investor Fit: Behavior Under Pressure](#investor-under-pressure), [Success for Whom, and for How Long?](#success-for-whom) |
| A business that has invested in us wants to connect its systems to ours, or wants access to our data | [Plan Acquisitions and Separations: Account for Extra Work, Not Just Expected Value](#acquisition-adds-work-first) | [Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore), [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement) |
| The investor wants a leadership change | [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides) | [Scale the Team Up: Headcount Is Not Capacity](#fix-decisions-before-hiring), [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability), [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#investors-adviser) |
| We must reduce the number of employees | [Manage Funding Delays: Revise the Cash Plan and Commitments](#the-financing-slipped) | [Scale the Team Down: Decide What Work Stops, Not Just Who Leaves](#anatomy-of-a-layoff), then [Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets) on how three different rewards shape what people push for: the managers’ ownership shares, the fund manager’s carry and employees’ jobs; then the [Practical Tools for Ownership and Technology Decisions](#toolkit) workforce-decision record |

If your decision is the first one in the table — an announced investment that someone expects to become a hiring plan — read the chapter [Understand Funding and Control: An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget) now and the rest in order later.

{id: introduction--owners-rights-funding-and-change}
## Owners, Rights, Funding, and Change

This book focuses mainly on **private companies**, whose shares (the units of ownership in a company) are not traded on a public stock exchange, working with **outside investors**: people or organizations from outside the company who commit money expecting a **financial return**, the gain they hope to make on it, and accepting the risk of loss.

An investor’s money can go to two different places, and a deal sometimes combines both. When the company issues new shares, the investor pays the company, which then has new funding to spend. When the investor buys shares from existing owners, the money goes to those sellers, and the company itself receives nothing to spend: the ownership changes, the budget does not.

Two cases sit outside that main scope. A founder funding the company from their own resources serves as a point of comparison. Public stock markets come up where they influence financing or ownership changes, but leadership in publicly traded companies, whose shares anyone can buy on an exchange, is not covered in detail.

To understand the impact of any outside investment, keep **four questions** separate: who the owners are, what rights they have, how the company is funded, and what is changing.

Two words recur in the answers. An owner’s **stake** is the share of the company it holds, usually stated as a percentage. **Control** is the power to direct the company’s main decisions, such as appointing its leaders or approving its budget. Holding more than half the shares normally brings control, but the rights agreed in the investment can move it.

The first question, who the owners are, is where most of the labels come from. A **venture investor** typically funds a young company that is still proving its product or the way it earns money, though venture funds also invest in later **funding rounds** (each round is one occasion on which the company raises money from investors on agreed terms) of companies already scaling an established product. A **growth investor** funds the expansion of a business with established demand; the venture and growth labels overlap at that later stage, and the round’s terms matter more than its name. A **buyout investor** purchases control: it buys enough of the company, on terms that give it the power to direct the main decisions. A **corporate investor** is another operating business investing for financial or commercial reasons; it may hold a **minority stake** (less than half the company) or acquire the company outright, which is a corporate **acquisition**.

These labels tell you roughly what kind of investor you’re dealing with, but not the answers to the other three questions. **Rights** don’t automatically follow from **stake size**: a minority investment can carry important **approval rights** without conferring control. An investor holding a fifth of the shares may, for example, have the agreed right to say no to new borrowing above a set amount or to a sale of the company, while having no say in day-to-day decisions. **Funding** doesn’t follow from deal type: borrowing (money that must be repaid, usually with interest) is a way to raise money and isn’t confined to buyouts. And the nature of the **change** is separate again: a **carve-out** takes a business out of a larger company, a **turnaround** fixes serious business problems, and either can involve any of the owner types above.

The practical impact of any investment therefore depends on its actual terms, **established case by case**: the investor’s rights, the financing, the support available and how long the investor expects to remain involved. The events a leader faces, from a first funding round to a sale of the company or continued ownership, arrive in any order; each sends you to a different part of the book, which is why the routes above exist.

![Four cards feed one notebook labelled Commitment: Owners (three people in business clothes), Rights (a signed document stamped APPROVED beside a ticked checkbox), Funding (a money bag, stacked coins and a rising line chart) and What is changing (a small building moving out of a larger building outline, labelled Leaving a larger company, and a cracked building being repaired with a wrench and propped by a beam, labelled Fixing a struggling business).](private-techuity/posts/introduction/assets/images/introduction/four-questions-before-a-commitment.jpeg)

**Figure 1:** *Keep the four questions separate before a commitment: who the owners are, what rights they have, how the company is funded and what is changing, for instance a business leaving a larger company or a struggling business being fixed.*

{id: introduction--how-the-parts-build-on-each-other}
## How the Parts Build on Each Other

- **Part I** supplies the financial tools to understand your owners and the cash you can actually count on.
- **Part II** establishes who has the authority to decide, which rewards and pressures shape those decisions (the incentives), and the working relationships around them.
- **Part III** connects the investor–company working arrangement with useful help, the agreements that define an adviser’s or specialist’s work and authority, and the people who provide that support.
- **Part IV** turns expectations into choices about product, engineering, people and AI, and revises them when expected money is late. It is the center of the book.
- **Part V** changes the company’s size and shape deliberately: adding people, reducing them, changing systems for expected growth, and buying or separating a business.
- **Part VI** keeps the technology the company already runs worth its cost: a lower cloud bill and backups that must actually restore.
- **Part VII** follows the events around a funding or ownership change: the investigation before an investment, the first hundred days, and the handover to the next owners.
- **Part VIII** examines historical cases and closes with the book’s standard for success.

Each part introduction explains its chapters and the order. On a first pass, read in order, since each chapter builds on terms introduced earlier: for instance, the chapter [Understand Valuation: An Estimate, Not a Fact](#valuation-is-an-estimate) teaches how a company’s worth is estimated, and the chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design) later applies those concepts to a design choice once the product and engineering foundations are in place.

The eight parts work together around one purpose: **commitments the company can keep**. Funding and obligations (the payments and duties the company must fulfil) set the conditions; authority and incentives shape decisions; the working arrangement with the investor adds capability; those decisions become feasible work, deliberate changes of size and a technology estate kept worth its cost. Funding and ownership events require renewed commitments, and evidence from other companies helps you question the assumptions throughout.

![Eight parts form a connected framework around commitments the company can keep: I Understand money and obligations; II Align authority and incentives; III Collaborate for useful help and capability; IV Commit to feasible work; V Scale the team, the systems and the company deliberately; VI Sustain the technology you run, worth its cost; VII Lead through funding and ownership changes; VIII Learn from evidence about other companies. A clockwise path connects the parts and returns from learning to understanding.](private-techuity/posts/introduction/assets/images/introduction/owned-eight-part-framework.jpeg)

**Figure 2:** *The eight parts share one leadership purpose. Read I–VIII to build the foundations, then revisit the relevant part as conditions and evidence change.*

{id: introduction--meet-the-fictional-company}
## Meet the Fictional Company

**Larkspur** sells scheduling software to maintenance businesses. Its customers organize appointments and assign people to work. A recurring challenge is **customer onboarding**: the setup and help needed before a customer can use the product successfully.

Ines is the **chief executive officer (CEO)**, leading the company. Alex is the **chief technology officer (CTO)**, leading technology. Sam is the **chief financial officer (CFO)**, leading finance. Priya leads product. Morgan is the investor’s technology adviser in the scenarios where an investment fund, a pool of investors’ money run by a management firm, owns part or all of Larkspur.

The chapters place Larkspur in alternative situations: learning with limited cash, expanding with growth funding, operating after a buyout, or working with a corporate owner. These are fictional decision exercises, not a single company history. Each example states its own assumptions; its figures do not combine into one set of financial records.

One shared example is the deliberate exception, and it is the main one. A single onboarding finding, that setting up a new customer depends on one specialist’s manual work, is carried through six stages, nine chapters and the toolkit with the same identifiers:

1. the investigation before the investment, [Use Diligence: Correct the Plan Before It Is Signed](#diligence-corrects-the-plan), in which the buyer examines the business before committing;
2. the funded early plan, [Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days), which sets one approved budget and allocation of staff time for the first hundred days, and [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything), which chooses within that budget to run a **pilot** (a limited trial of automated onboarding before any larger commitment) and revises the choice when a test fails;
3. the recovery test funded beside the pilot, [Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore), which checks that a failed system and its data can be restored;
4. the investor’s support for the pilot, [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability) and [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement);
5. the pilot’s measured outcome and the decision it supports, [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue), and how those numbers are defined, owned and labelled, [Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards](#have-your-numbers-ready);
6. the handover of what was paid, owed and left undone, [Manage the Handover: Carry Forward the Evidence and Obligations](#handover-of-obligations).

The [Practical Tools for Ownership and Technology Decisions](#toolkit) shows the record those chapters write, stage by stage. Follow that example to see one decision carried all the way through, from evidence to money to what was left undone.

The delayed-financing chapter ([Manage Funding Delays: Revise the Cash Plan and Commitments](#the-financing-slipped)) and the staff-reduction chapter that continues it ([Scale the Team Down: Decide What Work Stops, Not Just Who Leaves](#anatomy-of-a-layoff)) form a second, separate connected example. They show how a dated **cash forecast**, a month-by-month estimate of the money expected to come in and go out and the balance left, changes commitments when expected money arrives late. They also show when a staff reduction requires payments and when its savings begin. Their cash, the rate at which the company spends it, their people and their dates are their own and do not add to the main example’s figures. “€m” means millions of euros.

{id: introduction--choose-a-reading-format}
## Choose a Reading Format

All thirty-nine main chapters provide an **Article**, a short **TL;DR** summary and an illustrated **Comic**, with captions and dialogue transcripts. TL;DR means “too long; didn’t read.” Summaries aim for 300–500 words; some current drafts run longer than that target. Most comics are pages of stacked strips with the dialogue drawn into the artwork; the three case comics on Visma, Toys R Us and TeamSystem use single-scene panels. The eight part introductions, the appendix and the reference pages use only the Article format. These counts describe the files at the time of writing and are rechecked as chapters are revised.

For a shorter first pass, read the part introductions and chapter summaries. The formats are companions rather than substitutes. Each one is written to reach the same decision and to keep the conditions that decide whether that decision holds; what varies is depth: the article gives the fullest calculations, the discussion of sources and the alternative cases, while every format keeps the conditions that would change the decision. The summaries and comics of this September 2026 revision are still being reconciled chapter by chapter, so where a short format and the article disagree, the article is the one to trust.

{id: introduction--read-the-evidence-with-its-limits}
## Read the Evidence With Its Limits

This living manuscript was first drafted in September 2026 and revised the same month. Its historical cases examine specified periods at Hilton, Skype, Visma, Toys R Us and TeamSystem. The evidence concentrates on **private equity**, investment in companies whose shares are not publicly traded, usually made through funds of pooled investor money and often taking control, and on related ownership transitions. It doesn’t establish how all venture, growth or corporate investors behave or perform.

Guides published by regulators and by public development banks, publicly backed institutions that support business or economic development, underpin the descriptions of other arrangements. The comparative Larkspur exercises are the author’s illustrations of decisions under stated assumptions. Company filings (documents formally submitted to a regulator or public registry), investors’ own accounts of events and research answer different questions; none makes an unobserved customer or employee outcome known.

The [Bibliography and Evidence Guide](#bibliography) records consultation scope and evidence limits. The chapter-end “To Probe Further” lists are optional reading for going deeper; the bibliography identifies which resources were also used as evidence, since a few appear in both places. A chapter’s argument rests only on the sources cited inline.

{id: introduction--contents}
## Contents

The site navigation lists the same chapters; this list is here for lookup.

{id: introduction--part-i-understand-financing-and-ownership}
### Part I — UNDERSTAND: Financing and Ownership

- [UNDERSTAND: Financing and Ownership](#part-1) — part introduction
- **1.** [Understand Expectations: Customers, Lenders and Investors](#customers-lenders-investors)
- **2.** [Understand Funding and Control: An Investment Announcement Is Not a Budget](#announcement-is-not-a-budget)
- **3.** [Understand Valuation: An Estimate, Not a Fact](#valuation-is-an-estimate)
- **4.** [Understand Investor Returns: Same Performance, Different Outcomes](#three-different-returns)
- **5.** [Understand Funding Choices: Match the Money to the Work](#raise-what-you-need)
- **6.** [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget)

{id: introduction--part-ii-align-clarify-who-decides-and-what-is-at-stake}
### Part II — ALIGN: Clarify Who Decides and What Is at Stake

- [ALIGN: Clarify Who Decides and What Is at Stake](#part-2) — part introduction
- **7.** [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides)
- **8.** [Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets)
- **9.** [Assess Investor Fit: Behavior Under Pressure](#investor-under-pressure)

{id: introduction--part-iii-collaborate-get-useful-help-from-your-investors}
### Part III — COLLABORATE: Get Useful Help From Your Investors

- [COLLABORATE: Get Useful Help From Your Investor](#part-3) — part introduction
- **10.** [Plan Investor Support: Match the Help to Company Priorities](#operating-model-blueprints)
- **11.** [Learn Through Your Investor’s Network: Knowledge, Peers and New Perspectives](#learn-through-investors-network)
- **12.** [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability)
- **13.** [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement)
- **14.** [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#investors-adviser)
- **15.** [Understand Technology Operating Partners: How They Work With Your Team](#tech-operating-partner)

{id: introduction--part-iv-commit-turn-expectations-into-work-you-can-deliver}
### Part IV — COMMIT: Turn Expectations Into Work You Can Deliver

- [COMMIT: Turn Expectations Into Work You Can Deliver](#part-4) — part introduction
- **16.** [Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking)
- **17.** [Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards](#have-your-numbers-ready)
- **18.** [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything)
- **19.** [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue)
- **20.** [Clarify AI Strategy: Three Different Investment Questions](#ai-strategy-three-questions)
- **21.** [Assess Capability: Can the Team Deliver?](#can-the-team-deliver)
- **22.** [Manage Funding Delays: Revise the Cash Plan and Commitments](#the-financing-slipped)

{id: introduction--part-v-scale-change-the-team-the-systems-and-the-company-deliberately}
### Part V — SCALE: Change the Team, the Systems and the Company Deliberately

- [SCALE: Change the Team, the Systems and the Company Deliberately](#part-5) — part introduction
- **23.** [Scale the Team Up: Headcount Is Not Capacity](#fix-decisions-before-hiring)
- **24.** [Scale the Team Down: Decide What Work Stops, Not Just Who Leaves](#anatomy-of-a-layoff)
- **25.** [Scale the Team With AI: Capacity Claims Need the Same Evidence as Headcount](#scale-the-team-with-ai)
- **26.** [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design)
- **27.** [Plan Acquisitions and Separations: Account for Extra Work, Not Just Expected Value](#acquisition-adds-work-first)

{id: introduction--part-vi-sustain-keep-the-technology-you-run-worth-its-cost}
### Part VI — SUSTAIN: Keep the Technology You Run Worth Its Cost

- [SUSTAIN: Keep the Technology You Run Worth Its Cost](#part-6) — part introduction
- **28.** [Manage Technical Debt: Fund the Fix by the Cost, the Risk and the Speed It Buys](#manage-technical-debt)
- **29.** [Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore)
- **30.** [Critically Evaluate Cloud Costs: A Lower Bill Is Not Always Better](#cheaper-cloud-bill)
- **31.** [Critically Evaluate AI Costs: Measure the Return per Task and per Period](#ai-worth-its-cost)

{id: introduction--part-vii-lead-manage-funding-and-ownership-changes}
### Part VII — LEAD: Manage Funding and Ownership Changes

- [LEAD: Manage Funding and Ownership Changes](#part-7) — part introduction
- **32.** [Use Diligence: Correct the Plan Before It Is Signed](#diligence-corrects-the-plan)
- **33.** [Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days)
- **34.** [Manage the Handover: Carry Forward the Evidence and Obligations](#handover-of-obligations)

{id: introduction--part-viii-learn-lessons-from-the-field}
### Part VIII — LEARN: Lessons From the Field

- [LEARN: Lessons From the Field](#part-8) — part introduction
- **35.** [Hilton and Skype: A Successful Exit Still Needs Explaining](#hilton-and-skype)
- **36.** [Visma: Continuity of Manager Is Not Continuity of Money](#visma)
- **37.** [Toys R Us: Positive Operating Earnings, Too Little Cash](#toys-r-us)
- **38.** [TeamSystem: Each New Owner Inherits Progress and Unfinished Work](#teamsystem)
- **39.** [Success for Whom, and for How Long?](#success-for-whom)

{id: introduction--appendix}
### Appendix

- [Appendix: Grounded Architecture Across an Investment Portfolio](#grounded-architecture-portfolio) — the author’s Grounded Architecture framework applied across a portfolio, the set of companies one investor holds: reuse the shared data and people foundations, adapt the way decisions and responsibilities are organized in each company.

{id: introduction--reference-material}
### Reference Material

- [Practical Tools for Ownership and Technology Decisions](#toolkit) — practical decision and support records, with one finding followed all the way through.
- [Fund Economics: Fees, Distributions and Performance Reports](#fund-economics) — optional depth on how an investment fund’s money flows: the fees its manager charges, distributions (money the fund pays out to its own investors, which is not funding for the company) and reports on investment performance.
- [Glossary](#glossary) — plain-language definitions and an alphabetical index.
- [Bibliography and Evidence Guide](#bibliography) — sources, consultation dates and evidence limits.
