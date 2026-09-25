{id: cheaper-cloud-bill}
# 31. Critically Evaluate Cloud Costs: A Lower Bill Is Not Always Better

![Critically Evaluate Cloud Costs: A Lower Bill Is Not Always Better — logo](private-techuity/posts/29-cheaper-cloud-bill/assets/images/29-cheaper-cloud-bill/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to put cloud bills on one comparable basis, separate why they changed, and decide how much to commit before calling a lower bill an improvement.

> **WHY INVESTORS CARE:** An investor, someone who puts money into the company hoping to get more back, sees the cloud bill as one large, visible expense. As the company handles more work, it expects the cost of each completed customer task to fall, and the plan the board approved turns that expectation into a number to test. It needs to know whether a lower bill means each task now costs less, or means customers are asking for less work, or means the company has cut the spare capacity that keeps the service running when something fails.

> **WHY YOU SHOULD CARE:** A lower bill can conceal falling demand, a higher cost per completed task, or a contract that obliges you to keep paying after the work shrinks. Reading the bill correctly is the difference between a saving and a hidden cost.

> **KEY POINTS:**
>
> * A smaller bill can have **several explanations**. Put the figures on one comparable basis, then separate changes in demand, usage, prices and software design before claiming an improvement.
> * Choose a **unit that reflects useful service**, and read it against the plan as well as the prior period. Cost per completed transaction or comparable customer can reveal more than total spending alone, and unit cost can improve while the approved spending plan is still missed.
> * **Commit only to the demand you can defend**. Test a promise to buy a fixed amount against a stated range of likely demand and against the period the company can already afford to pay for, and keep service quality as the final check on any saving.

**Cloud services** provide computing resources, storage and related services rented from a supplier. A company’s cloud bill falls by 20%. Has its operation improved?

Perhaps unused resources were removed. Perhaps traffic fell because customers left. Perhaps spending moved into another account. Perhaps the company promised to buy a large amount in advance, which lowered this month’s supplier bill while leaving it owing money for years. The number is a starting observation, not a conclusion. The reverse also holds: a bill can rise while each completed customer task becomes cheaper, and fall while the service becomes worse.

The chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design) compares three views of one proposal: its effect on **profit** (what is left after the costs being counted are taken off the money earned), its effect on cash and its effect on the software design. Here we apply that approach to cloud spending. First choose a meaningful unit of service and a comparable way of counting cost, then separate the reasons costs change, then decide how much to commit, and finally check the saving alongside service quality.

**Unit economics** means examining money earned or spent for one meaningful unit of activity, such as a completed transaction or a customer account. **FinOps** is the practice of managing technology’s financial value through collaboration among engineering, finance and business teams. The name joins *Finance* with *DevOps*, the practice of having the people who build software and the people who run it work as one team. The FinOps Foundation’s unit-economics guidance connects technology costs to organizational outcomes and distinguishes efficient use of computing resources from measures of business results. [FinOps Foundation: unit economics](https://www.finops.org/framework/capabilities/unit-economics/) For a company leader, it bridges infrastructure work and the questions about cash and about **margin** (the money left from a sale after the costs being counted) discussed in the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget).

{id: cheaper-cloud-bill--setting-up-the-example-why-larkspurs-cloud-bill-rose-20}
## Setting Up the Example: Why Larkspur’s Cloud Bill Rose 20%

Larkspur is the fictional scheduling-software company this book follows. Its **board**, the small group of directors who oversee the company on the owners’ behalf, has approved an **operating plan** for 2026, a statement of the activity and spending expected for that year. That plan assumes cloud spending stays roughly flat against 2025 while the number of customer transactions grows by half. Morgan, the technology adviser working for Larkspur’s investor, has asked why last quarter’s bill rose 20%.

The question is legitimate. It is also incomplete, because a rising bill can still mean cheaper service per task. Alex, the technology leader, has to show what the bill means for the service customers receive, and whether a saving that looks good at the next board meeting would still look good a year later.

Two separate questions sit inside Morgan’s one: did the cost of a unit of useful work improve, and was the plan the board approved met? Answering either starts with the unit.

{id: cheaper-cloud-bill--choose-a-unit-that-explains-the-business}
## Choose a Unit That Explains the Business

Cost per **virtual machine**, a software-defined computer running on shared hardware, can help an infrastructure team. Cost per completed **customer transaction** — one piece of work a customer asked for and received, which for Larkspur means one appointment successfully scheduled — may help management understand what serving a customer actually costs. Cost per active account may help a subscription product, provided accounts use similar amounts of computing. No single unit works for every product.

In 2025 the company spent €100,000 a month to process one million successful transactions: €0.10 each. The board’s plan for 2026 kept spending flat at €100,000 while volume grew by half, to 1.5 million transactions: about €0.067 each. Last quarter’s monthly figures — the three months just closed, in 2026 — show the volume arriving on plan, but spending at €120,000: €0.08 each. All three rows are monthly figures on the same basis, cost assigned to the period (defined in the next section), so the comparison is like for like.

| | Monthly spending | Successful transactions | Cost per transaction |
| --- | ---: | ---: | ---: |
| Actual, 2025 | €100,000 | 1,000,000 | €0.100 |
| Board plan, 2026 | €100,000 | 1,500,000 | €0.067 |
| Actual, last quarter of 2026 | €120,000 | 1,500,000 | €0.080 |

Against 2025, the total bill rose 20% while unit cost fell 20%: the service became cheaper per unit of useful work. Against the 2026 plan, spending is €20,000 a month above the flat €100,000 the plan allowed, and unit cost is 20% above the €0.067 the plan implied. **Improvement and plan are separate measures**; reporting only the first would present a missed plan as a success. Whether the result is desirable also depends on the revenue each transaction earns, on service quality, on which kinds of customer the growth came from, and on what the company had to spend to support that growth.

The two measures can also part company in the other direction. Suppose the bill had instead fallen to €90,000 because volume reached only 1.2 million transactions: €0.075 each. Unit cost improved 25% against 2025 and the bill came in €10,000 under the 2026 plan, yet transaction volume was 20% below plan — the company grew volume by 20% where the plan assumed 50%. The lower bill is not an achievement; it is the shadow of the missing demand. And if volume fell to 500,000 with an €80,000 bill, unit cost would rise to €0.16, 60% worse than last year and about 2.4 times the planned figure. A cost-saving headline would hide a deterioration in the business’s ability to spread its costs.

These simple examples show why a cost target should be attached to a service and demand assumption, and why it should be read against both the prior period and the plan. They don’t establish that all infrastructure costs vary in proportion to usage.

A related trap is comparing the company with the investor’s other companies — its **portfolio**. Cloud cost as a percentage of **revenue**, the money earned from sales before costs are taken off, mixes together several different things: how efficiently the technology runs, what the company charges, how much of each sale is left after costs, how the product is delivered, and how far along the company is. Such a comparison can identify a question worth investigating, but it does not answer it. A **cohort**, a group selected for comparison, needs to match how the businesses earn money, their size, the computing work their systems perform, and which services are counted in the figure. Even then, a handful of companies is too few to draw a reliable conclusion from. A company may spend more because its product performs more valuable work, or because it is inefficient.

{id: cheaper-cloud-bill--put-every-figure-on-the-same-basis}
## Put Every Figure on the Same Basis

Comparing this month’s **invoice** — the supplier’s bill — with last month’s only works if both numbers mean the same thing. A monthly bill, a payment made in advance, and a bill reduced by supplier **credits** are three different measurements: they mix *when money leaves the account* with *which period the cost belongs to*. Before comparing, state which of four figures each number is:

| Basis | What it measures | Typical distortion |
| --- | --- | --- |
| **Cash paid** in the period | Money that left the company’s account | Paying a year in advance makes one month look expensive and the following months look cheap |
| **Cost assigned to the period** | The period’s share of the resources consumed, with any advance payment spread across the months it covers | The comparable basis for unit costs and trends |
| **Credits** | Temporary reductions in what the supplier or a partner charges, which cut the cash paid without cutting the resources used | A bill reduced by credits understates the cost that continues after they end |
| **Commitment usage** | How much of a prepaid or minimum commitment the period’s demand actually used | Unused commitment is a cost with no matching service |

The examples in this chapter use cost assigned to the period unless stated otherwise. When finance and engineering disagree about whether a saving happened, the disagreement is often about the basis, not the facts: engineering is looking at resources consumed while finance is looking at cash paid. Agree the basis first.

{id: cheaper-cloud-bill--separate-usage-rates-and-architecture}
## Separate Usage, Rates and Architecture

A cheaper bill can come from using fewer computing resources for the same work, from paying a different price per resource, or from changing the **architecture** — how the software is designed to do the work.

Removing unused resources can yield fairly direct savings. **Rightsizing** means renting only the computing capacity the product actually needs, including at its busiest moments; it needs evidence about those peaks and about what the service has promised customers. Agreeing a lower price in exchange for a purchase promise can be valuable when demand is predictable, but the freedom to stop buying has a value too. Redesigning the software can improve efficiency while adding the cost of moving systems, new reliability risks and ongoing maintenance.

**Do not count the same saving twice**. If rightsizing reduces the volume eligible for a discounted commitment, the two headline opportunities aren’t necessarily additive. A model should apply changes in a stated order and calculate the combined result.

![A cloud bill connects to three dials. Demand — how much work customers ask for, shown as completed appointments. Price agreed with the supplier for each unit of computing. Resource use, showing computing that does useful work beside computing left unused. A counter below records the appointments completed.](private-techuity/posts/29-cheaper-cloud-bill/assets/images/29-cheaper-cloud-bill/three-drivers-of-cloud-cost.jpeg)

**Figure 1:** *Three dials move the bill. **Demand** is how much work customers ask for — for Larkspur, appointments to be scheduled. **Price** is what the supplier charges for each unit of computing. **Resource use** is how much computing that work actually consumes, which depends on the software design as well as on demand: the same 1,250 appointments cost more if the software leaves capacity idle. Separate the three before deciding whether the service became more efficient.*

{id: cheaper-cloud-bill--a-multi-year-commitment-changes-future-spending}
## A Multi-Year Commitment Changes Future Spending

Larkspur’s scheduling service is the largest part of the €120,000 monthly bill. At **flexible prices** — paying only for what is used, month by month, with no minimum — it needs €50,000 of resources each month. The provider offers a 30% price reduction in return for a **commitment**: a promise to pay a fixed amount every month for three years, whether or not the company uses that much. The 30% and the fixed amounts used in this chapter are assumptions for the example, not a supplier’s published prices; the conclusions below hold for these quoted terms and the stated range of demand, not for every contract. The right comparison includes plausible demand paths, alternative designs, any plan to buy another company, and the possibility of selling or separating part of the business.

Assume a fixed €35,000 a month replaces the €50,000 flexible bill. At unchanged demand, the saving is €15,000 a month. If demand falls so that flexible prices would cost only €20,000, the same commitment costs €15,000 more a month, assuming it can’t be reduced or used elsewhere. The €35,000 is the cost assigned to each month; whether the company pays it monthly or in advance changes when cash leaves the account, not this comparison.

A discount on unused capacity is still an expense. A contract that makes switching expensive can be reasonable, but the loss of flexibility should be visible when it’s approved.

![Two bar comparisons on one scale. At stable demand, flexible spending is €50,000 a month against €35,000 for the committed contract. At lower demand, flexible spending is €20,000 against the same €35,000 commitment.](private-techuity/posts/29-cheaper-cloud-bill/assets/images/29-cheaper-cloud-bill/fixed-commitment-changing-demand.jpeg)

**Figure 2:** *The same €35,000 commitment saves €15,000 a month against €50,000 of flexible spending and costs €15,000 more against €20,000. Test the commitment against lower demand as well as the forecast that makes it attractive.*

{id: cheaper-cloud-bill--the-decision-larkspur-makes}
### The Decision Larkspur Makes

To decide, Larkspur states a demand range and a funding condition.

**Demand range.** Throughout this decision, demand is measured as what the scheduling service’s usage *would* cost at flexible prices, so every option is compared against the same yardstick. Eighteen months of usage show that figure has never fallen below €30,000 a month. For the twelve months from 1 January to 31 December 2027, the board has approved a **demand forecast** — its view of how much work customers will ask for — putting that figure between €30,000 (new customers stop arriving and the largest one leaves) and €60,000 (the forecast growth arrives). The €20,000 case lies below that range; it is kept as a **stress case**: a deliberately harsh scenario used to test a decision, not a forecast.

**Funding condition.** Alongside that forecast, the board has approved the **cash provision** for 2027: the money set aside to meet the supplier payments the forecast implies. Larkspur has cash in the bank plus customer receipts it expects on deliberately cautious assumptions, and together these cover the €21,000 a month Option C would commit to (€252,000 over the year), the flexible usage on top of it across the forecast range, and the reserve Sam sets aside for the final usage bill that arrives in January 2028. That is what pays the commitment: money the company already holds or can reasonably expect from customers it already serves, not money a new investor might provide.

Three approvals therefore exist for 2027 — a demand forecast, the cash to meet it, and the chief executive’s standing permission to sign contracts of a year or less. One does not: the board has not yet set a **2027 spending target**, the equivalent of the flat €100,000 a month it set for 2026. That target is agreed in the autumn planning round, after this contract must be signed. So the commitment rests on approved purchasing authority and approved cash, not on an approved annual ceiling — a distinction the ending returns to.

Beyond 31 December 2027, even that much is absent. The board has approved no forecast, no cash provision and no plan of any kind for 2028, and no investor or lender has promised further money. A three-year commitment would therefore oblige Larkspur to pay for two more years that nobody has yet shown it can fund — and would run past any change of ownership in that time.

Three options are compared on the same basis:

| Option | Cost at €30,000 demand | Cost at €50,000 demand | Cost at €60,000 demand | Cost at €20,000 stress case |
| --- | ---: | ---: | ---: | ---: |
| A. Stay flexible | €30,000 | €50,000 | €60,000 | €20,000 |
| B. Three-year commitment covering €50,000 of demand (€35,000 fixed) | €35,000 | €35,000 | €45,000 | €35,000 |
| C. One-year commitment covering €30,000 of demand (€21,000 fixed), remainder flexible | €21,000 | €41,000 | €51,000 | €21,000 |

Option B saves €15,000 a month at or above forecast demand but costs €5,000 more at the low end of the range and €15,000 more in the stress case. Option C saves €9,000 a month at every point in the stated range, costs €1,000 more in the stress case, and ends when the funded year ends.

**Larkspur chooses Option C.** Alex, the technology leader, proposes it, using eighteen months of usage history and the plan’s demand range as evidence. Sam, the finance leader, checks that the company can pay for it and reads the contract terms, set out below. Ines, the chief executive, approves it: the board has given her standing permission to sign supplier contracts that run for a year or less without returning to them, and Option C fits inside that permission.

**What the contract actually says.** In this fictional example, the agreement is signed by Larkspur Software B.V. — *besloten vennootschap*, the Dutch private limited company form, which makes it a company in its own right, responsible for its own debts. It is the operating company itself that signs, not its owner.

Larkspur pays the €21,000 minimum **in advance**, on the first of each month from 1 January to 31 December 2027 — €252,000 in total, owed whether or not the service is used. Usage above what that €21,000 buys is **settled in arrears**, meaning paid after the service has been used rather than before: the provider measures each month’s extra usage, issues the bill on the first working day of the following month, and payment falls due 30 days after that bill. January’s extra usage is therefore billed in early February and paid in early March.

The bill for a month’s extra usage arrives the month after; the money leaves the account the month after that. February 2027 is the first bill that shows a full month under the new arrangement — January’s €21,000 was paid on 1 January, and January’s extra usage appears in the February bill.

The contract cannot be cancelled early: leaving in month three still leaves the remaining months payable in full. It cannot be transferred to another company without the provider’s written consent, which the provider is not obliged to give. And it expires on 31 December 2027 in the sense that no further minimum payment falls due and any renewal is a fresh negotiation, not an automatic extension.

Expiry does not wipe out charges already incurred, though. December 2027’s extra usage is billed in January 2028 and paid in February 2028 — two months after the contract ends. Sam therefore reserves that final settlement inside the 2027 cash provision rather than treating 31 December as the last payment date, and confirms all of this before Ines signs.

**Why the other two are rejected.** Option B’s extra €6,000 a month of saving exists only at €50,000 of demand or above, and turns into a €14,000 a month disadvantage at the low end of the range. That extra saving is bought by owing money for two years beyond the period anyone has approved a plan for. Option A — simply staying flexible — is rejected because a €9,000 monthly saving with no downside inside the stated range is real money.

**What a later review can and cannot change.** Four events reopen the decision: flexible-price usage falling below €30,000 a month for two consecutive months, rightsizing work that cuts the volume the commitment applies to, a proposal to sell the company or separate part of it, or the provider offering transfer rights.

If demand collapses in March, Larkspur still owes the remaining monthly payments; it cannot cancel, and it cannot hand the contract to someone else unless the provider agrees. If the company changes hands, the buyer inherits an operating company that is still liable for those payments.

What management can actually do is bounded to four moves: stop adding flexible usage on top of the commitment, look for other computing work to run inside the €21,000 it is already paying for, ask the provider — who has no obligation to say yes — for a transfer or a restructure, and decline to renew on 31 December 2027. That last option is precisely why the obligation was kept to one year in the first place.

A company with stable demand and funding already secured for several years might reasonably accept Option B after the same comparison. The rule is not “commit less”; it is that the commitment follows from a stated demand range and a period the company can pay for, and that the person approving it can see the case where it costs more.

Product and engineering leaders should involve **procurement**, the people responsible for buying and negotiating supplier services, and finance early. Engineering understands usage and whether moving systems to another arrangement is feasible. Finance understands payment timing and accounting. Procurement and legal specialists interpret contract terms. None of those views is sufficient by itself.

{id: cheaper-cloud-bill--credits-minimum-spend-and-ownership-change-conditions}
## Credits, Minimum Spend and Ownership-Change Conditions

Contract terms that change the invoice without changing the resources consumed belong together, because they distort the same comparison.

**Temporary credits.** **Credits** are temporary reductions the supplier or a partner applies to the bill — not borrowed money, and not a sign that the service became cheaper to run. In a separate fictional Larkspur scenario, credits reduce a €30,000 monthly service bill to €5,000 for six months. The underlying service still consumes €30,000 of resources at the stated prices. A plan that extends beyond the six months has to show how the company will pay the full €30,000 once the credits stop. And before calling the service **profitable** — earning more than it costs — compare the revenue and costs of serving a customer both with and without the credits.

**Minimum spend and who signs.** An investor may introduce a provider, or a **corporate parent** — a company that owns this one — may offer a discount negotiated for all the companies it owns. Ask which company legally signs and therefore owes the payments, whether a **minimum spend** applies (an amount payable whether or not it is used), and who benefits from the lower price, and who pays for capacity nobody uses. The help can be useful while also creating an obligation the company must carry after the relationship changes.

**Ownership change.** A **carve-out** is the separation or sale of part of a business as a standalone company. A commitment that cannot move with the business in a carve-out becomes a **stranded cost**: one the company still owes but no longer benefits from. Check, before signing rather than in the middle of a sale, what the contract says about renewal, about a change of owner, and about moving the product to another provider. After one company buys another, applying the buying group’s discount to the acquired company’s bill and calling the result a **synergy** — a benefit expected from combining two businesses, such as a lower price — skips the cost of moving that company onto the group’s shared technical platform; the chapter [Plan Acquisitions and Separations: Account for Extra Work, Not Just Expected Value](#acquisition-adds-work-first) treats that comparison.

None of these terms is a problem in itself. The test is whether the company can see the continuing cost behind the invoice, and whether the service is still the one the customer bought.

{id: cheaper-cloud-bill--protect-the-service-the-customer-bought}
## Protect the Service the Customer Bought

The easiest way to reduce some costs is to reduce the service. Whether that’s acceptable is a product decision. Less **redundancy** — fewer spare components or alternative ways to keep operating when something fails — longer allowed times to finish processing, or help available over fewer hours, can change the customer’s experience and the company’s risk.

Define service conditions alongside the cost target. Track successful work completed; **latency**, the time a user waits for a response, where it matters; the share of requests that fail; how quickly service is restored after a failure; and customer complaints. The exact measures should follow what the product promised. Larkspur, for instance, promises that an appointment is confirmed within two seconds and that the service is available 99.9% of the month. A low-cost service that can’t complete a customer’s essential workflow has poor economics even if the infrastructure dashboard looks efficient.

{id: cheaper-cloud-bill--prove-the-saving-actually-arrived}
## Prove the Saving Actually Arrived

Before a cost initiative starts, define the **baseline**: the starting costs and demand used for comparison. Estimate what spending would have been without the initiative, and state which costs are included. Then keep three things separate as the work proceeds:

- **Opportunity:** a model of what might be saved.
- **Change implemented:** resources or contracts actually changed.
- **Observed net effect:** the spending actually seen, or the spending actually avoided, after the costs of making the change and any shift in demand have been explained and put on the agreed cost basis.

A **run-rate projection**, such as “€9,000 a month, so €108,000 a year,” is a separate, labelled estimate. It assumes the observed month repeats; state that assumption and what would break it.

A capacity reduction may avoid a forecast increase rather than reduce this month’s bill. That can be valuable, but the forecast and its uncertainty should stay visible. Similarly, reducing internal support effort doesn’t automatically reduce **payroll**, the money actually paid to employees. The hours freed are real, but a cash saving needs the amount actually paid for staffing to fall — fewer paid overtime hours, a smaller contractor bill, or a departure that is not backfilled. Cancelling a planned hire is different again: it prevents a future increase rather than reducing the bill the company pays today.

An initiative record should include the staff time spent making the change, fees paid to outside experts, tooling, the cost of running the old and new services side by side during the switch, and ongoing maintenance. A **payback calculation** — working out how long the accumulated savings take to repay what the change cost — must include **the work required to capture savings**. Comparable services and people who have faced the same decision, including through an investor’s network, are covered in the chapter [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability).

A useful cost improvement has an explanation the company can check: what changed, on what basis it was measured, how demand affected the comparison, what the change cost to make, and whether service remained acceptable.

Larkspur’s answer to Morgan’s question is not “the bill went up 20%” or “we found €15,000 a month.” It has two parts, and they belong to different time frames.

**What already happened.** Unit cost per successful transaction fell 20% against 2025, so the service became more efficient. The 2026 flat-spend plan was still missed: last quarter’s spending ran €20,000 a month above the €100,000 that plan allowed, and unit cost was 20% above what it implied. Nothing signed now changes it, and the money is already spent.

**What is expected to happen next.** From 1 January 2027, the one-year commitment on the scheduling service is expected to reduce future monthly spending by €9,000 at every point in the approved demand range, and to cost €1,000 more a month if demand falls to the €20,000 stress case. That is a projection, not yet an observation: nobody has seen a post-change bill. The first one covering a full month under the new arrangement arrives in early February 2027, and until then the €9,000 belongs in the “opportunity” column above, not the “observed net effect” one.

The two do not cancel out, and the €9,000 is a smaller claim than it first looks. It is a constant saving *against buying the same usage flexibly* — €9,000 a month at every demand level in the range. Total cloud spending still moves with demand: holding the roughly €70,000 a month outside the scheduling service steady, Larkspur spends about €91,000 a month if scheduling demand sits at the bottom of the range, €111,000 at €50,000 of demand, and €121,000 at the top.

Take the €50,000 case — roughly where last quarter ran — and compare it with the €100,000 the 2026 plan allowed: about €111,000 against €100,000 leaves €11,000 a month unexplained. That is an illustrative figure, not a fixed one. It assumes scheduling demand of €50,000, the other €70,000 holding steady, and the €100,000 benchmark.

The board approved a 2027 demand forecast and the cash to meet it, which is what let Ines sign; it has not yet set a 2027 spending target. So €100,000 is the 2026 expectation being carried forward for want of a 2027 one. Alex owes the board two things at the autumn planning round: an account of what drives that €11,000, and a 2027 target to be measured against — either further changes that bring spending back to €100,000, or a case for a higher one. That is a contract choice set beside an honest comparison with the plan, not a savings announcement.

The commitment was tested against demand the company can observe, and the chapter [Build And Test Resilience: Backups Are Not Enough](#prove-you-can-restore) judged spending whose benefit is harder to observe, protection against a failure. The next chapter applies this chapter’s method, a unit of useful work, one comparable basis, the reasons a bill changed and a commitment sized to a demand range, to the newest metered bill a company runs: [Critically Evaluate AI Costs: Measure the Return per Task and per Period](#ai-worth-its-cost).

{id: cheaper-cloud-bill--questions-to-consider}
## Questions to Consider

1. *What unit of useful service does your cost per unit describe, are the figures you compare over time on the same cost basis, and do you read them against the plan you were funded for as well as the prior period?*
2. *When your infrastructure bill last changed, how much came from usage, rates, architecture or demand? Were any savings counted twice?*
3. *Which of your commitments would become a stranded cost if demand fell below the range you planned for, the product moved to another provider, or the company were separated from its owner?*

{id: cheaper-cloud-bill--to-probe-further}
## To Probe Further

- **[Cloud FinOps, 2nd edition](https://www.finops.org/community/finops-book/)** — J.R. Storment and Mike Fuller, O'Reilly, 2023.  
  *The book behind the FinOps practice this chapter cites, whose chapters on usage, rate and commitment optimization show how to avoid counting the same saving twice.*
- **[Cost Optimization Pillar, AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)** — Amazon Web Services, 2024.  
  *The supplier's own account of good practice, useful for the vocabulary your procurement discussion will use, though it treats staying on the platform as given.*
- **[Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)** — chapter 4 of *Site Reliability Engineering*, Google, O'Reilly, 2016.  
  *Explains how to state the service conditions this chapter says must sit beside any cost target, so you can define the service the customer bought before someone cuts it.*
- **[The Cost of Cloud, a Trillion Dollar Paradox](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)** — Sarah Wang and Martin Casado, Andreessen Horowitz, 2021.  
  *A disputed argument from a firm that invests in growing companies, showing exactly how an investor may connect your cloud bill to the money left after costs and to the value placed on the whole business.*
- **[Why we're leaving the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)** — David Heinemeier Hansson, 37signals, 2022.  
  *One company's decision to leave the cloud with real bill figures and a clear statement of when cloud still makes sense, read as a case rather than a rule.*
