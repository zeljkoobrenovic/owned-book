{id: data-foundations-for-alignment}
# 37. Appendix: Data Foundations for Alignment With Investors

![Appendix: Data Foundations for Alignment With Investors — logo](private-techuity/posts/data-foundations-for-alignment/assets/images/data-foundations-for-alignment/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn which financial, planning and technology evidence an investor relationship needs, how to build it from sources you already have, and how to label a figure so nobody mistakes a forecast for a result.

> **WHY INVESTORS CARE:** An investor that cannot trace a number back to a source has to give it less weight, and that applies to your good news as well as your bad. Evidence that arrives late, is defined differently each quarter or blurs a projection into a result costs the company credibility precisely when it needs to be believed.

> **WHY YOU SHOULD CARE:** Without shared evidence, a disagreement about priorities becomes a contest of assertion, and the person with more authority wins it. With shared evidence, you can show what a commitment would cost, what the last one actually produced and which assumption the plan is resting on.

> **KEY POINTS:**
>
> * Build the picture from **sources you already have**. Code repositories, cloud bills, incident records, delivery-tracking tools and the finance system already hold most of the evidence; the work is curating, defining and connecting it, not buying a platform.
> * **Define once, own by name, refresh on a stated schedule.** A measure without a written definition, a named owner and a refresh date produces a different answer each time someone asks, and the difference gets attributed to the business rather than to the arithmetic.
> * **Label every figure as actual, target, forecast or assumption — and a resource the board has authorized as committed.** The most expensive reporting mistake is not an inaccurate number; it is an accurate projection read as an observed result.

At Larkspur's day-100 board review — the meeting of the directors who oversee the fictional scheduling-software company — the papers report on a pilot that automated part of customer **onboarding**, the setup work before a new customer can use the product. The eight customers set up during the pilot took an average of 62 hours each, against about 80 hours for the customers set up before it. Someone asks what that is worth. The answer in the papers is €135,000 a year.

Both figures are correct, and together they are misleading. The 62 hours is an average: eight customers, 496 hours of real work, observed. The 80-hour baseline would have implied 640 hours for the same eight, so 144 hours fewer. That is a result.

The €135,000 is 100 implementations a year × 18 fewer hours each × €75 an hour. It is a projection, and it rests on three things nobody has observed: that about 100 customers will be set up next year, that an hour of staff time is worth €75, and that the 18-hour difference seen in eight customers will hold for the next hundred. It values staff time freed for other work, which becomes money only if the company actually avoids a payment or collects more from additional customers than serving them costs. One number is a result. The other is arithmetic about a future that has not happened. Printed in the same column, in the same typeface, they look like the same kind of thing.

This is what a data foundation is for. Part II has established who decides ([Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides)), what each party stands to gain or lose ([Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets)) and how the relationship behaves under pressure ([Assess Investor Fit: Behavior Under Pressure](#investor-under-pressure)). Those arrangements only work when everyone involved is reasoning about the same facts. This chapter is about assembling the facts: what evidence the relationship needs, how to build it from what you already have, how to keep it honest and what to share.

The argument is not that better data produces agreement. It is that **better data makes disagreement useful**. Two people looking at the same defined, sourced, dated figures can disagree about what to do and discover exactly where their views diverge — a volume assumption, a risk tolerance, a time horizon. Two people looking at different numbers, or at the same number understood differently, argue about reality and never reach the decision.

{id: data-foundations-for-alignment--start-from-the-sources-you-already-have}
## Start From the Sources You Already Have

The instinct when an investor asks for better reporting is to start a project: a data warehouse (a central store that combines data from many systems for reporting), a platform, a business-intelligence tool (software for building reports and dashboards), a quarter of work connecting systems to each other. That instinct is usually wrong, and it is wrong for a practical reason. The evidence already exists, scattered across systems that were built for other purposes.

This book's author has written about this pattern elsewhere. **Lightweight Architectural Analytics**, a practice described in *Grounded Architecture*, builds an architecture-centric picture of an organization's technology landscape — its systems and how they depend on one another — by curating sources that are already there: source-code **repositories** (where the software's code is kept, with the record of every change made to it), the bills from public-cloud providers (computing rented from an outside supplier rather than run on the company's own servers), incident records, and business and finance data — rather than by purchasing software or standing up a data warehouse on day one. [S106: Lightweight Architectural Analytics](https://grounded-architecture.io/analytics) The implementation is deliberately modest: consistently organised data files whose every change is recorded, small scripts that generate the reports, and simple web pages built in advance, all maintainable by a small team. [S107: Building Lightweight Architectural Analytics](https://grounded-architecture.io/data-website)

The proposal in this chapter is to extend that principle from the technology landscape to the investor relationship. The sources widen — the finance system, the customer records, the sales pipeline and the delivery tools join the repositories and the cloud bill — but the method is the same: curate what exists, connect it, keep it current, and let people trace any figure back to where it came from.

From that practice's account of what its data has to be, this chapter distils five qualities. The wording and the grouping are this chapter's — the practice's own headings are organised a little differently — and they are the standard the rest of this chapter applies:

| Requirement | In the investor relationship |
| --- | --- |
| **Curated** | Someone is responsible for the quality of each measure. Accuracy is a person's job, not a property of the tool. |
| **Current** | Refreshed by a repeatable process on a stated schedule, so nobody asks how old the number is. |
| **Credible** | Traceable to the original source. A reader who doubts a figure can follow it back rather than argue about it. |
| **Actionable** | Present in real decisions. A measure nobody has ever used to decide anything is overhead. |
| **Accessible** | Available to the people who need it, at a level of detail appropriate to each, without a request queue. |

![Five ordinary sources feed one curated layer, which supports three connected areas of evidence: financial and business, planning and execution, and product and technology.](private-techuity/posts/data-foundations-for-alignment/assets/images/data-foundations-for-alignment/three-areas-one-foundation.jpeg)

**Figure 1:** *One curated layer, built from sources the company already keeps, supports three areas of evidence. The areas are connected to each other, not ranked.*

{id: data-foundations-for-alignment--the-three-areas-and-how-they-connect}
## The Three Areas, and How They Connect

Investor conversations fail in a particular way. Financial results are discussed with precision, execution is discussed in anecdote, and technology is discussed either not at all or as an unexplained cost line. The three areas below are not three reports. They are three views of one business, and the value is in connecting them: a revenue forecast means little without the roadmap that is supposed to produce it, and that roadmap means little without evidence that the systems and teams can carry it.

{id: data-foundations-for-alignment--financial-and-business-evidence}
### Financial and Business Evidence

This is the area with the most mature conventions, and the one where a product or engineering leader most often defers entirely to finance. Defer on the preparation; do not defer on understanding what the figures assume, because those assumptions become your commitments.

- **Revenue**, the amount earned from supplying goods or services during a period — whether the customer paid earlier, at the time or later. A year's subscription paid up front is earned across the year; a training course delivered in March and paid for in May is March's revenue, not May's. Setup work that only enables a continuing subscription is the awkward case: it is earned along with the subscription it enables, not on the day the setup is finished, so Larkspur's onboarding hours are a cost figure, not a revenue one. Break it down in ways that reveal its character: recurring against one-off, by product, by customer segment (a group of similar customers), by market. A single total hides whether growth came from more customers, higher prices or one large deal.
- **Profitability** — what remains of revenue after costs are deducted — on a stated basis, meaning it says which costs and which accounting rules it includes; and **cash flow**, the money actually received and paid in a period. The chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget) covers why these differ and why the second constrains you.
- **Cost structure**: what is fixed, what varies with the volume of business, and what is genuinely discretionary within the year — spending that could be postponed or dropped without breaking a commitment. This is where technology cost belongs, and where a cloud bill stops being an unexplained line.
- **Unit economics**: what it costs to win, serve and keep one customer, against what that customer pays over the relationship. Larkspur's 80 hours of onboarding effort per customer is a unit-economics figure that happens to be measured in engineering and setup time rather than money.
- **Customer retention**: who stayed, who left, what they were worth, and why they left where it is known. Retention is the measure most often reported as a single percentage and least often reported with a definition.
- **Sales pipeline**: the potential sales in progress — what is being sold, at what stage, with what probability, and with what history of those probabilities proving right. A pipeline without a record of what share of past deals actually became sales (the conversion rate) is a list of hopes.
- **The assumptions behind growth forecasts**, written down separately from the forecast itself: the volume of customers or sales, the price, the share of deals that convert, the capacity to serve them. When the forecast misses, this is the list you return to.

{id: data-foundations-for-alignment--planning-and-execution-evidence}
### Planning and Execution Evidence

This area is usually the weakest, because it is nobody's reporting duty. It answers whether the company does what it said it would.

- **Strategic priorities** and **investment plans**: where the money and the team's capacity are going, at a level of aggregation a board can actually discuss. The chapter [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything) covers choosing among these.
- **Roadmaps and milestones** — the plan of intended product work and its significant checkpoints — with dated commitments and their current status. The useful record is not the roadmap as it stands today but the roadmap as it stood when the commitment was made, kept alongside it.
- **Resource allocation**: how engineering capacity is actually distributed across new product work, maintenance, reliability, compliance and support. Most companies discover on first measurement that the split differs substantially from the plan.
- **Dependencies**: what a commitment requires from outside the team delivering it — another team, a supplier, a legal or contractual step, a customer's own work. Larkspur's market entry depended on billing, legal, support and product configuration moving together; engineering alone could not complete it.
- **Delivery performance**: how long work takes from commitment to customer availability, and how predictable that is. The chapter [Assess Capability: Can the Team Deliver?](#can-the-team-deliver) covers what to measure and the trap of measuring only the part of the process that engineering controls.
- **The gap between commitments and outcomes**, kept deliberately. This is the single most valuable and least maintained record in the set: what was promised, what arrived, when, and what the difference was. Kept honestly for four quarters, it tells an investor more about the company's judgment than any forecast.

{id: data-foundations-for-alignment--product-and-technology-evidence}
### Product and Technology Evidence

This is the area a product or engineering leader owns outright, and the one where the absence of evidence is most often mistaken for the absence of a problem.

- **Product adoption and usage**: who uses what, how often, and whether use is growing, concentrated or declining. Distinguish activity from value; logins are not outcomes.
- **Customer outcomes**: what the product actually achieves for the customer, in the customer's terms. Larkspur's customers care about schedules dispatched on time, not about the scheduling engine's uptime (the share of time the service is available) — though the second serves the first.
- **Portfolio performance**: which products, modules and lines earn their cost of maintenance and which do not. Portfolios accumulate; without this evidence, nothing is ever retired.
- **Architecture**: the actual structure of the systems, including what depends on what. Larkspur's country-specific rules living inside the invoicing module was an architectural fact with a direct commercial consequence for market entry.
- **Technical debt**: where past shortcuts now make change slower or riskier, recorded as specific constraints on specific future work rather than as a general complaint about quality.
- **Reliability**: incidents (service failures that reach customers), their frequency, their customer impact, and whether recovery has been demonstrated rather than assumed. The chapter [Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore) is an extended argument that an untested recovery capability is not evidence of anything.
- **Security**: the protections in place and the obligations the company must meet; and **scalability**: what the systems can carry today and what the growth plan would require of them.
- **Technology cost**: the cloud bill, licences and suppliers, attributed to products or capabilities so that cost can be discussed against value. The chapter [Critically Evaluate Cloud Costs: A Lower Bill Is Not Always Better](#cheaper-cloud-bill) covers the attribution.
- **Engineering delivery capability**: the size, composition, key-person concentration and skills of the teams. Larkspur's diligence — the investigation of the company before the investment — found that one specialist was the only person who could release and recover the scheduling engine — an evidence-based constraint on every plan that assumed that engine could change quickly.

The connection is the point. Larkspur's onboarding automation appears in all three areas at once: as unit economics (hours and cost per customer), as an execution commitment (€180,000 and twelve engineer-weeks — an engineer-week being one engineer's working week, a planning unit rather than elapsed time — with a dated review), and as product and technology evidence (the configuration work, the customer-data quality problem, the capacity it releases). A conversation that only has the first is a conversation about a number nobody can act on.

{id: data-foundations-for-alignment--define-it-once-own-it-by-name-refresh-it-on-a-schedule}
## Define It Once, Own It by Name, Refresh It on a Schedule

Most reporting disputes are definition disputes wearing a disguise. Someone reports retention at 94% and someone else at 88% — one counting customers kept, the other counting the revenue they represent, over different periods — and an hour disappears into reconciling the two that should have gone into deciding something.

The fix is unglamorous and durable. For each measure that matters, record five things in one place, and keep them with the measure rather than in a separate document nobody opens.

| Field | Larkspur's onboarding effort measure |
| --- | --- |
| Definition | All human hours spent setting up one customer, end to end — Larkspur's own staff, the contract implementation specialist and any bought-in data-entry help, whoever pays them — including all time spent checking and correcting the customer's data, before or during setup |
| Source | The implementation team's time records, reconstructed per customer |
| Owner | Priya, the product leader |
| Refresh | Per customer cohort — the group of customers set up in the same period and measured together; reported at each quarterly review |
| Boundaries | Excludes automated checking by the outside validation service, which has no hours and is carried separately as a continuing cost, per customer and per year |

Each field earns its place. The **definition** settles the arguments in advance: "whoever pays them" is why the contract specialist's hours and bought-in help count — fifty staff hours plus twenty supplier hours is seventy, not fifty, so the figure cannot be improved by moving manual work to a supplier — and why an outside service's automated checks, which nobody spends hours on, are carried as money instead. The **source** makes the figure credible — a reader who doubts 62 hours can go to the time records. The **owner** is a person, not a team: someone answerable for the number being right and for saying so when it is not. The **refresh** frequency stops the "how current is this?" exchange that precedes every stale decision. The **boundaries** state what the measure deliberately excludes, which is where most double-counting begins.

Two rules keep the set useful. First, **define a measure once and change it rarely**; when a definition must change, restate the history on the new basis or say clearly that the series breaks. A changed definition presented as a changed result is indistinguishable from bad news being managed. Second, **keep the set small**. Fifteen measures nobody disputes are worth more than ninety nobody trusts; one of the five qualities is that a measure be *actionable* — present in real decisions — and one that has never changed a decision should be retired.

{id: data-foundations-for-alignment--someone-has-to-do-this-work}
## Someone Has to Do This Work

Everything above is work, and it is work that falls between existing roles. Finance owns the financial close — checking and finalising the accounts for each period — not the definition of onboarding effort. Engineering owns the repositories and the incident records, not their translation into a board measure. Product owns the roadmap, not the record of what was committed four quarters ago. Left unassigned, the work happens in the fortnight before a board meeting, performed by whoever is least able to refuse — which is how a company ends up rebuilding the same figures every quarter and disagreeing about them each time.

**Product operations** is the discipline that has formed around this gap. In the account by Melissa Perri and Denise Tilles, it rests on three pillars, and the correspondence with this chapter's three areas is close enough to be useful. [S109: Perri and Tilles, *Product Operations*](https://melissaperri.com/book)

| Product operations pillar | What it does | This chapter's area |
| --- | --- | --- |
| **Business data and insights** | Gathers information on how the product and the company are performing, extracted from existing business systems, with standardized definitions so leaders can compare across products | Financial and business evidence, and the commercial half of product evidence |
| **Customer and market insights** | Collects descriptive and numerical research from outside the company and passes it to the teams that need it | Customer outcomes, adoption and the market assumptions behind forecasts |
| **Process and governance** | Establishes consistent practices for how product work is planned, committed and reviewed — consistency with necessary variation, not uniformity | Planning and execution evidence, especially the record of commitments against outcomes |

Three things about this framing are worth carrying into the investor relationship.

**The pillars describe the same connection this chapter argues for.** Perri and Tilles put the joining of financial performance to what teams actually build at the centre of the first pillar. That is precisely the connection an investor conversation needs and most often lacks — and it is the same joining that Lightweight Architectural Analytics performs on the technology side, from the other direction.

**Standardized definitions are named as the mechanism, not a by-product.** The reason a leader can compare two products is that both report on the same definition. This chapter's measure record is one way to hold that standard; the pillar explains why an organization needs someone whose job it is to maintain it.

**It is an infrastructure function, not an approval layer.** Product operations supplies the evidence and the consistent process; it does not take over the decisions, and the discipline's own literature is emphatic that it is not a product manager and not merely a set of tools. The same boundary applies here. The data foundation exists so the people with authority — established in [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides) — can decide well. It does not decide anything.

A small company will not have a product operations function, and does not need one to start. What it needs is the work assigned: a named person per measure, as the record above requires, and one person accountable for the board pack — the set of papers prepared for a board meeting — being consistent, current and honest as a whole. The function is what this becomes when a company grows large enough that doing it informally stops working.

{id: data-foundations-for-alignment--give-a-number-its-context}
## Give a Number Its Context

A figure on its own is not evidence. "62 hours" says nothing until the reader knows what it is being compared with, how many observations it rests on and which way it is moving. Four pieces of context turn a number into something a board can use:

- **Baseline**: what it was before, measured on the same definition. Larkspur's baseline is about 80 hours, reconstructed from the time records of the twelve implementations of the previous two quarters, not measured in advance.
- **Comparison**: what it was expected to be. The plan anticipated 50 hours; the cohort produced 62. The gap is the interesting part, and it is where the data-quality finding came from.
- **Direction and confidence**: which way it is moving and how much weight the figure carries. The pilot group averaged fewer hours than the earlier group. That is one observed difference between two groups, not a trend over time, and it does not by itself show that the automation caused it: sales chose which customers went through the pilot first, the same specialist served both groups and may have grown faster with practice, and the baseline was reconstructed after the fact. The honest report states the difference, states those limits, and leaves the causal claim at "plausibly helped" — the chapter [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue) works through what such a comparison can and cannot establish.
- **Decision link**: what this figure is used to decide. At Larkspur, the thresholds were agreed in advance — under 60 hours would allow Priya to request the next stage of onboarding work, which would still need its own approval; 60 to 70 supports a data-quality step (checking and correcting each customer's data before setup begins) while expansion and hiring stay deferred; over 70 reopens the plan. At 62 hours the recommendation was settled before the meeting began. What remained for the board was the money: the step costs €40,000 and four engineer-weeks from the reserve the board holds back for later decisions, and a draw on that reserve is the board's to approve, which it did. The rule chooses the recommendation; it does not spend anything.

That last point deserves emphasis, because it is where data stops being reporting and becomes alignment. **Thresholds agreed before the measurement** convert a potential argument into an arithmetic check. The investor and the company disagree about the threshold in advance — which is the right time to disagree, before the result is known and while nobody has a number to defend — and then both accept what the measurement says.

{id: data-foundations-for-alignment--label-what-kind-of-number-it-is}
## Label What Kind of Number It Is

Return to the day-100 board papers. Four kinds of statement about results and the future were in them, and only one was a fact about the past. A fifth kind, the resources authorized for the work, sits beside them:

![Four identical cards distinguished only by hanging tags reading Actual, Target, Forecast and Assumption; only the Actual card is anchored to something below it.](private-techuity/posts/data-foundations-for-alignment/assets/images/data-foundations-for-alignment/four-kinds-of-number.jpeg)

**Figure 2:** *The four kinds of statement look identical on a page. The label is what separates a measured result from arithmetic about a future that has not happened.*

| Kind | What it is | Larkspur's day-100 papers |
| --- | --- | --- |
| **Actual** | Observed and recorded, on a stated definition | 496 hours of work across eight customers, an average of 62; 144 hours fewer than the 640 the 80-hour baseline implies; about €90,000 of the pilot's €180,000 incurred — work or services already received, whether or not the invoices have been paid |
| **Target** | The result the plan set out to reach, and by when — a desired outcome, not a contractual promise | 50 hours per customer by the day-90 measurement |
| **Forecast** | A calculation about the future from stated inputs | €135,000 a year of released capacity (100 × 18 × €75) |
| **Assumption** | An input taken as given, which may not hold | 100 implementations a year; €75 an hour fully loaded — wages plus employer charges, benefits and tools, the rate finance uses in plans; and that the 18-hour difference observed in eight customers holds for the next hundred |
| **Committed** | A resource the board has authorized for the work — an input, not a result | €180,000 and twelve engineer-weeks for the pilot; the part consumed so far is reported as an actual |

The fifth row, *Committed*, is there because a board pack always contains figures that are none of the first four. The pilot's €180,000 and twelve engineer-weeks — the onboarding pilot carries the identifier ONB-1 in Larkspur's plan — are the resources committed to the work: an input the board authorized, tracked as committed against incurred, not a result anyone was aiming at. Labelling them *committed* keeps them from being read as a target that was missed or a cost that has already been paid.

Two further points keep the table honest. The third assumption is the easiest to forget. Sales chose the eight pilot customers, so the 18-hour difference they showed may not hold for the customers who follow, and the forecast is only as good as that continuation.

And cash conversion is not an assumption behind the €135,000 at all. The forecast values freed time; it does not forecast cash receipts or payments. A cash forecast would need further conditions on top.

Written this way, the €135,000 is still worth reporting — it is the revised value of the benefit the work was funded for; the original case, at 50 hours, was 100 × 30 × €75 = €225,000 — but it can no longer be mistaken for money the company has. It is 1,800 hours of projected capacity a year, at an assumed volume, valued at an assumed rate, on the assumption that the observed difference continues. And it is gross: the pilot's remaining €90,000 and its €30,000 a year of upkeep sit beside it, not inside it.

When could any of it become money? **Capacity becomes cash only when a payment is actually avoided or additional customer receipts exceed the cash cost of serving those customers**, on a date. At Larkspur the nearest such date is month twelve. The contract implementation specialist engaged to work through the customer queue runs until then under every option the board weighed, so nothing could be cancelled by day 100. Not extending that contract — only if the queue is moving by then — is the first payment the pilot could avoid.

The deferred hire of two specialists is spending avoided, not spending reduced. Deciding not to hire changes nothing in the bank on the day of the decision; the difference appears only on the paydays those salaries would have fallen on.

Larkspur's own finance discipline excludes the €135,000 from **debt service** — the interest and loan repayments the company must meet — for exactly that reason. Loan payments fall on fixed dates, and projected capacity has none.

The labelling rule is one line, and it is the highest-value convention in this chapter: **every figure in a document that goes to a board or an investor carries its kind.** Four words for anything that describes a result or a future — actual, target, forecast, assumption — and *committed* for a resource the board has authorized. One word per number. The cost is a few minutes of preparation. The benefit is that the company never has to explain, six months later, why a result it appeared to report did not arrive.

{id: data-foundations-for-alignment--decide-what-is-internal-and-what-is-shared}
## Decide What Is Internal and What Is Shared

Not everything should go to an investor, and not everything an investor asks for is theirs by right. Three distinctions keep this straightforward.

**Rights against courtesy.** An investor's **information rights** — the reporting it is contractually entitled to, typically set out in the investment agreement — are specific: usually periodic financial statements (the reports of the company's results and financial position), a budget, a capitalization table (the record of who owns which shares) and sometimes board materials, on a stated schedule. The contract is not the only source of entitlement, though. What a particular recipient may see depends on applicable law, the company's governing documents, the contracts and the recipient's role: a director the investor appointed receives board materials as a director, and shareholders may hold inspection rights under company law that no contract grants. Beyond those entitlements, disclosure is a choice. Knowing which is which changes the conversation from "must we?" to "should we, and in what form?" Check the actual agreements rather than assuming either extreme; where an obligation is unclear or a request touches customer or employee data, involve the people qualified to advise.

**Detail against aggregation.** The same evidence is appropriate at different resolutions. The working detail that makes a measure useful internally is rarely what makes it useful to a board.

| Evidence | Held internally | Appropriate to share |
| --- | --- | --- |
| Onboarding effort | Per customer, per activity, per person | Cohort average against baseline and threshold, with the definition |
| Incidents | Every incident, with full timeline and names | Frequency, customer impact, recurring causes, what changed |
| Technology cost | Every service and account line | Attributed to products or capabilities, against the plan |
| Delivery | Per-team, per-initiative detail | Commitments against outcomes, with the reasons for gaps |
| People | Individual performance and pay | Key-person concentration, skills gaps, retention risk as it affects commitments |

Individual performance data, personal data and identifiable customer data stay internal by default, and handling them — including any properly authorised access — is governed by obligations well outside this chapter's scope.

**Raw access against curated reporting.** Investors sometimes ask for direct access to a system. This is worth treating carefully — not because there is anything to hide, but because a figure pulled without its definition creates precisely the disputes the definitions exist to prevent. A reasonable response is usually to widen what is shared and keep it curated: more measures, more history, full definitions, sources named, on a regular schedule, with a route for specific questions. If an investor still wants raw access, ask what question it answers; frequently the answer is a measure you can define and provide properly.

One principle simplifies the rest: **share the evidence that supports decisions the recipient is entitled to participate in.** The board approves the plan, so a director the investor appointed receives the evidence the plan rests on, with its assumptions visible — as a director. The investor itself receives what its information rights provide and, where the investment agreement gives it a separate consent right over the plan, the evidence that consent needs. Whether the director may pass board papers on to the investor depends on the arrangement and any confidentiality terms; check rather than assume. Investors do not run the engineering team, so they do not need its internal working detail — and offering it usually starts a conversation neither side has time for.

![Dense working records inside the company pass through an open gate and are aggregated into a single shared sheet, which carries a tag reading With its definition.](private-techuity/posts/data-foundations-for-alignment/assets/images/data-foundations-for-alignment/internal-and-shared.jpeg)

**Figure 3:** *The same evidence at two resolutions. What crosses the boundary is aggregated and carries its definition with it.*

{id: data-foundations-for-alignment--build-it-in-the-order-that-pays}
## Build It in the Order That Pays

Nobody assembles all of this at once, and a company that tries produces a large document instead of a working foundation. Build in the order that changes decisions soonest.

1. **Start with the decision in front of you.** Not "what should we report?" but "what does the next consequential decision need?" At Larkspur the next decision was whether to fund the expansion, so the evidence that mattered was the cohort's effort split and the waiting time. Everything else could wait.
2. **Find where the evidence already lives.** Time records, repositories, the cloud bill, incident records, the finance system, the customer records. Most measures need connecting, not creating.
3. **Write the definition before the first number.** Define the measure, name the owner, state the refresh frequency and the boundaries. Five minutes now; an hour of reconciliation saved every quarter.
4. **Establish the baseline honestly.** Reconstruct from real records, state how many observations it rests on, and say where it is weak. Larkspur's 80 hours came from twelve implementations, and the chapter that used it said so.
5. **Agree thresholds in advance**, with whoever will act on them. This is the step most often skipped and the one that most reliably prevents a dispute.
6. **Automate the refresh, not the interpretation.** A repeatable process keeps the figure current; a person still has to say what it means. Two of the five qualities are that data be current *and* curated — automation serves the first, never the second.
7. **Add measures only when a decision needs them.** The set grows by pull, not by push.

A useful test at each step: could someone who doubts this figure trace it to its source in under ten minutes? If not, the problem is not the reader's scepticism.

{id: data-foundations-for-alignment--what-this-does-not-fix}
## What This Does Not Fix

Shared evidence does not produce agreement, and a chapter that implied otherwise would be selling something. An investor and a company can look at the same well-defined figures and still want different things, because they are exposed differently — the subject of [Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets). Evidence does not resolve a disagreement about risk appetite, time horizon or what the company is for.

Data can also be used badly. A measure can be chosen because it flatters, a threshold can be set where it is easy to pass, a definition can be quietly revised in a bad quarter, and a comprehensive pack can bury a material problem in volume. None of these is prevented by having more data; several are made easier by it. The defences are the ones already described — definitions that change rarely and visibly, thresholds agreed in advance, figures traceable to sources, and a deliberately small set — plus a leader willing to report the number that is not flattering.

What shared evidence does is narrower and still valuable. It moves disagreement from what is true to what to do, makes the assumptions in a plan visible before they fail, and gives a leader a way to show the cost of a commitment rather than merely assert it. When Larkspur's cohort came in at 62 hours rather than 50, the evidence did not settle whether to expand. It established that the pilot group had averaged fewer hours than the earlier group, with the comparison's limits stated; that about 40% of what remained traced to customer data quality; and that under the rule agreed in advance the recommendation was the data-quality step, with expansion waiting for the next review. It let the company propose that step with a specific cost — €40,000 and four engineer-weeks, which the board then approved from its reserve — rather than defend a disappointing number.

And it left the next test already agreed. The second group of customers, set up after the data-quality step, must pass two checks:

- **Effort:** an average of 50 hours or less per customer, on the same definition as before.
- **Waiting time:** a median of eight weeks or less from signed contract to first real use. The median is the middle value when the eight waits are put in order — for a group of eight, the average of the fourth and fifth — so, unlike the average used for effort, one customer who waits half a year does not drag it up.

Passing lets Priya request a further stage; it approves nothing by itself.

{id: data-foundations-for-alignment--a-small-record-you-can-reuse}
## A Small Record You Can Reuse

[Tool 15](#toolkit--tool-15) gives the measure record used above. For a measure that is going into an investor conversation, fill in the definition, source, owner, refresh frequency and boundaries; then, for each figure you report from it, the baseline, the comparison, the kind (actual, target, forecast or assumption — or committed, for a resource the board has authorized) and the decision it informs. If a measure cannot be given an owner or a decision, it probably should not be in the pack.

Part II established who decides, what each party stands to gain or lose and how the relationship behaves under pressure; this appendix has assembled the evidence all three depend on. Part III shows what this evidence is for: choosing among things the company cannot all afford, and committing only to what it can deliver — [COMMIT: Turn Expectations Into Work You Can Deliver](#part-3) and [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything).

{id: data-foundations-for-alignment--questions-to-consider}
## Questions to Consider

1. *Take the three figures most often quoted in your investor conversations. For each, can you state the definition, the source, the owner and when it was last refreshed — without asking anyone?*
2. *Look at your last board pack. How many figures in it are actuals, and how many are forecasts or targets presented in the same typeface?*
3. *Which of your current commitments rests on an assumption that is nowhere written down? What would it cost you if that assumption is wrong?*
4. *What does your investor receive by right, and what do you provide by choice? Would your investor answer that question the same way you just did?*
5. *If you kept a record of commitments against outcomes for the last four quarters, what would it show — and who in the company already knows?*

{id: data-foundations-for-alignment--to-probe-further}
## To Probe Further

- **[Lightweight Architectural Analytics](https://grounded-architecture.io/analytics)** — Željko Obrenović, *Grounded Architecture*.  
  *The author's own account of the practice this chapter extends: building a current picture of the technology landscape by curating source-code, cloud-billing, incident and business data, and the account of what its data must be from which this chapter distils its five qualities — curated, current, credible, actionable, accessible.*
- **[Building Lightweight Architectural Analytics](https://grounded-architecture.io/data-website)** — Željko Obrenović, *Grounded Architecture*.  
  *The implementation companion: structured data files whose every change is tracked (version control), small programs that generate the reports, and web pages built in advance rather than on request, all maintained by a small team. Relevant if your instinct on reading this chapter was to start a platform project.*
- **[Product Operations: How Successful Companies Build Better Products at Scale](https://melissaperri.com/book)** — Melissa Perri and Denise Tilles, 2023.  
  *The fullest treatment of the discipline that maintains this kind of evidence: the three pillars, why standardized definitions are the mechanism rather than the by-product, and how the function supplies evidence without taking over the decisions. Read it if the work in this chapter keeps landing on whoever is free.*
- **[Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/)** — Nicole Forsgren, Jez Humble and Gene Kim, IT Revolution, 2018.  
  *The research behind the delivery measures most often quoted to investors (DevOps is the practice of joining software development and its operation into one flow of work), including what they do and do not establish. Useful for the execution area, and for understanding why measuring only the part of delivery that engineering controls flatters the picture.*
- **[How to Measure Anything: Finding the Value of Intangibles in Business](https://www.howtomeasureanything.com/)** — Douglas W. Hubbard, Wiley, 3rd edition, 2014.  
  *An argument that measurement is about reducing uncertainty for a decision, not achieving precision. It supports this chapter's rule that a measure with no decision attached should be retired.*
