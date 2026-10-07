{id: understand-funding-choices}
# 7. Understand Funding Choices: Match the Money to the Work

![Understand Funding Choices: Match the Money to the Work — logo](private-techuity/posts/04-understand-funding-choices/assets/images/04-understand-funding-choices/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to size the work the company must do next, compare the funding arrangements that could support it, and act on an arrangement you inherited.

> **WHY INVESTORS CARE:** A **raise** brings in money from outside the company; a **round** is one such event. Raise **too little** and the company may need a **rescue round**: urgent money on worse terms. Raise **too much** and the same gain is spread over more money, **diluting returns**, while the surplus funds work that was never justified. Investors weigh the ownership given up, the reserve kept and the risk of raising again against the plan, as the company should.

> **WHY YOU SHOULD CARE:** Funding that does not match the work either starves the plan or buys it with rights, obligations and expectations the company cannot afford. The mismatch lands on the people who must deliver.

> **KEY POINTS:**
>
> * Start with the **problem the money must solve, and size it**: base work, transition costs, an allowance for uncertainty, and runway (the time the money buys before the next decision). Funding expansion, paying a retiring founder and separating a business from a parent are different needs.
> * Examine the **terms behind the investor’s label**. The terms and the investor’s expectations, not the category, set the pace, the losses tolerated and the time the plan gets.
> * Product and engineering leaders who **inherit the arrangement** can still act: bring the costed scope, a cash requirement and an alternative to the people who can renegotiate it. Changing the financing, changing the plan or continuing without a new owner can each be the right answer.

> **[DYSFUNCTIONS THIS SECTION ADDRESSES](#where-investment-goes-wrong):**
>
> * **The Ratchet Roadmap** — Sizes the work, transition costs and uncertainty before choosing funding and commitments.
> * **Spending the Press Release** — Tests funding terms and timing against the work the company must pay for.

A business has customers and a useful product. Its founder might want money to expand it, or might want to retire and sell their shares, the units of ownership in the company. Those are different needs, even if both conversations begin with “we need an investor.”

The preceding chapters explained funding, ownership, valuation and returns, and the last showed that an investor's return depends on price, borrowing and timing as much as on the business. This chapter turns the question around: **how much money does the next piece of work actually need**, and which arrangement can supply it without attaching **conditions** the work cannot meet?

Product and engineering leaders may not choose the investor, but they **inherit the consequences** of the choice. The terms of the funding, the conditions attached to the money, and the investor’s expectations affect the pace at which results are expected, how much loss the shareholders will tolerate and how long the plan has before it is judged. Those **terms come from the agreement**, not from the category on the investor’s website: two growth investors can offer different rights and different patience. A migration (moving customers or data from an old system to a new one) or a product bet that fits one set of terms can be unaffordable or unwanted under another.

{id: understand-funding-choices--separate-the-owner-the-financing-and-the-situation}
## Separate the Owner, the Financing and the Situation

**Investor type** describes who supplies money in exchange for a share of ownership, and what they seek. **Control** concerns the rights to decide. **Financing** concerns the money and its obligations: whether it is borrowed and must be repaid, or exchanged for ownership. **Transaction context** describes an event such as a funding round, an acquisition (one company buying another) or a separation. These dimensions interact, but none replaces the others. A founder might need personal cash from selling shares while the company needs no new funding; a large transaction can leave the company with no new money.

The chapter [Understand Expectations: Customers, Lenders and Investors](#understand-expectations) and the [Introduction & Reading Guide](#introduction) introduce the arrangements. The recap below says in a phrase what each one is and keeps only the question it raises about the work; the operating consequences are conditional judgments, not evidence that all investors in a category behave alike.

| Arrangement | What it is | The question to test against the work |
| --- | --- | --- |
| Venture funding | Ownership investment in a young company whose product may not yet pay for itself, by investors who expect many failures and a few large successes | What evidence can arrive before current cash runs short, and what happens if another round does not complete? |
| Growth funding | Ownership investment in an established business to expand what already works | Which part of growth is already repeatable, and what must be funded to repeat it elsewhere? |
| Buyout ownership | An investor buys a controlling share of the company, often partly with borrowed money that the company then carries | How much cash reaches the company, what rights change and what borrowing limits the money that can be put back into the business? |
| Corporate minority investment | An operating company buys less than half of another company, usually for commercial reasons | Which product and information requests serve the wider customer base, and which chiefly serve the investor? |
| Corporate acquisition | An operating company buys the whole company and makes it part of its group | What stays local, what must be connected to the group’s systems and which group budget funds the work that depends on it? |
| Continued founder or family ownership | The current owners keep the company and fund it from its own cash | Which growth pace is acceptable to the current shareholders, and how much of their wealth are they willing to keep tied to this one business? |

A **carve-out** separates a business from a parent; a **turnaround** addresses serious operating or financial problems; an **acquisition** purchases a company or its assets, such as its software and customer contracts, and may use cash, borrowing or shares. These describe the situation, not who the investor is: any kind of owner can be involved in any of them. Label the situation separately from the owner. Otherwise, a deadline for connecting the business to a parent’s systems (an integration), or a cash crisis, gets blamed on the type of owner rather than on the situation that caused it.

![One fictional proposal for onboarding, setting new customers up to use the software, becomes a demand test, a repeatable rollout, work scheduled around payment dates or an integration into a parent group’s distribution, depending on the funding and authority behind it.](private-techuity/posts/04-understand-funding-choices/assets/images/04-understand-funding-choices/one-product-different-funding-plans.jpeg)

**Figure 1:** *The same onboarding work, setting new customers up to use the software, needs a different plan under different funding, authority and expected outcomes; the four routes are explained in the paragraph below.*

Reading the figure: the same proposal can become a **demand test** (a **pilot**, a small trial with a few customers, run first to learn whether they will pay before more money is committed), a **repeatable rollout** (a setup process that has already worked, repeated for more customers), **work scheduled around payment dates** (spending timed so that loan repayments are always covered, with any surplus put back into the business) or an **integration into group distribution** (the parent company’s sales channels selling to its own customers, through partners it already has). The funding and the authority behind the proposal decide which of the four it becomes.

{id: understand-funding-choices--size-the-work-before-you-name-the-investor}
## Size the Work Before You Name the Investor

Take Rotaline, the fictional scheduling-software company used throughout this book. In this scenario customers already buy the product, but onboarding, the setup of each new customer, depends on the implementation team configuring the product by hand, and the **queue of waiting customers is growing**. Ines, who runs the company as its chief executive, and Sam, who runs its finances, are weighing outside money. Alex, who leads engineering, and Priya, the product leader, are asked what the fix costs.

The first mistake would be to size the raise **from the offer on the table**. The second would be to size it **from the build alone**. The reusable setup step from the chapter [Test Revenue Assumptions: Do Customers Respond as Expected?](#test-revenue-assumptions) costs about €180,000 to build; a request for €180,000 would fund the software and nothing that makes it work.

| Component of the need | Cash | Basis |
| --- | ---: | --- |
| Base work: build the reusable setup step | €180,000 | 12 engineer-weeks, as in [Set Priorities: You Cannot Fund Everything at Once](#set-priorities); one engineer-week is one engineer’s work for one week, here three engineers for four weeks |
| First year of maintenance: keeping the step working after it ships | €30,000 | €30,000 a year, paid in the financial year after the step ships (months 13–24); later years sit inside the operating forecast |
| Transition: run the manual and new process in parallel for two quarters (a quarter is a three-month period), migrate existing configurations, train the implementation team | €90,000 | Estimated from the current implementations, which take 80 staff hours each |
| Interim capacity: one contract implementation specialist for twelve months (months 1–12), setting customers up while the step is built and proved | €150,000 | Without it the queue grows during the build. The contract also covers any hours the specialist spends on the amber data-quality step, so they are not billed again there |
| Uncertainty allowance: 25% of build and transition | €70,000 | 25% of €270,000 is €67,500, rounded up to €70,000; effort may fall to 62 hours per customer rather than the 50 assumed |
| Decision runway: six further months (months 13–18) of the contract specialist and of keeping the old manual process running alongside the new step, if the cohort evidence, the measured result from the first group of customers, arrives late | €90,000 | €75,000 for the specialist and €15,000 for the parallel running; maintenance in those months is already in the maintenance row. Keeps the choice open without a raise under pressure |
| **Cash need** | **€610,000** | About €160,000 is allowance and runway, not base work |

Whatever the funding, the **scarce resource is people**. The work needs twelve engineer-weeks to build the reusable setup step, plus the one implementation specialist who understands how existing customers are configured. Both are needed in the same two quarters, whichever funding arrangement pays for them, so more money cannot make them available sooner. Twelve engineer-weeks measures **effort, not elapsed time**: with three engineers working on it, the step is usable from about day 35, but the transition around it (running the old and new processes side by side, migrating configurations, training the team) still takes both quarters.

{id: understand-funding-choices--two-ways-to-fund-the-setup-step-plan}
### Two Ways to Fund the Setup-Step Plan

Sam has two realistic ways to fund the plan: selling part of the company to a growth investor, or taking a bank loan. Both raise the €610,000; they differ in what comes with the money. The investor wants a say in the budget and senior hires; the bank wants regular repayments. Both options rest on one assumption: Rotaline generates about €350,000 of **operating cash** a year, the money left from ordinary trading after tax and existing obligations. That figure is before any interest on new borrowing and before the minimum cash balance the **board**, the group of directors that oversees the company on the shareholders’ behalf, requires it to hold. In this scenario that minimum is €200,000 and Rotaline holds €250,000, so only €50,000 is available above it. The company therefore cannot pay for the plan from its own cash, and any loan must be repaid out of that €350,000 a year.

**Arrangement A: €2.5 million (€2.5m) of growth equity.** **Equity** is money exchanged for a share of ownership; **growth equity** is equity provided to **expand a business** that already works. A growth investor offers €2.5m for a **minority stake**, a share of less than half the company, with approval rights over the annual budget and senior hires, meaning those decisions need the investor’s agreement. The offer records entry into a second country within eighteen months as the plan the money is raised on. That expansion is not a contractual obligation, but the approval right over the budget means the board cannot spend the money on a slower plan without the investor’s agreement, which is where an **expectation becomes a pace**. The offer funds the onboarding work about four times over. The surplus is a reserve against the pilot disappointing, and it makes a later round less likely to be needed soon; it does not remove the risk, because a raise would still be needed if the expansion consumed the surplus before the pilot had paid for itself. The pace also has a cost: the second country needs a working setup step first, or it exports the manual bottleneck, and the surplus becomes a sales-hiring budget before the pilot has produced any evidence.

**Arrangement B: a €750,000 term loan, with the work done in stages.** A **term loan** is borrowed money repaid over an agreed period; the **principal** is the amount borrowed, and **interest** is the charge for borrowing it. The company’s bank offers a four-year loan at 8% with a one-year **principal holiday**, a period at the start of a loan when the borrower pays **only interest** and repays none of the amount borrowed. In that first year, Rotaline pays €60,000 of interest. Each year’s interest is 8% of the balance at the start of the year, paid at year end together with that year’s principal. From the second year, Rotaline repays €250,000 of principal a year, so the loan is fully repaid at the end of year four; the second year’s payment alone is €310,000 of the €350,000 operating cash. The current shareholders keep control of the company, and the €140,000 borrowed beyond the €610,000 need is held as a cash cushion for surprises. The catch is that the repayments are fixed whatever the pilot shows. If the pilot disappoints and the company later needs an investor after all, that money might cost a larger share of the company than it would today, or might not be available at all.

| Year | Loan balance at start | Interest at 8% | Principal repaid | Payment at year end | Loan balance at end | Year’s operating cash (€350,000) minus the payment |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | €750,000 | €60,000 | €0 | €60,000 | €750,000 | €290,000 |
| 2 | €750,000 | €60,000 | €250,000 | €310,000 | €500,000 | €40,000 |
| 3 | €500,000 | €40,000 | €250,000 | €290,000 | €250,000 | €60,000 |
| 4 | €250,000 | €20,000 | €250,000 | €270,000 | €0 | €80,000 |

Total interest over the term is €180,000, and the four payments total €930,000. The last column tests each payment against that year’s operating cash alone; the stated assumptions below say why nothing else is counted.

**Why Rotaline cannot simply pay as it goes.** €350,000 of operating cash a year sounds close to €610,000 spread over eighteen months, but most of the **spending comes early**. The build (€180,000), the transition (€90,000) and the first six months of the contract specialist (€75,000) all fall in the first two quarters: about €345,000. In those same six months only about €175,000 of operating cash comes in, and Rotaline has just €50,000 above the board’s minimum balance. The arithmetic: €345,000 out, €225,000 available, so paying as the cash arrived would leave the company about €120,000 below the required minimum by month six. And that is before funding the two safety margins in the plan: the **uncertainty allowance** (€70,000), extra money in case the build and transition cost more than estimated, and the **decision runway** (€90,000), six more months of the specialist and the old process in case the evidence from the first customers arrives late. The company would then have to raise money in a hurry, on whatever terms it could get, which is exactly the situation the decision runway is meant to prevent.

**Stated assumptions.** The comparison rests on a few assumptions, and they are not equally solid:
- **What is proven:** customer evidence shows that slow setup really is holding back growth. Demand in a second country is not yet proven.
- **What is shared with other chapters:** the financing comparison is this chapter’s own scenario, but it borrows the pilot from the shared Rotaline storyline: €180,000 to build the setup step, €30,000 a year to maintain it, and its measured result.
- **The weaker outcome:** the 62-hour case is what Priya later measures in the chapter [Test Revenue Assumptions: Do Customers Respond as Expected?](#test-revenue-assumptions), on the first eight customers set up with the new step, ninety days after the board adopts the plan. The model there projects that at 62 hours per customer the step frees about €135,000 a year of implementation staff time; at the hoped-for 50 hours, about €225,000.
- **Freed time is not cash:** freed staff time is valuable, but it does not pay a loan. Finance counts it towards repayments only once it turns into money, either because contractor spending is actually cancelled or because customers pay more **contribution**, the cash they pay less the direct cost of serving them, and that cash has actually been received.

**The choice.** Under these assumptions Ines and Sam recommend B to the board. The work is bounded and the evidence arrives within the first year. Sam’s test is strict: each year’s payment must be covered by that year’s €350,000 of **operating cash alone**, without counting the €135,000 of **released time**, the €140,000 **reserve** or cash retained from earlier years. The schedule passes that test in every year. Year two has the least margin: €40,000 after the €310,000 payment.

**The dated review.** At day 90, counted from the board meeting that adopts the plan, Priya measures the first **cohort**, the group of eight customers who are the first to be set up with the new step. The board decides at day 100, as in the chapter [Plan the First Hundred Days: Turn Expectations Into Funded Work](#first-hundred-days). The measure is the average staff hours needed to set up one customer: 80 today, with 50 the target. Below 60 hours is green: request the expansion at the next quarterly review. Between 60 and 70 hours is amber: fund the data-quality step, work that validates and corrects a customer’s data before setup begins, because poor customer data is where much of the remaining effort goes; keep expansion and hiring deferred. The 62-hour case sits here. Above 70 hours, or no reduction, is red: reopen hiring, narrow the target or reopen the equity conversation, and act while there is still cash in hand.

**Who does the work, and when.** The plan books each person once, in this order:
- **Days 0–35, build:** three engineers spend four weeks (the twelve engineer-weeks) building the setup step, so it is usable from about day 35.
- **Days 35–90, first cohort:** the implementation team, not the engineers, sets up the first eight customers with the new step.
- **From day 100, only if the result is amber, the data-quality step:** it costs €40,000 and four engineer-weeks. The €40,000 comes from the €140,000 reserve and buys two things the plan does not already pay for: an external data-validation service, which checks each customer’s records against the new step’s rules and flags errors, and temporary data-entry help to correct the flagged records. The contract specialist reviews those corrections, but that time is already covered by the €150,000 for months 1–12 and is not billed again. The four engineer-weeks are not money from the reserve but people: two of the same three engineers return for two weeks to build the validation into the step, which pushes the reporting improvements they were due to start back by two weeks.
- **Months 4–6, second cohort:** with the improved step ready by about month four, the implementation team sets up another eight customers, and Priya measures them at month six.

Throughout, the internal specialist and the contract specialist stay on the transition, so nobody is booked twice.

**Cash balance, base case and downside.** Two different checks answer two different questions. The **strict annual test** asks whether each year’s loan payment is covered by that year’s operating cash. The **cash forecast** below asks how much money is actually in the bank at the end of each year. Both rows assume the pilot result this chapter takes from the shared storyline:
- the first eight customers take an average of 62 hours each to set up, an amber result, so the €40,000 data-quality step is paid from the reserve in year one;
- that result arrives on time, so the €90,000 decision runway is never spent and the contract specialist is not kept on beyond month 12.

Had the first customers taken under 60 hours each on average, the green outcome in the review rules above, the data-quality step would not be needed and every year-end balance would be €40,000 higher. All figures are cash above the €200,000 minimum balance, and every number is fictional.

| Cash above the €200,000 minimum | Year 1 | Year 2 | Year 3 | Year 4 |
| --- | ---: | ---: | ---: | ---: |
| Opening | €50,000 | €630,000 | €640,000 | €700,000 |
| Loan received | €750,000 | – | – | – |
| Operating cash | €350,000 | €350,000 | €350,000 | €350,000 |
| Work paid for | −€460,000 | −€30,000 | – | – |
| Loan payment | −€60,000 | −€310,000 | −€290,000 | −€270,000 |
| Closing, base case | €630,000 | €640,000 | €700,000 | €780,000 |
| Of which still earmarked for the work (see the note below) | €290,000 | – | – | – |
| Closing, downside (operating cash €300,000 from year two) | €630,000 | €590,000 | €600,000 | €630,000 |

How to read the table:
- **Work paid for, year one (€460,000):** the build (€180,000), the transition (€90,000), twelve months of the contract specialist (€150,000) and the data-quality step (€40,000). The €40,000 pays only for the validation service and the data-entry help; the specialist’s hours on that step are already inside the €150,000.
- **Work paid for, year two (€30,000):** the first year of maintenance, which falls in the financial year after the step ships. From year three, maintenance is an ordinary running cost and is already included in the €350,000 operating-cash forecast.
- **Still earmarked at the end of year one (€290,000):** part of the €630,000 closing balance is set aside for the plan and should not be spent on anything else. It is the €70,000 uncertainty allowance and the €90,000 decision runway, both unspent and held until month 18; the €30,000 of maintenance due in year two; and the €100,000 left of the reserve (€140,000 less the €40,000 data-quality step).
- **Nothing earmarked after year two:** at month 18 the funded period ends, and whatever is left of the allowance, the runway and the reserve becomes ordinary cash again. No money moves and the balance does not change; the cash simply stops being reserved for the plan.

**What happens in Sam’s downside.** Suppose that from year two operating cash falls to €300,000, about 14% lower, because customers pay later and some do not renew their contracts while the setup queue stays long. Year by year, against the loan payments:
- **Year two:** €300,000 comes in against a €310,000 payment, a €10,000 shortfall.
- **Years three and four:** €300,000 covers the €290,000 and €270,000 payments, but with only €10,000 and €30,000 to spare.

The year-two payment is still made. The missing €10,000 comes out of the cash kept from year one, €340,000 of which is not earmarked for the plan. So the downside means a year in which **trading does not cover the loan**, not a missed payment. The cost is that the same retained cash must also absorb any build overrun or late cohort result; on this forecast it is enough for both. What neither forecast rules out is worse: if collections fall further or costs rise, cash could run short on a repayment date in any year of the loan. That is the **risk a fixed repayment schedule carries** and the investor’s money does not.

**Why the €135,000 of freed time is left out of the forecast.** On the day the first cohort is measured, no contract has been cancelled and no extra money has come in from customers, so the freed staff time is not yet cash that could meet a loan payment. It can turn into cash, or avoided cost, in three ways, each with its own condition:
- **The contract specialist is not kept on.** If the setup queue is moving by month twelve, the specialist’s contract is not extended, so up to €150,000 a year is never spent. The first €75,000 of that is the specialist’s share of the decision runway.
- **The two planned specialist hires stay on hold.** This avoids €300,000 a year of future cost, but it reduces nothing the company spends today.
- **Faster setup brings in more contribution.** Extra contribution from customers set up sooner is counted only after the second cohort, measured at month six, averages 50 hours or less and customers are waiting less time to be set up.

**What the reserve is for.** The €140,000 **reserve does not pay the loan**: interest and principal come from operating cash on the schedule above. The reserve is held against the **work overrunning** or the **cohort arriving late**; the amber step took €40,000 of it, leaving €100,000. If €10,000 of that were used for a payment instead, the €610,000 of work would still be funded, but the cushion would be €90,000, and an overrun in the same year would land on what was left.

Sam rejects Arrangement A, the €2.5m from a growth investor, **because of its pace, not its price**. The investor would be backing a full expansion plan before the pilot has shown that the new setup step works. Its approval right over the budget would also mean that if Rotaline wanted to slow down, it would have to **negotiate with the investor instead of deciding for itself**. And the €1.9m raised beyond the €610,000 need would cost a permanent share of the company, only to protect against a risk that the staged plan already covers with a smaller cash cushion. Sam also rejects a third option: raising nothing and paying only the €180,000 build from Rotaline’s own cash. That would leave no money for the transition, the contract specialist or the decision runway, so if the first cohort’s result came late, the company would have to raise money in a hurry, on whatever terms it could get.

**What would reverse the decision.** Signed commitments from customers in the second country would make A’s pace fit the work. On the loan side, a red result at day 100 reopens the decision. Red does not mean the loan is being repaid from capacity that failed to appear; the payments never depended on it. It means the work the loan was sized for is not delivering, and the €40,000 margin in year two has to carry that disappointment as well.

**Who decides, and who recommends.** Different people own the financing and the case for the work:
- **The financing:** Ines and Sam negotiate the loan or the investment and take it to the board for approval. The shareholders’ agreement, the contract among the owners, says which decisions also need the owners’ approval (**shareholder consent**). Alex and Priya do not sign the financing.
- **The work:** Alex and Priya bring the case for the work itself. Here that meant the revised scope; the €610,000 cash need, broken into its parts; the alternative of hiring two implementation specialists for about €300,000 every year; and the dated review, with the first cohort measured at day 90 and the board deciding at day 100. Their recommendation covers which option to fund, in what order, and what evidence would show it isn’t working.

**How much is borrowed matters more than what the financing is called.** Suppose Rotaline were instead carrying acquisition debt, money borrowed to buy the company. If that debt cost €4m a year in interest rather than €1m, Rotaline would have €3m a year less for everything else, other things being equal. That €3m is about five times the €610,000 the setup work needs, so the size of the debt, not its label, does most to decide how much is left for the work. Interest alone still does not show whether the work is affordable: the company must also pay tax, keep investing and wait for customers to pay. The chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow) works through all of these in a cash bridge, a step-by-step calculation from earnings down to the cash left over.

{id: understand-funding-choices--control-and-partnership-are-separate-questions}
## Control and Partnership Are Separate Questions

A **majority investor**, one holding more than half the shares, can have substantial influence, but the actual exercise of control depends on the agreements. A **minority investor**, holding less than half, may hold **approval rights** over financing, budgets, hiring or a sale, and a founder who keeps shares may not keep the same role. Ask for the decision boundaries in plain language — who approves material hiring, who funds a product transition if the original plan proves wrong, which decisions need board or shareholder consent — and let legal advisers resolve the contractual interpretation. The chapter [Clarify Authority: Decide Who Decides Before You Disagree](#clarify-authority) builds that authority map.

**Partnership**, how good a partner the investor would be, is a separate question from the terms of the deal. It asks three things: can the investor put in more money later, does it bring relevant experience, and will it stay steady when the plan runs into trouble? Investors’ own descriptions of themselves are a weak guide. Gompers, Kaplan and Mukharlyamov surveyed 79 private equity investors, funds that buy ownership of companies whose shares are not traded on a stock exchange. The investors said they emphasize growing the companies they buy more than cutting costs. But the survey records what investors say they do, not what each one actually delivered, so treat any such claim as something to check against specific evidence, such as the record of companies the investor has backed. [S04: survey of private equity practitioners](https://www.nber.org/papers/w21133) The chapter [Assess Investor Fit: Behavior Under Pressure](#assess-investor-fit) sets out how to run that check.

{id: understand-funding-choices--revisit-the-fit-when-the-plan-changes}
## Revisit the Fit When the Plan Changes

An arrangement that fitted the original plan may become restrictive when demand slows, a migration takes longer or a new market needs more investment. In the Rotaline case, a day-90 cohort that comes in red turns the loan from comfortable to tight: the payments do not change, and the €40,000 margin in year two was set on operating cash alone, with the cash retained in year one and what remains of the €140,000 reserve behind it, and nothing else. Recheck the remaining cash, repayment dates, approval rights and investor expectations against the revised work, not the original one.

If the funding no longer fits the work, there are several ways to respond. The company might slow the pace of the work, release the investment in stages tied to results, or renegotiate the loan or investment terms. It can also step back and compare different kinds of ownership against the work ahead: staying owned by its founders, taking a minority investor, or selling to a **strategic buyer**, another operating business that buys it for commercial reasons, such as adding its product to the buyer’s own. Any of three conclusions can be right: change the deal, change the plan, or keep both as they are. A company that decides against outside ownership hasn’t failed a test; it has answered the question.

![Changes in customer demand, available funding or time remaining feed a review of the assumptions, which leads to one of three outcomes: adjust the scope, that is, change the work included in the plan; change the financing; or continue as planned. Each outcome loops back into the next review.](private-techuity/posts/04-understand-funding-choices/assets/images/04-understand-funding-choices/investment-fit-review-loop.jpeg)

**Figure 2:** *Investment fit needs reassessment when the assumptions supporting the work change. A review can end in adjusting the scope (changing the work included in the plan), changing the financing, or continuing as planned.*

The useful question is “**what work** must this business do next, and which **ownership and funding arrangement** can support it?” Once the arrangement is chosen, the next question is how much of the company’s earnings is actually cash the work can use. The chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow) works down from EBITDA to the cash left after financing, tax, investment and working capital.

{id: understand-funding-choices--questions-to-consider}
## Questions to Consider

1. *What work does your company need to do next, and what does it cost in full: base work, transition, an allowance for uncertainty and runway to the next decision?*
2. *Which two arrangements could fund that need, and what does each bring besides the money: rights, an expected pace, fixed repayments, a reserve?*
3. *If demand slowed or a migration took twice as long, which part of the arrangement would become restrictive first: cash, repayment dates, approval rights or investor expectations?*
4. *What can you recommend from your role, and who in your company can renegotiate the financing?*

{id: understand-funding-choices--to-probe-further}
## To Probe Further

- **[Bootstrap Finance: The Art of Start-ups](https://hbr.org/1992/11/bootstrap-finance-the-art-of-start-ups)** — Amar Bhidé, Harvard Business Review, 1992.  
  *A study of fast-growing companies that started without venture capital, funding themselves from their founders’ savings and their customers’ payments: the case that raising less can be right, which this chapter treats as one legitimate outcome of a sized comparison rather than a rule.*
- **[How to Fund a Startup](https://paulgraham.com/startupfunding.html)** — Paul Graham, 2005.  
  *A seed investor (one who supplies money at the start of a company) walks through the funding sources as a sequence, to read alongside this chapter’s point that the sequence is not a required ladder.*
- **[How Do Venture Capitalists Make Decisions?](https://www.nber.org/papers/w22587)** — Paul Gompers, Will Gornall, Steven Kaplan and Ilya Strebulaev, National Bureau of Economic Research working paper, 2016 (Journal of Financial Economics, 2020).  
  *A survey of 885 venture investors on how they select companies, value them and get their money out, which is what the “venture funding” row of this chapter’s table expects, in their own words.*
- **[Financial Contracting Theory Meets the Real World: An Empirical Analysis of Venture Capital Contracts](https://www.nber.org/papers/w7660)** — Steven Kaplan and Per Strömberg, National Bureau of Economic Research working paper, 2000 (Review of Economic Studies, 2003).  
  *Evidence from real investment contracts that the rights to the company’s cash, the votes, the board seats and the order of payment if the company is sold or closed down are allocated separately, the research behind this chapter’s claim that control is more than a percentage.*
