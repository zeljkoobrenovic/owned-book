{id: have-your-numbers-ready}
# 18. Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards

![Have Your Numbers Ready: Metrics for Investors, Goals and Dashboards — logo](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn which measures matter when investors own part of your company, which of them you own and which you must merely understand, how to hold a small set of them ready before anyone asks, and how the same numbers serve the investor conversation, your goals and your dashboards.

> **WHY INVESTORS CARE:** An investor relies on your reports for the work it does not see day to day. A figure that arrives late, is defined differently each quarter or blurs a projection into a result has to be given less weight, and that applies to your good news as well as your bad.

> **WHY YOU SHOULD CARE:** The questions arrive before the numbers exist. When they arrive, the answer is assembled in a hurry, each function brings its own version, and a disagreement about what to do turns into an argument about what is true. With the numbers ready, you can show what a commitment costs, what the last one produced and which assumption the plan rests on.

> **KEY POINTS:**
>
> * **Know the catalogue, then keep a small set.** Money and runway, customers and growth, product outcomes, delivery, technology health and people each have a handful of standard measures. Know what each one tells and where it misleads. Report the dozen that your decisions and your outcome record actually need.
> * **Hold every number ready: defined once, owned by name, refreshed on a schedule, and labelled.** Each figure carries its definition, source, owner and context, and its kind: **actual, target, forecast** or **assumption**, or **committed** for a resource the board has authorized. The most expensive reporting mistake is an accurate projection read as an observed result.
> * **One set of numbers, three uses.** The same measures feed the investor conversation, the goals teams work to and the dashboards used by the board, the leadership and the teams, each at its own level of detail. Every figure on the board’s page should trace down to work a team is doing.

After an investment, requests for numbers arrive quickly: a reporting template from the investor, a question from an adviser, the papers for a board meeting a few weeks away. Most companies already hold much of the evidence, in their accounts, time records, incident logs and sales pipelines. But it is **scattered across systems**, defined differently by each function and rarely ready when someone asks. The usual result is a **scramble before every meeting** and an argument about whose figure is right, rather than about what to do.

This chapter’s argument is not that better numbers produce agreement. It is that **ready numbers make disagreement useful**. Two people looking at the same defined, sourced and dated figures can disagree about what to do and find exactly **where their views part**: a volume assumption, a risk tolerance, a time horizon. Two people looking at different numbers, or at the same number understood differently, argue about reality and never reach the decision.

The chapter starts from the sources a company already has and sets out a catalogue of what is worth measuring. It then shows how to pick a small set, hold each number ready and label what kind of number it is, and how the same set serves the investor conversation, team goals and dashboards. It ends with who does the work, the order in which to build it and what ready numbers do not fix.

{id: have-your-numbers-ready--setting-up-the-example-two-requests-in-one-week}
## Setting Up the Example: Two Requests in One Week

Larkspur, the fictional scheduling-software company this book follows, has just agreed its outcome record in the chapter [Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking): the one-page record of the change customers should see, the business result it should produce and the measures that connect the two. In the same week, Larkspur receives two requests.

Larkspur’s investor is a fund: a pool of money gathered from many investors and used to buy parts of companies. The fund’s portfolio team, the people who follow the companies it has invested in, sends its standard quarterly reporting template: two pages of financial and operating measures, several of which Larkspur has never calculated. Meanwhile, Morgan, the investor’s technology adviser, asks Priya a simpler question: how long does it take to set up a new customer, and how does she know?

The raw material for both answers exists. Sam, who leads finance, has monthly accounts. Priya has the specialist’s time records. Alex, the chief technology officer (CTO), has incident records, the cloud bill (the monthly charge for the rented computing the software runs on) and the code repositories. Sales has its pipeline, the list of deals in progress.

None of it is wrong, but none of it is ready. Nobody has written down what “setup time” means, whether it counts the contract specialist’s hours, or which of the figures in the setup proposal are observed and which are hoped for.

Ines, the chief executive, runs the company day to day. She answers to its **board**: the directors who oversee the company for its owners; the investor has a seat on it. The board approves the plan and any spending outside it. Ines has seen what happens next in other companies: the numbers get rebuilt in the fortnight before every board meeting, by whoever cannot refuse, and are argued over each time.

{id: have-your-numbers-ready--start-from-the-sources-you-already-have}
## Start From the Sources You Already Have

The instinct, when an investor asks for better reporting, is to start a project: a data warehouse (a central store that combines data from many systems for reporting), a business-intelligence tool (software for building reports and dashboards), a quarter of work connecting systems. The evidence mostly exists already, scattered across systems that were never meant to be read together: the finance system, the billing system, the customer records, the sales pipeline, the delivery-tracking tools, the code repositories (where the software’s code is kept, with the record of every change), the cloud bill and the incident records. The work is curating, defining and connecting what is there, not buying a platform.

For the technology part of that picture, the author has described one lightweight way of doing this elsewhere: [Lightweight Architectural Analytics](https://grounded-architecture.io/analytics), in *Grounded Architecture*, builds a current picture of systems, costs and dependencies from repositories, cloud bills and incident records with small scripts rather than a platform. [S106: Lightweight Architectural Analytics](https://grounded-architecture.io/analytics) The same attitude serves the whole set of numbers in this chapter.

![Six existing records on a shelf feed one teal tray labelled defined once, owned by name, refreshed on a schedule, which supplies six cards: money and runway, customers and growth, product outcomes, delivery, technology health and people.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/three-areas-one-foundation.jpeg)

**Figure 1:** *The numbers mostly exist already. The work is defining and connecting them into one curated layer that supplies every family of measures, not buying a platform.*

{id: have-your-numbers-ready--the-catalogue-what-is-worth-measuring}
## The Catalogue: What Is Worth Measuring

The measures below are the ones that come up, again and again, when a company works with investors. They are grouped in six families. The point of the catalogue is not that you report all of them. It is that you know what each one tells, who normally produces it and where it misleads, so that when one is asked for you are not meeting it for the first time.

A **measure** (or metric) is a defined way of counting something. A **key performance indicator (KPI)** is a measure chosen to track a result that matters. A **leading indicator** moves early and gives warning; a **lagging indicator** confirms later that the result happened. The chapter [Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking) uses the same vocabulary.

{id: have-your-numbers-ready--money-and-runway}
### Money and Runway

Finance produces these. A product or engineering leader should not prepare them, but must understand what they assume, because those assumptions become your commitments. **Profit** is revenue minus expenses, counted when the work is delivered and the costs are incurred. **Cash** is money actually received or paid out. The two can differ for months, for example when a customer pays an invoice late. The chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget) explains why that gap matters.

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **Revenue**, split into **recurring** (subscription fees earned again every month or year) and **one-off** (setup fees, services) | How much the company earns, and how much of it repeats | A single total hides whether growth came from more customers, higher prices or one large deal |
| **Annual recurring revenue (ARR)** | The yearly value of all current subscriptions, as if each renewed unchanged | It is a snapshot, not revenue earned and not cash received |
| **Gross margin** | The share of revenue left after the direct cost of serving customers: hosting (renting the computers the software runs on), support and setup | Reclassifying a direct cost as an operating cost — booking setup staff under general operations instead of the cost of serving customers — raises it without changing anything |
| **Operating costs by function** | Where the money goes: product and engineering, sales and marketing, general and administration | Shares of revenue look precise; they depend on how shared costs, such as rent, are divided between functions |
| **Burn** | The net cash the company spends in a month when it spends more than it takes in | One month is noise; read it over a quarter |
| **Runway** | How many months the cash in the bank lasts at the current burn | It assumes the burn stays where it is, which a hiring plan changes |
| **Cash conversion** | How much of profit becomes cash, after the timing of customer payments and bills | Growth can make it worse: more customers owing money at year end |

![Recurring and one-off revenue pipes join into one revenue pipe, which passes a sieve that drains the cost of serving customers and continues as gross margin into a tank labelled cash in the bank; three cost outlets drain the tank, an arrow marks burn and a calendar marks runway.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/money-and-runway.jpeg)

**Figure 2:** *Money and runway as one tank: what comes in and how much of it repeats, what serving customers costs, where the rest goes, and how many months the level lasts at the current burn.*

{id: have-your-numbers-ready--customers-and-growth}
### Customers and Growth

Sales, customer success (the team that helps existing customers get value from the software) and finance own most of these, and investors read them closely because they show whether growth builds on itself.

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **New customers** and **bookings** (the value of contracts signed) | How fast the company wins business | A booking is a promise to pay, not revenue and not cash |
| **Net revenue retention (NRR)** | The recurring revenue from the customers the company had a year ago, now against then, counting their growth, cutbacks and departures | Above 100% can hide many departures behind a few large expansions |
| **Gross revenue retention (GRR)** | The same comparison for the same customers without the growth: how much of their starting revenue stayed | It can never exceed 100%, so it is often left out when it is unflattering |
| **Customer churn** and **renewal rate** | Churn: customers lost during a period, divided by the customers at its start. Renewal rate: of the contracts that came up for renewal in the period, the share renewed | Different denominators — all customers, or only those due to renew — so one is not simply the other’s complement. The units differ too: churn counts customers, this renewal rate counts contracts, so a customer with two contracts counts once in churn and twice here. Neither is weighted by money, so read them beside the retention figures |
| **Customer acquisition cost (CAC)** and **payback** | What it costs in sales and marketing to win one customer, and how many months it takes to earn that back from what the customer pays each month minus the cost of serving it | Which costs are counted changes the answer; state them |
| **Lifetime value (LTV)** | The gross profit a customer is expected to bring over the whole relationship: what it pays, minus the cost of serving it, over the years it is expected to stay | It is a forecast built on retention assumptions, often presented as a fact |
| **Pipeline** and **conversion rate** | The sales in progress, by stage, and the share of past deals that ended in a signed contract | A pipeline without its conversion history is a list of hopes |

![Left: a funnel from pipeline through conversion rate to new customers, beside a stack of coins for acquisition cost. Right: three bars, last year, kept and kept plus expansion; kept is shorter than last year by a dashed outline for what left or was cut back, and kept plus expansion ends taller than last year; they are tagged gross retention and net retention.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/customers-and-growth.jpeg)

**Figure 3:** *Winning customers and keeping them. Net retention can exceed 100% while many customers leave, because expansion hides the gap; gross retention shows what stayed.*

{id: have-your-numbers-ready--product-and-customer-outcomes}
### Product and Customer Outcomes

These are the product leader’s own, and the ones most often missing from the board pack, the set of reports the directors receive before each board meeting. The outcome record from [Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking) chooses which of them matter for this company.

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **Time to first value** (at Larkspur: weeks from signed contract to the first real schedule) | How quickly a customer starts getting what they bought | An average is dragged by one slow customer; the median, the middle value, is steadier |
| **Activation** (reaching a defined starting point — at Larkspur, as in the outcome record, the day the customer’s account is ready to use; the first real schedule, which can come days or weeks later, is first value) and **depth of use** (how much of the work then runs through the product — at Larkspur, the share of a customer’s technicians scheduled in it) | Activation: whether customers reach a working start, and the date from which early use and month-one support requests are counted. Depth: whether they use the product for the job they bought it for | Logins and clicks count activity, not value |
| **Cost to serve** (at Larkspur, starting with human hours per customer setup — effort, one part of the cost) | What it costs to set up and support one customer | It shrinks by moving work to suppliers unless every hour counts, whoever pays for it |
| **Support requests** per customer | Where customers struggle, especially in the first month after activation | Fewer requests can mean customers gave up asking |
| **Customer feedback scores** | How customers say they feel | A score without the reasons behind it tells you little about what to change |

![A road with four signposts, contract signed, setup, first real schedule and every technician scheduled, with time to first value bracketed from signing to first schedule, staff hours at setup, depth of use at the end, support requests below the road, and a warning card that logins count activity, not value.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/product-and-customer-outcomes.jpeg)

**Figure 4:** *Product outcomes follow the customer: how soon they get value, what setting them up costs, how fully they use the product and where they struggle. Clicks and logins are not on the path.*

{id: have-your-numbers-ready--delivery-and-execution}
### Delivery and Execution

This family answers whether the company does what it said it would, and it is usually the weakest, because it is nobody’s reporting duty.

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **Commitments against outcomes** | What was promised, what arrived, when, and the difference | Only honest if the commitment is recorded when it is made, not reconstructed later |
| **Allocation against plan** | How team time is actually split between new capabilities, improvements and maintenance | Most companies find on first measurement that it differs from the plan |
| **Software delivery measures** from DORA (DevOps Research and Assessment, a research programme on how software teams deliver), listed below the table | Whether the team can change the software quickly and safely | They cover only the part of delivery engineering controls, not the wait before work starts |
| **Predictability** | How often dated commitments land on their date | Easily gamed by committing only to safe dates |

DORA’s current guide has five delivery measures. Older sources quote the original four, without the last.

- **Change lead time:** how long a change takes from being saved in the code repository to running in the live service.
- **Deployment frequency:** how often the team deploys, that is, puts changes into the live service.
- **Change fail rate:** the share of deployments that fail and need immediate repair.
- **Failed deployment recovery time:** how long recovery from such a failed deployment takes. It does not cover every outage.
- **Deployment rework rate:** the share of deployments that are unplanned repairs after an incident.

Deploying puts a version into the live service; releasing makes it available to customers. A change can be deployed behind a switch that stays off, and released later by turning the switch on. The chapter [Assess Capability: Can the Team Deliver?](#can-the-team-deliver) covers what delivery measures can and cannot establish.

![Top: a ledger with columns promised and arrived, two rows flagged, recorded when promised. Bottom: a conveyor where five boxes wait before work starts and the rest pass through build, test, release, the only part the delivery measures see, before reaching customers.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/delivery-and-execution.jpeg)

**Figure 5:** *Delivery evidence has two parts: an honest record of what was promised against what arrived, and delivery measures read with the wait before work starts, which they do not cover.*

{id: have-your-numbers-ready--technology-health-and-cost}
### Technology Health and Cost

The engineering leader owns these outright, and here the absence of a number is most often mistaken for the absence of a problem.

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **Reliability** against an agreed objective, and **incidents** (failures that reach customers) with their impact | Whether customers can count on the service | Uptime, the share of time a service is available, says nothing about the failure that mattered |
| **Recovery tested** — the date and result of the last restore test | Whether the company can actually bring the service back | A backup that has never been restored is not evidence ([Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore)) |
| **Security findings** (known weaknesses) by severity and age | The protections in place and the obligations still open | A count without age hides the finding that has been open for a year |
| **Technology cost** per customer and as a share of revenue | Whether the cloud bill and software licence fees grow slower than the business | A total not split by product or customer cannot be weighed against the value they bring ([Critically Evaluate Cloud Costs: A Lower Bill Is Not Always Better](#cheaper-cloud-bill)) |
| **Technical debt register** | Where past shortcuts now slow specific future work | A general complaint about quality is not a register ([Manage Technical Debt: Fund the Fix by the Cost, the Risk and the Speed It Buys](#manage-technical-debt)) |
| **Key-person concentration** | Which systems only one person can release or recover | Invisible until that person is away; at Larkspur, diligence — the checks the investor made before investing — found that only one specialist could release the scheduling engine, the part of the software that builds the schedules, and recover it after a failure; releasing means making a new version available to customers |

![A service cabinet in the centre surrounded by six objects: a reliability gauge, a backup box stamped as restore tested, a shield of security findings by age, coins for cost per customer, a technical debt register, and one key on a single hook for the system only one person can release.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/technology-health-and-cost.jpeg)

**Figure 6:** *Technology health made visible: reliability against an agreed objective, a restore that has actually been tested, open findings and their age, cost per customer, the debt register, and the systems only one person can run.*

{id: have-your-numbers-ready--people}
### People

| Measure | What it tells you | Where it misleads |
| --- | --- | --- |
| **Headcount against plan** | Whether hiring is ahead or behind what the budget assumes | Headcount is a cost, not capacity (usable working time); new people take months to be fully effective |
| **Unwanted departures** | Whether the company is losing people it wanted to keep | A company-wide rate hides a team that lost half its engineers |
| **Open roles** and **time to hire** | Whether commitments that assume new people are realistic | An approved role is not a person doing the work |

Individual performance and pay stay internal; what an investor needs from this family is how people risks affect commitments.

![Twelve chairs in three teams under a dashed headcount-plan line: Team A full, Team B with two empty chairs tagged left, Team C with one open role and one new person still ramping up; a line notes that an approved role is not a person doing the work.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/people-measures.jpeg)

**Figure 7:** *People measures in one row: headcount against plan, departures that a company-wide rate would hide in one team, open roles, and new people who take months to reach full speed.*

{id: have-your-numbers-ready--pick-a-small-set}
## Pick a Small Set

Nobody should report all of that. Fifteen measures nobody disputes are worth more than ninety nobody trusts.

- **Start from decisions, not from the template.** Ask what the next consequential decision needs. At Larkspur, the next decisions are whether to fund the setup work and, later, whether it worked; the numbers that matter are setup effort, the wait to first schedule and the cost of the work. The investor’s template still gets filled in, but the company’s own set starts from its decisions.
- **Let the outcome record choose the product numbers.** The customer outcome, the business outcome and the measures between them ([Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking)) are the product and customer numbers worth having ready. The rest of the catalogue is context.
- **Add a measure only when a decision needs it.** A measure that has never changed a decision should be retired.

A reasonable shape for the investor conversation is a dozen or so numbers: a few from money and runway, a few from customers and growth, the outcome record’s pair and its leading measures, and a few from delivery and technology health, each chosen because someone decides something with it.

{id: have-your-numbers-ready--hold-each-number-ready}
## Hold Each Number Ready

A number is ready when anyone who doubts it can trace it back to its source in under ten minutes, and when everyone who quotes it means the same thing. Most reporting disputes are definition disputes in disguise. Someone reports retention at 94% and someone else at 88% — one counting customers kept, the other the revenue they represent, over different periods — and an hour that should have gone into deciding something disappears into reconciling the two.

For each measure in the set, record five things — plus, for a figure reported for a group, how the individual records are combined — and keep them with the measure rather than in a document nobody opens. Larkspur’s first entry is the one Morgan asked about:

| Field | Larkspur’s setup-effort measure |
| --- | --- |
| Definition | All human hours spent setting up one customer, end to end — Larkspur’s own staff, the contract implementation specialist and any bought-in data-entry help, whoever pays them — including all time spent checking and correcting the customer’s data |
| Source | The implementation team’s time records, reconstructed per customer |
| Owner | Priya, the product leader |
| Aggregation | The average per setup: total included hours for a group of setups divided by the number of setups in the group |
| Refresh | Per group of customers set up together (a cohort), reported at each quarterly review |
| Boundaries | Excludes automated checking by an outside service, which has no hours and is carried separately as a cost |

The **definition** settles arguments in advance: “whoever pays them” means the figure cannot be improved by moving manual work to a supplier. The **source** makes the figure credible. The **owner** is a person, not a team: someone answerable for the number being right and for saying so when it is not. The **refresh** stops the “how current is this?” exchange that precedes every stale decision. The **boundaries** say what the measure deliberately leaves out, which is where double-counting begins. [Tool 15](#toolkit--tool-15) gives the record as a template.

The **aggregation** rule means two people given the same records get the same figure. Take three setups of 65, 75 and 100 hours. They report as 80: 240 hours divided by three setups. They never report as the 240-hour total, or as the middle setup’s 75. The average, rather than the median, fits here because the question is how much effort setups consume in total.

Define a measure once and change it rarely. When a definition must change, restate the history on the new basis or say plainly that the series breaks. A changed definition presented as a changed result is indistinguishable from bad news being managed.

{id: have-your-numbers-ready--give-each-number-its-context}
### Give Each Number Its Context

“80 hours” says nothing until the reader knows what it is compared with, how many observations it rests on and what it is for. Four pieces of context turn a number into something a board can use:

- **Baseline**: what it was before, on the same definition. Larkspur’s 80 hours is, this week, the average of the five setups Morgan examined during diligence, three of which needed the specialist’s manual configuration. It is provisional. Days in this book count from day 0, the board meeting that adopts the operating plan shortly after the investment. The baseline the company will use is to be reconstructed by day 20 from the time records of all twelve setups of the previous two quarters, and the report says so.
- **Comparison**: what it was expected to be. The setup proposal aims at an average of 50 hours per setup.
- **Direction and confidence**: which way it is moving and how much weight it carries. Five observations are a starting point, not a trend.
- **Decision link**: what the figure is used to decide. The plan the board adopts sets the rule in advance for the average of the first group of eight pilot customers (a small trial of the changed setup). The average is measured at day 90 and goes to the board’s review at day 100. Under 60 hours supports a request for the next stage, which the board must still approve; 60 to 70 hours, including exactly 60 or 70, supports a smaller corrective step; over 70 reopens the plan ([Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days)).

**Thresholds agreed before the measurement** settle in advance which response each result points to, so the later review is about what to do, not about what counts as good. They guide the decision rather than make it: the board still weighs the evidence. Ines authorizes spending inside the approved plan. A new stage, a draw on the reserve (money the board set aside for needs the plan did not foresee) or any other spending outside the plan needs the board’s approval ([Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides)). The investor and the company disagree about the threshold in advance, which is the right time to disagree, before either side has a number to defend.

{id: have-your-numbers-ready--label-what-kind-of-number-it-is}
## Label What Kind of Number It Is

Priya’s setup proposal is a page of figures, and they look alike. They are not the same kind of thing.

![Five identical blank cards on a table, tagged actual, target, forecast, assumption and committed; only the actual card is anchored below the table. A line reads same typeface, different kinds.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/four-kinds-of-number.jpeg)

**Figure 8:** *The kinds of statement look identical on a page. The label is what separates a measured result from a target, a calculation about the future, an input taken as given, and a resource already authorized.*

| Kind | What it is | In Larkspur’s setup proposal |
| --- | --- | --- |
| **Actual** | Observed and recorded, on a stated definition | An average of about 80 staff hours per setup and a median wait of about ten weeks from signing to first real schedule; provisional until the day-20 baseline |
| **Target** | The result the plan sets out to reach, and by when — a desired outcome, not a promise | 50 hours per setup for the first pilot group, measured at day 90 |
| **Forecast** | A calculation about the future from stated inputs | €225,000 a year of staff time released: 100 setups a year × 30 fewer hours per setup = 3,000 hours a year, valued at €75 an hour |
| **Assumption** | An input taken as given, which may not hold | About 100 setups a year; €75 an hour, the fully loaded rate finance uses in plans (pay plus the employer’s other employment costs, per working hour); that the 50-hour target is reached and holds for later customers |
| **Committed** | A resource the board has authorized — an input, not a result | The contract implementation specialist, €150,000 for months 1 to 12, agreed before the plan and paid from the operating budget, the spending plan for running the business. The proposal’s own €180,000 and twelve engineer-weeks (twelve weeks of one engineer’s working time) become committed only when the board funds them ([Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything)) |

The forecast is still worth reporting, but written this way it cannot be mistaken for money the company has. It is 3,000 hours of projected capacity a year, at an assumed volume, valued at an assumed rate, on an assumed result. Each assumption carries weight: if volume and rate hold but setups reach only 65 hours, the saving is 15 hours per setup, 1,500 hours a year, and the forecast halves to €112,500.

**Capacity becomes cash only when a payment is actually avoided or additional customers pay in more than serving them costs**, on a date: a contract not extended, a planned hire whose salaries are never paid, or extra customers set up with the freed time whose payments exceed their costs. Deciding not to hire changes nothing in the bank that day; the benefit arrives month by month, as the salaries are not paid. Until then, finance keeps it out of any calculation of what the company can repay.

The labelling rule is one line, and it is the highest-value habit in this chapter: **every figure in a document that goes to a board or an investor carries its kind.** The cost is a few minutes of preparation. The benefit is that the company never has to explain, six months later, why a result it appeared to report did not arrive. When the first pilot group reports at day 90, the same labels will separate what was measured from what was projected ([Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue), [Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days)).

{id: have-your-numbers-ready--one-set-of-numbers-three-uses}
## One Set of Numbers, Three Uses

The same measures serve three purposes, at three levels of detail. Keeping them as one set, rather than three, is what stops the board, the leadership team and the teams from running on different facts.

{id: have-your-numbers-ready--in-the-investor-conversation}
### In the Investor Conversation

Not everything should go to an investor, and not everything an investor asks for is something it is entitled to receive.

- **Rights against courtesy.** An investor’s **information rights** — the reporting it is entitled to, usually set out in the investment agreement — are specific: typically periodic financial statements, a budget, the record of who owns which shares and sometimes board materials, on a stated schedule. Law and the company’s own governing documents can add entitlements, and a director the investor appointed receives board papers as a director. Beyond those, disclosure is a choice. Check the actual agreements rather than assuming either extreme, and involve qualified advisers where a request touches customer or employee data.
- **Aggregated, not raw.** The detail that makes a measure useful inside is rarely what makes it useful to a board. Aggregating means combining detailed records into totals or averages: the average for a cohort against baseline and threshold, not every customer’s hours; incident frequency and impact, not every timeline.
- **Share what supports decisions the recipient takes part in.** The board approves the plan, so it receives the evidence the plan rests on, with its assumptions visible. Investors do not run the engineering team, so they do not need its working detail.

![Dense working detail on the left passes through an open doorway and narrows into a single shared sheet on an easel on the right, tagged with its definition.](private-techuity/posts/16-have-your-numbers-ready/assets/images/16-have-your-numbers-ready/internal-and-shared.jpeg)

**Figure 9:** *The same evidence at two resolutions. What crosses the boundary to the investor is aggregated and carries its definition with it.*

{id: have-your-numbers-ready--in-goals}
### In Goals

Goals take the same numbers and put a date and a level on them.

- **Set goals on leading measures, report the lagging ones.** A team can move staff hours per setup this quarter; it cannot move renewals until the anniversaries. The outcome record sets which is which ([Adopt Outcome Thinking: Balance Customer and Business KPIs](#adopt-outcome-thinking)).
- **Pair a target with a counter-measure.** A measure that becomes a target changes behaviour, and not always the way intended. Setup hours can fall because customers are rushed into using a half-configured account; pairing the hours with month-one support requests shows it when it happens.
- **Keep the goal’s measure and the reported measure identical.** A team goal on a private definition of “setup time” produces a number the board cannot compare with anything.

{id: have-your-numbers-ready--in-dashboards}
### In Dashboards

A dashboard is the same set of numbers, refreshed automatically and shown at the level of detail its readers need. Three layers are usually enough:

| Layer | Readers and rhythm | What it shows |
| --- | --- | --- |
| **Board** | Directors and the investor, quarterly | The dozen numbers, each with its kind, baseline, comparison and the decision it informs; the record of commitments against outcomes |
| **Leadership** | The executive team, monthly or weekly | The same numbers with their drivers, by product and customer group; the allocation of team time against plan |
| **Team** | Each team, weekly or daily | The measures of the team’s own areas of work — its lanes — and the counter-measures beside them |

The test of the three layers is traceability: every figure on the board’s page should lead down to a leadership view and from there to the teams whose work moves it. A board number with nothing beneath it is a number nobody can act on; a team dashboard with nothing above it is work nobody can connect to the plan.

**Automate the refresh, not the interpretation.** A repeatable process keeps a figure current; a person still has to say what it means, and the owner named in the measure record is that person.

{id: have-your-numbers-ready--someone-has-to-do-this-work}
## Someone Has to Do This Work

Finance owns the accounts, not the definition of setup effort. Engineering owns the repositories and the incident records, not their translation into a board measure. Product owns the roadmap, not the record of what was committed four quarters ago. Left unassigned, the work happens in the fortnight before a board meeting.

**Product operations** is the discipline that has formed around this gap. In the account by Melissa Perri and Denise Tilles, it rests on three pillars, and they map closely onto the catalogue above. [S109: Perri and Tilles, *Product Operations*](https://melissaperri.com/book)

| Product operations pillar | What it does | The numbers it keeps ready |
| --- | --- | --- |
| **Business data and insights** | Gathers how the product and the company are performing from existing business systems, with standardized definitions so leaders can compare across products | Money and runway, customers and growth, cost to serve |
| **Customer and market insights** | Collects research from outside the company and passes it to the teams that need it | Product and customer outcomes, and the market assumptions behind forecasts |
| **Process and governance** | Keeps consistent practices for how product work is planned, committed and reviewed | Delivery and execution, especially commitments against outcomes |

**Standardized definitions are the mechanism, not a by-product**: two products can be compared only because both report on the same definition, and someone has to maintain it. And **product operations supplies evidence; it does not take the decisions**: the numbers exist so that the people with authority, established in [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides), can decide well.

A small company will not have a product operations team and does not need one to start. It needs the work assigned: a named owner per measure, as the record requires, and one person accountable for the board pack being consistent, current and honest as a whole. At Larkspur, Sam takes the board pack and the money family; Priya the product and customer numbers; Alex delivery and technology health. The function is what this becomes when doing it informally stops working.

{id: have-your-numbers-ready--build-it-in-the-order-that-pays}
## Build It in the Order That Pays

Nobody assembles all of this at once, and a company that tries produces a large document instead of ready numbers.

1. **Start with the decision in front of you** and the numbers it needs.
2. **Find where each number already lives**: time records, billing, the finance system, repositories, the cloud bill, incident records.
3. **Write the definition before the first number**: definition, source, owner, refresh, boundaries.
4. **Establish the baseline honestly**, from real records, and say how many observations it rests on and where it is weak.
5. **Agree thresholds in advance** with whoever will act on them — the step most often skipped, and the one that most reliably prevents a dispute.
6. **Label every figure** by its kind before it leaves the company.
7. **Automate the refresh** once the definition has survived a quarter, and build the dashboards on top.

{id: have-your-numbers-ready--what-ready-numbers-do-not-fix}
## What Ready Numbers Do Not Fix

An investor and a company can look at the same well-defined figures and still want different things, because they are exposed differently ([Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets)). Numbers do not settle a disagreement about risk appetite, time horizon or what the company is for.

A measure can be chosen because it flatters, a threshold set where it is easy to pass, a definition quietly revised in a bad quarter, and a comprehensive pack can bury a real problem in volume. More data makes several of these easier. The defences are the ones above — definitions that change rarely and visibly, thresholds agreed in advance, figures traceable to sources, a deliberately small set — plus a leader willing to report the number that is not flattering.

What ready numbers do is narrower and still valuable: they move disagreement from what is true to what to do, make a plan’s assumptions visible before they fail, and let a leader show the cost of a commitment rather than merely assert it.

{id: have-your-numbers-ready--what-to-say-when-the-investor-asks}
## What to Say When the Investor Asks

**“How long does it take to set up a customer, and how do you know?”** About 80 staff hours and about ten weeks to the first real schedule, both provisional, from a sample of five; the baseline from all twelve recent setups follows by day 20. Here is the definition, and Priya owns it.

**“What are your burn and runway?”** Sam’s figures, from the monthly accounts, on the stated definition — and the hiring plan that would change them, with its dates.

**“Why is this number different from last quarter’s?”** Either the business changed or the definition did. If the definition changed, the history is restated on the new basis, or the break is marked on the chart.

**“Can we have direct access to your systems?”** Ask what question the access would answer. Usually the answer is a measure that can be defined and provided properly, with more history and full definitions, on a regular schedule. A figure pulled without its definition creates exactly the disputes the definitions exist to prevent.

**“What is your €225,000 worth in cash?”** Nothing yet. It is a forecast of staff time, resting on three assumptions: about 100 setups a year, €75 an hour, and setups reaching 50 hours and staying there. It becomes cash only on the date a scheduled payment is actually avoided, or when additional customers pay more than serving them costs.

With the numbers ready and labelled, Larkspur can choose among its requests against the cash and team time the board approves. That is where [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything) begins.

{id: have-your-numbers-ready--questions-to-consider}
## Questions to Consider

1. *Take the three figures most often quoted in your investor conversations. For each, can you state the definition, the source, the owner and when it was last refreshed — without asking anyone?*
2. *Which families of the catalogue are missing from your board pack entirely? Which decision would one number from each of them inform?*
3. *Look at your last board pack. How many figures in it are actuals, and how many are forecasts or targets printed in the same typeface?*
4. *Can every figure on your board dashboard be traced to a team whose work moves it? Which cannot, and who would act on them?*
5. *What does your investor receive by right, and what do you provide by choice? Would your investor answer that question the same way?*

{id: have-your-numbers-ready--to-probe-further}
## To Probe Further

- **[Product Operations: How Successful Companies Build Better Products at Scale](https://melissaperri.com/book)** — Melissa Perri and Denise Tilles, 2023.  
  *The fullest treatment of the discipline that keeps these numbers ready: the three pillars, why standardized definitions are the mechanism, and how the function supplies evidence without taking over the decisions.*
- **[16 Startup Metrics](https://a16z.com/16-startup-metrics/)** — Jeff Jordan, Anu Hariharan, Frank Chen and Preethi Kasireddy, Andreessen Horowitz, 2015.  
  *Investors explaining the metrics founders most often confuse — bookings against revenue, recurring against total revenue, gross profit, customer acquisition cost, burn — which is a useful view of the money and growth families from the other side of the table.*
- **[DORA’s Software Delivery Performance Metrics](https://dora.dev/guides/dora-metrics/)** — DORA (DevOps Research and Assessment), Google Cloud.  
  *The current definitions of the five delivery measures in the catalogue — the original four plus deployment rework rate — grouped into throughput (how fast changes reach the live service) and instability (how often deployments fail or need unplanned repair).*
- **[Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/)** — Nicole Forsgren, Jez Humble and Gene Kim, IT Revolution, 2018.  
  *The research behind those delivery measures, including what they do and do not establish; useful before quoting them to a board. DevOps is the set of practices that joins building software with running it; Lean is the discipline of improving the flow of work and cutting waste.*
- **[How to Measure Anything: Finding the Value of Intangibles in Business](https://www.howtomeasureanything.com/)** — Douglas W. Hubbard, Wiley, 3rd edition, 2014.  
  *An argument that measurement exists to reduce uncertainty for a decision, not to achieve precision, and that this holds even for intangibles, things with no physical form such as customer satisfaction. It is the reason this chapter retires any measure with no decision attached.*
