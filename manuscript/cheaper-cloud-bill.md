{id: cheaper-cloud-bill}
# 16. Why a Cheaper Cloud Bill Can Be Bad News

![Why a Cheaper Cloud Bill Can Be Bad News — logo](private-techuity/posts/10-cheaper-cloud-bill/assets/images/10-cheaper-cloud-bill/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to put cloud bills on one comparable basis, separate why they changed, and decide how much to commit before calling a lower bill an improvement.

> **WHY INVESTORS CARE:** Cloud spend is a visible cost line that investors expect to fall at unit level with scale, and the approved plan turns that expectation into a number to test; they need to know whether a lower bill is a better service unit or a sign that demand, or resilience, has fallen.

> **WHY YOU SHOULD CARE:** A lower bill can conceal falling demand, a worse service unit or a commitment that stops the company shrinking later; reading the bill correctly is the difference between a saving and a hidden cost.

> **KEY POINTS:**
>
> * A smaller bill can have **several explanations**. Put the figures on one comparable basis, then separate changes in demand, usage, prices and architecture before claiming an improvement.
> * Choose a **unit that reflects useful service**, and read it against the plan as well as the prior period. Cost per completed transaction or comparable customer can reveal more than total spending alone, and unit cost can improve while the approved spending plan is still missed.
> * **Commit only to the demand you can defend**. Test a purchase commitment against a stated demand range and the company’s funded horizon, and keep service quality as the final check on any saving.

**Cloud services** provide computing resources, storage and related services rented from a supplier. A company’s cloud bill falls by 20%. Has its operation improved?

Perhaps unused resources were removed. Perhaps traffic fell because customers left. Perhaps spending moved into another account. Perhaps a large upfront commitment lowered the monthly invoice while increasing long-term exposure. The number is a starting observation, not a conclusion.

In the fictional Larkspur scenario used in this chapter, the operating plan the board approved assumes cloud spending stays roughly flat while transaction volume grows by half. Morgan, the investor’s technology adviser, has asked why last quarter’s bill rose 20%. The question is legitimate. It is also incomplete: a bill can rise while the service becomes cheaper per unit of useful work, and fall while the service becomes worse. Alex, the technology leader, has to show what the bill means for the service customers receive, and whether a saving that looks good at the next board review would still look good a year later. Two separate questions sit inside Morgan’s one: did the cost of a unit of useful work improve, and was the plan the board approved met? This chapter keeps them apart, because the answers can differ.

The previous chapter compared the earnings, cash and design views of one proposal. Here we apply that approach to cloud spending: first choose a meaningful unit of service and a comparable cost basis, then separate the reasons costs change, then decide how much to commit, and finally check the saving alongside service quality.

**Unit economics** means examining revenue or cost for a meaningful unit of activity, such as a completed transaction or customer account. FinOps is the practice of managing technology’s financial value through collaboration among engineering, finance and business teams. The FinOps Foundation’s unit-economics guidance connects technology costs to organizational outcomes and distinguishes resource efficiency from business unit measures. [S16: FinOps unit economics](https://www.finops.org/framework/capabilities/unit-economics/) For a company leader, it bridges infrastructure work and the cash and margin questions discussed in [Find the Cash Behind Your Technology Budget](#obligations-before-budget).

{id: cheaper-cloud-bill--choose-a-unit-that-explains-the-business}
## Choose a Unit That Explains the Business

Cost per **virtual machine**, a software-defined computer running on shared hardware, can help an infrastructure team. Cost per completed customer transaction may help management understand delivery economics. Cost per active account may help a subscription product, provided accounts have comparable usage. No single unit works for every product.

Larkspur’s figures make the distinction concrete. Last year the company spent €100,000 a month to process one million successful transactions: €0.10 each. The board’s plan for this year kept spending flat at €100,000 while volume grew by half, to 1.5 million transactions: about €0.067 each. Last quarter’s monthly figures show the volume arriving on plan, but spending at €120,000: €0.08 each. All three rows are monthly figures on the same basis, cost assigned to the period (defined in the next section), so the comparison is like for like.

| | Monthly spending | Successful transactions | Cost per transaction |
| --- | ---: | ---: | ---: |
| Prior year | €100,000 | 1,000,000 | €0.100 |
| Board plan | €100,000 | 1,500,000 | €0.067 |
| Actual, last quarter | €120,000 | 1,500,000 | €0.080 |

Both questions now have an answer, and the answers differ. Against the prior period, the total bill rose 20% while unit cost fell 20%: the service became cheaper per unit of useful work. Against the plan, spending is €20,000 a month above the flat envelope, and unit cost is 20% above the €0.067 the plan implied. **Improvement and plan are separate measures**; reporting only the first would present a missed plan as a success. Whether the result is desirable also depends on revenue per transaction, quality, customer mix and the investment needed to support the growth.

The two measures can also part company in the other direction. Suppose the bill had instead fallen to €90,000 because volume reached only 1.2 million transactions: €0.075 each. Unit cost improved 25% against the prior year and the bill came in €10,000 under the plan, yet the planned growth was missed by a fifth. The lower bill is not an achievement; it is the shadow of the missing demand. And if volume fell to 500,000 with an €80,000 bill, unit cost would rise to €0.16, 60% worse than last year and about 2.4 times the planned figure. A cost-saving headline would hide a deterioration in the business’s ability to spread its costs.

These simple examples show why a cost target should be attached to a service and demand assumption, and why it should be read against both the prior period and the plan. They don’t establish that all infrastructure costs vary in proportion to usage.

A related trap is the portfolio comparison. Cloud cost as a percentage of revenue mixes technical efficiency, pricing, product margin, service model and company maturity; it can identify a question worth investigating but does not answer it by itself. A **cohort**, a group selected for comparison, needs to match business model, scale, workload and the services included, and even then a small portfolio offers limited statistical confidence. A company may spend more because its product performs more valuable work or because it is inefficient. Diagnosis must distinguish the two.

{id: cheaper-cloud-bill--put-every-figure-on-the-same-basis}
## Put Every Figure on the Same Basis

Comparing this month’s invoice with last month’s only works if both numbers mean the same thing. A monthly bill, an upfront commitment and a credit-reduced invoice mix cash timing with cost allocation. Before comparing, state which of four figures each number is:

| Basis | What it measures | Typical distortion |
| --- | --- | --- |
| **Cash paid** in the period | Money that left the company’s account | An upfront commitment makes one month look expensive and the following months look cheap |
| **Cost assigned to the period** | The period’s share of the resources consumed, with any upfront payment spread across the months it covers | The comparable basis for unit costs and trends |
| **Credits** | Supplier or partner subsidies that reduce cash paid without reducing resources consumed | A subsidized invoice understates the continuing cost |
| **Commitment usage** | How much of a prepaid or minimum commitment the period’s demand actually used | Unused commitment is a cost with no matching service |

The examples in this chapter use cost assigned to the period unless stated otherwise. When finance and engineering disagree about whether a saving happened, the disagreement is often about the basis, not the facts: engineering is looking at resources consumed while finance is looking at cash paid. Agree the basis first.

{id: cheaper-cloud-bill--separate-usage-rates-and-architecture}
## Separate Usage, Rates and Architecture

Infrastructure improvement can come from using fewer resources for the same work, paying a different rate, or changing how the product does the work. These mechanisms carry different risks.

Removing unused resources can yield fairly direct savings. **Rightsizing**, matching provisioned capacity to actual demand, needs evidence about peaks and service requirements. Rate commitments can be valuable when demand is predictable, but flexibility has an economic value too. Architectural change can improve efficiency while introducing migration, reliability and maintenance costs.

**Do not count the same saving twice**. If rightsizing reduces the volume eligible for a discounted commitment, the two headline opportunities aren’t necessarily additive. A model should apply changes in a stated order and calculate the combined result.

![Demand, unit prices and resource usage can each change the cloud bill.](private-techuity/posts/10-cheaper-cloud-bill/assets/images/10-cheaper-cloud-bill/three-drivers-of-cloud-cost.jpeg)

**Figure 1:** *Separate why the bill changed before deciding whether the service became more efficient.*

{id: cheaper-cloud-bill--a-multi-year-commitment-changes-future-spending}
## A Multi-Year Commitment Changes Future Spending

Larkspur’s scheduling service, the largest component of the €120,000 monthly bill, needs €50,000 of resources each month at flexible rates. The provider offers a 30% discount for a fixed monthly commitment over three years. The discount and the commitment floors used in this chapter are assumptions for the example, not a supplier’s published tariff; the conclusions below hold for these quoted terms and the stated range of demand, not for every contract. A commitment promises a lower rate but obliges the company to pay for capacity over a fixed period. The right comparison includes plausible demand paths, alternative architectures, acquisition plans, and the possibility of selling or separating the business.

Assume a fixed monthly commitment of €35,000 replaces the €50,000 flexible bill. At unchanged demand, the saving is €15,000 a month. If demand falls so that flexible spending would be €20,000, the same commitment costs €15,000 more a month, assuming it can’t be reduced or used elsewhere. The €35,000 is the cost assigned to each month; whether the company pays it monthly or in advance changes cash timing, not this comparison.

A discount on unused capacity is still an expense. A contract that makes switching expensive can be reasonable, but the loss of flexibility should be visible when it’s approved.

![A fixed cloud commitment can cost less at stable demand and more when flexible demand falls below the commitment.](private-techuity/posts/10-cheaper-cloud-bill/assets/images/10-cheaper-cloud-bill/fixed-commitment-changing-demand.jpeg)

**Figure 2:** *Test the commitment against lower demand as well as the forecast that makes it attractive.*

{id: cheaper-cloud-bill--the-decision-larkspur-makes}
### The Decision Larkspur Makes

The two cases above bracket the choice; they don’t make it. To decide, Larkspur states a demand range and a funding condition.

**Demand range.** Eighteen months of usage show that flexible-rate spending has never fallen below €30,000 a month. The board-approved operating plan puts next year between €30,000 (onboarding stalls and the largest customer leaves) and €60,000 (the plan’s growth arrives). The €20,000 case lies outside that range; it is kept as a stress test, not a forecast.

**Funding condition.** Larkspur’s cash plan assumes no new financing for the next twelve months, and the board has approved an operating plan for that period only. A three-year commitment would extend past the funded horizon and past any ownership change in that time.

Three options are compared on the same basis:

| Option | Cost at €30,000 demand | Cost at €50,000 demand | Cost at €60,000 demand | Cost at €20,000 stress case |
| --- | ---: | ---: | ---: | ---: |
| A. Stay flexible | €30,000 | €50,000 | €60,000 | €20,000 |
| B. Three-year commitment covering €50,000 of demand (€35,000 fixed) | €35,000 | €35,000 | €45,000 | €35,000 |
| C. One-year commitment covering €30,000 of demand (€21,000 fixed), remainder flexible | €21,000 | €41,000 | €51,000 | €21,000 |

Option B saves €15,000 a month at or above forecast demand but costs €5,000 more at the low end of the range and €15,000 more in the stress case. Option C saves €9,000 a month at every point in the stated range, costs €1,000 more in the stress case, and expires with the funded horizon.

**Larkspur chooses Option C.** Alex proposes it with the usage history and the plan’s demand range as evidence; Sam confirms the commitment is paid monthly, so cash timing matches cost, and confirms what the contract says about early termination and transfer; Ines approves it within her delegated authority for contracts of one year or less. Option B is rejected: its extra €6,000 a month of saving, which exists only at €50,000 of demand or above and turns into a €14,000 disadvantage at the low end of the range, is bought with exposure beyond the period anyone has approved a plan for. Option A is rejected because a €9,000 monthly saving with no downside inside the stated range is real money. The decision is reviewed if flexible spending falls below €30,000 for two consecutive months, if rightsizing work reduces the eligible volume, if a transaction or carve-out is proposed, or if the provider offers transfer rights.

This is one result under one set of conditions. A company with stable demand and multi-year committed funding might reasonably accept Option B after the same comparison. The rule is not “commit less”; it is that the commitment follows from a stated range and horizon, and the person approving it can see the case where it costs more.

Product and engineering leaders should involve **procurement**, the people responsible for buying and negotiating supplier services, and finance early. Engineering understands usage and migration feasibility. Finance understands payment timing and accounting. Procurement and legal specialists interpret commercial terms. None of those views is sufficient by itself.

{id: cheaper-cloud-bill--credits-minimum-spend-and-ownership-change-conditions}
## Credits, Minimum Spend and Ownership-Change Conditions

Contract terms that change the invoice without changing the resources consumed belong together, because they distort the same comparison.

**Temporary credits.** In a separate fictional Larkspur scenario, cloud credits reduce a €30,000 monthly service bill to €5,000 for six months. The underlying service still consumes €30,000 of resources at the stated prices. A plan extending beyond the credits needs to show the later cash requirement. Compare customer economics with and without the subsidy before describing the service as profitable.

**Minimum spend and the signing entity.** An investor may introduce a provider, or a corporate parent may offer a group discount. Ask which entity signs, whether a minimum spend applies, and who benefits from the price reduction and who bears unused capacity. The help can be useful while also creating a commitment the company must carry after the relationship changes. The investor’s procurement access is an input to the decision, not its conclusion.

**Ownership change.** A commitment that can’t transfer on a carve-out can become a **stranded cost**: one the company still owes but no longer benefits from. Check renewal terms and what happens if ownership changes or the product moves to another provider before signing, not during the transaction. After an acquisition, applying the group’s negotiated discount to an acquired company’s bill and calling the result a **synergy** skips the cost of moving it onto the common platform; [An Acquisition Adds Work Before It Adds Value](#acquisition-adds-work-first) treats that comparison.

None of these terms is a problem in itself. The test is whether the company can see the continuing cost behind the invoice, and whether the service is still the one the customer bought.

{id: cheaper-cloud-bill--protect-the-service-the-customer-bought}
## Protect the Service the Customer Bought

The easiest way to reduce some costs is to reduce the service. Whether that’s acceptable is a product decision. Less **redundancy**, meaning fewer spare components or alternative ways to keep operating, longer processing windows or reduced support coverage can change the customer’s experience and the company’s risk.

Define service conditions alongside the cost target. Track successful work completed, **latency**, the time a user waits for a response, where it matters, error rates, recovery performance and customer complaints. The exact measures should follow the product promise. A low-cost service that can’t complete a customer’s essential workflow has poor economics even if the infrastructure dashboard looks efficient.

{id: cheaper-cloud-bill--prove-the-saving-actually-arrived}
## Prove the Saving Actually Arrived

Before a cost initiative starts, define the **baseline**, the starting costs and demand used for comparison. Estimate what spending would have been without the initiative, and state which costs are included. Then keep three things separate as the work proceeds:

- **Opportunity:** a model of what might be saved.
- **Change implemented:** resources or contracts actually changed.
- **Observed net effect:** the net expenditure or avoided expenditure actually seen, with transition costs and demand changes reconciled and put on the agreed cost basis.

A **run-rate projection**, such as “€9,000 a month, so €108,000 a year,” is a separate, labelled estimate. It assumes the observed month repeats; state that assumption and what would break it. It is not a fourth observation.

A capacity reduction may avoid a forecast increase rather than reduce this month’s bill. That can be valuable, but the forecast and its uncertainty should stay visible. Similarly, reducing internal support effort doesn’t automatically reduce payroll.

An initiative record should include implementation labor, specialist fees, tooling, the cost of running old and new services together, and ongoing maintenance. A payback calculation must include **the work required to capture savings**. Comparable services and people who have faced the same decision, including through an investor’s network, are covered in [Find the Help That Changes What Your Team Can Do](#help-that-changes-capability).

A useful cost improvement has an explanation the company can check: what changed, on what basis it was measured, how demand affected the comparison, what the transition cost and whether service remained acceptable. Larkspur’s answer to Morgan’s question is not “the bill went up 20%” or “we found €15,000 a month.” It has two parts that must stay separate. Unit cost per successful transaction fell 20% against the prior year, so the service became more efficient. The flat-spend plan was still missed: spending is €20,000 a month above the approved envelope, and unit cost is 20% above what the plan implied. The one-year commitment on the scheduling service closes €9,000 of that gap at every point in the approved demand range, would cost €1,000 more in the stress case, and is revisited if usage or ownership changes. Alex still owes the board an explanation of the remaining €11,000 a month of cost drivers, and either further changes or a revised envelope. That is a contractual choice beside an honest plan comparison, not a savings announcement.

The commitment was tested against demand the company can observe. Some spending instead buys protection against harm the company hopes never to observe, and a lower bill there can mean the protection quietly went away. The next chapter shows how to judge that spending on evidence: [Prove You Can Restore, Not Just That You Back Up](#prove-you-can-restore).

{id: cheaper-cloud-bill--questions-to-consider}
## Questions to Consider

1. *What unit of useful service does your cost per unit describe, are the figures you compare over time on the same cost basis, and do you read them against the plan you were funded for as well as the prior period?*
2. *When your infrastructure bill last changed, how much came from usage, rates, architecture or demand? Were any savings counted twice?*
3. *Which of your commitments would become stranded cost if demand fell below the range you planned for, the product moved or the company were separated from its owner?*

{id: cheaper-cloud-bill--to-probe-further}
## To Probe Further

- **[Cloud FinOps, 2nd edition](https://www.finops.org/community/finops-book/)** — J.R. Storment and Mike Fuller, O'Reilly, 2023.  
  *The book behind the FinOps practice this chapter cites, whose chapters on usage, rate and commitment optimization show how to avoid counting the same saving twice.*
- **[Cost Optimization Pillar, AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)** — Amazon Web Services, 2024.  
  *The supplier's own account of good practice, useful for the vocabulary your procurement discussion will use, though it treats staying on the platform as given.*
- **[Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)** — chapter 4 of *Site Reliability Engineering*, Google, O'Reilly, 2016.  
  *Explains how to state the service conditions this chapter says must sit beside any cost target, so you can define the service the customer bought before someone cuts it.*
- **[The Cost of Cloud, a Trillion Dollar Paradox](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)** — Sarah Wang and Martin Casado, Andreessen Horowitz, 2021.  
  *A disputed argument from a venture firm that shows exactly how an investor may connect your cloud bill to margins and enterprise value.*
- **[Why we're leaving the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)** — David Heinemeier Hansson, 37signals, 2022.  
  *One company's decision to leave the cloud with real bill figures and a clear statement of when cloud still makes sense, read as a case rather than a rule.*
