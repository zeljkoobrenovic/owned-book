{id: can-the-team-deliver}
# 13. Assess Capability: Can the Team Deliver?

![Assess Capability: Can the Team Deliver? — logo](private-techuity/posts/11-can-the-team-deliver/assets/images/11-can-the-team-deliver/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to assess whether the software and the team can deliver the plan, and produce a finding that names the obstacle that most limits the plan (its **binding constraint**), the evidence, and what a transition would cost in money and time.

> **WHY INVESTORS CARE:** An investor puts money into a company expecting a return. Its reasoning for doing so, the investment case, assumes the systems and the team can support the plan. An assessment that finds the biggest obstacle early lets the investor reconsider the price it is willing to pay, or agree a different order and timing of work, rather than discover the problem through a missed deadline.

> **WHY YOU SHOULD CARE:** If the investment plan assumes a country launch before the systems have been assessed, the assessment tests whether the date and budget are credible, and gives the board, the directors who oversee the company, its first grounded view of what the plan will cost and when it can arrive.

> **KEY POINTS:**
>
> * Begin with **what the plan requires the company to do**. Name the changes, scale and reliability the business plan needs before judging any system.
> * Judge the technology and the team by **their consequences for that work**, and record strengths as well as constraints. An old system is not, by itself, a bad investment; a fashionable one is not a good one.
> * End with **a finding the next decisions can use**: the obstacle that most limits the plan, the evidence behind it, what is uncertain, and what a transition would cost, over what period, and when its first benefit could appear.

Larkspur, the fictional scheduling-software company, plans to serve customers in a second country. Its board has a plan that proposes the first paying customers there within twelve months. Its software assumes one set of tax and pricing rules, its contracts cover one market, and its support team works in one language. Which changes are needed before expansion can succeed?

The expansion date was proposed before anyone assessed the plan’s **dependencies**: the other work, systems and people it relies on. That is the condition this chapter starts from, and it is a common one. An investor’s growth assumption or a board’s plan can fix a destination and a timetable before anyone has examined the technology closely. That does not make the plan wrong. It changes the order of the work.

Alex, Larkspur’s technology leader, has to establish three things before the company commits money or makes a promise to a customer: what the systems and the team can support today, what must change in the plan, and what changing it would cost. That takes more than a look at the software, because the people who run it are part of what the company can do. The systems may be built in-house, bought from suppliers or assembled from both; the assessment is the same.

The chapter [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue) connected a proposed change to customer and business results. This chapter produces the assessment those results depend on. It moves from the business plan to required capabilities, then to strengths and constraints, then to evidence about delivery and knowledge, and finally to a feasible transition. It stops at a finding. The organizational response to that finding is the subject of the chapter [Trace the Work: Headcount Is Not Capacity](#fix-decisions-before-hiring); the choice among implementations is the subject of the chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design).

{id: can-the-team-deliver--translate-the-business-plan-into-required-capabilities}
## Translate the Business Plan Into Required Capabilities

A **valuation** estimates what the business or an ownership stake in it is worth. The investor’s explanation of why the investment should succeed, its **investment thesis**, tells the technology team which assumptions need investigation. Neither is a design specification. The chapter [Understand Valuation: An Estimate, Not a Fact](#valuation-is-an-estimate) introduces the financial terms.

If the case depends on growth, as Larkspur’s does, the product may need cheaper experiments, entry into another market, or faster **onboarding**, the work of setting up new customers so they can use the product. For the second country, the required capability is concrete: invoice customers, which means sending them bills, under that country’s tax and pricing rules; contract with them under its law; support them in their language; and onboard them without the manual setup that already limits the first country.

Useful technical work could take several forms. Larkspur might keep country rules in a distinct part of the software. It might buy a system and handle the rules through **configuration**, which means changing settings rather than writing new code. It might make those settings safer to change, or improve **deployment**, the process of releasing software so people can use it. An expensive redesign that delays customer learning can defeat the purpose even if it promises more flexibility later.

The case may instead emphasize **EBITDA**: earnings before interest, taxes, depreciation and amortization. Earnings means profit, what is left of sales after expenses. EBITDA is a profit measure that leaves four things out:

- **interest**, the cost of borrowing;
- **taxes** on the company’s profit, which are not the sales taxes on customer invoices discussed above;
- **depreciation**, the accounting charge that spreads the cost of a physical asset, such as a server, over the years it is used;
- **amortization**, the same kind of charge for an asset you cannot touch, such as purchased or internally built software.

What remains is roughly sales minus the day-to-day costs of running the business. A case built on EBITDA therefore directs management toward sustainable operating costs: removing unused infrastructure, automating support work, retiring duplicate systems.

EBITDA is not cash, and a higher figure does not show that a project can be paid for. Two accounting treatments of software development spending explain why. Development spending that is **expensed** is recorded as an operating expense, one of the day-to-day running costs, and reduces EBITDA in the period it is recognized. Development spending that is **capitalized** is recorded as an asset, which accounting rules allow only for work that meets their conditions. Its cost then reaches expenses over later years as amortization, which EBITDA leaves out. A replacement whose costs are capitalized can therefore leave EBITDA looking healthy while it consumes cash. Either way, the money left the bank account when the people and suppliers were paid. The case must show transition spending and continued product development in cash, and say which costs are expensed and which are capitalized.

These priorities overlap. Reliable deployment reduces both the cost of failure and the time needed to experiment. A useful assessment describes the capability required and the trade-offs, rather than picking a technology from the financial target.

![A business need, faster onboarding of customers, points to the two parts of the system that limit it, configuration and billing, before three options are compared: a small change, a staged replacement or a full replacement.](private-techuity/posts/11-can-the-team-deliver/assets/images/11-can-the-team-deliver/business-need-to-system-choice.jpeg)

**Figure 1:** *Start with the constraint the company needs to remove, then compare ways to remove it.*

{id: can-the-team-deliver--start-with-a-constraint-not-a-score}
## Start With a Constraint, Not a Score

A generic technical review of Larkspur might report **tight coupling**: parts of the system depend on one another so closely that changing one means changing others. The finding the plan needs is sharper. Larkspur’s country rules (its tax rates, pricing and invoice formats) live inside the invoicing **module**, the part of the software responsible for preparing customer bills. Three other things read the rules from that same place: the tool that generates customer contracts, the software the support team uses, and the product configuration that defines what each customer gets. Market entry therefore depends on coordinated changes to billing, legal work, support and product configuration. Engineering can change the software; it can’t complete the legal and support work on its own.

The constraint could justify significant technical change. It doesn’t establish that the whole system should be replaced. Compare the smallest coherent options that support the business need, including the possibility that the market-entry plan itself is premature.

Assessment should also **record strengths**. Larkspur’s scheduling core, the central part of the product that customers use to plan their work, is stable, with few **incidents**, meaning disruptions to the live service. The team knows its customers’ operations in detail. One deployment path releases weekly without disruption. An assessment report that lists only defects encourages a new owner to dismantle capabilities it doesn’t yet understand.

{id: can-the-team-deliver--technical-debt-is-a-decision-about-future-work}
## Technical Debt Is a Decision About Future Work

**Technical debt** describes future effort or risk created by earlier technical choices or postponed work. It’s a metaphor, not money owed to a lender, and it becomes less useful when every disliked design choice is included without a connection to work the company needs to perform.

Describe an important item through its consequences: which changes become slower, which incidents become more likely, what knowledge is scarce, and what the options cost. Avoid calculating a total “debt balance” by adding estimates with incompatible assumptions. The obligation doesn’t have to sit in code the company wrote. A heavily customized supplier system, an ageing integration layer (the software that connects other systems) or a version no longer supported creates the same kind of future work.

The invoicing module is the item that matters for the second country. It is fragile enough that the same two specialists review every pricing change, and a change takes about three weeks from request to running in **production**, the live system customers use. The second country’s tax and pricing rules will go through that same module and that same queue. If the growth plan also depends on frequent pricing experiments, three weeks per change slows the company’s learning about what customers will pay: each experiment takes about three weeks to reach customers, and results can come only after that. If pricing will stay stable, the more urgent problem is that those two people are the only ones who understand the module. What needs to improve depends on the plan.

Addressing technical debt competes with other engineering investments. That doesn’t mean it should always lose. Its case should include avoided disruption, lower change cost and preserved options, with uncertainty stated. “We must modernize” is weaker than “the second country’s rules cannot be added without the two people who also handle every production problem.”

{id: can-the-team-deliver--evidence-about-delivery-and-knowledge}
## Evidence About Delivery and Knowledge

**Engineering effectiveness** means the ability to deliver useful, reliable work and sustain that ability. The SPACE research framework examines several dimensions of developer productivity: satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. Its paper argues that developer productivity can’t be represented by a single activity measure or dimension. [S13: SPACE framework](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/)

This matters when an investor asks whether a company has too many engineers. Dividing **headcount**, the number of employees, by **revenue**, the income recorded from sales, gives a staffing-to-sales ratio: people per euro of sales. It says nothing about what those people are paid or what they deliver. It is neither a cost measure nor a measure of effectiveness.

**DORA**, short for DevOps Research and Assessment, is a long-running research program on software delivery and organizational performance. It provides another perspective. Its metrics guidance, consulted in September 2026, uses five delivery metrics and emphasizes the context of the application or service being measured. It warns against comparing unlike services and against **gaming** a metric, which means changing behavior to improve the score without improving the result. [S14: DORA metrics guide](https://dora.dev/guides/dora-metrics/) An investor comparing the companies it owns, its portfolio, should not rank a bank’s payment service, which is regulated and moves customers’ money, against a newly launched marketing application without explaining the difference.

Two lead-time measures are easy to confuse, and comparisons go wrong when they are mixed. Think of them as two clocks. **DORA change lead time** starts when a developer **commits** a change, which means recording the code change in the team’s shared version history, kept by a version control system. It stops when the change is running in production. **End-to-end work lead time** starts earlier and stops when customers can use the change. This book starts it when the change is requested; some teams start it when work begins. With this book’s request-based start, the measure includes deciding and waiting before work begins, as well as building and release. A clock that starts when work begins leaves that earlier time out. Name the start and end points whenever a number is quoted.

For Larkspur’s pricing changes, the DORA clock shows under two days and the end-to-end clock shows about three weeks. Most of the elapsed time therefore falls outside commit-to-production.

The difference does not say what that time is made of. Work before a commit includes building the change as well as approvals and queues, so the gap does not prove that the change was waiting. A step-by-step trace of one recent pricing or country change is needed to separate approvals, waiting for the specialists and the building itself. The chapter [Trace the Work: Headcount Is Not Capacity](#fix-decisions-before-hiring) supplies that trace and uses it as the evidence for its diagnosis.

Interviews help explain **telemetry**, the records and measurements collected from systems. A long end-to-end lead time may reflect a shared approval queue, unclear product decisions, an unreliable **test environment**, a separate setup used to check changes before customers receive them, or implementation that is slow because the code is hard to change. Adding developers helps only when their skills and responsibilities address the diagnosed constraint. New people do not automatically fix unclear decisions, a slow approval queue or an unreliable test environment, and code that is hard to change slows a newcomer too.

Where most delivery is configuring and integrating supplier systems rather than writing software, DORA’s particular measures may not apply, but the questions behind them survive: how long a needed change waits, how often it causes disruption, and how much depends on a single supplier or a single person.

{id: can-the-team-deliver--a-replacement-needs-a-funded-transition}
## A Replacement Needs a Funded Transition

One option a broad review might propose is to replace the central billing and configuration software, called the core below, so that adding a country’s rules becomes a matter of changing settings. Any such proposal must account for the period in which old and new systems coexist. This applies whether the company is rewriting software it owns, replacing a core supplier system or moving to a different large software platform. The cost categories are shared: additional capacity, **parallel running** (operating the old and new systems at the same time) and **migration** (moving customers and their data across, including the unusual cases, called exceptions, that have to be handled by hand). When the system is bought, the supplier contracts, the rights to end them and the supplier’s own timetable also matter, and they need their own line in the plan.

For this fictional estimate, Alex costs the replacement over eighteen months. Month one is the month the work is funded and the additional people start. No such funding has been approved.

| Transition cost | € |
| --- | ---: |
| Additional engineering capacity, 4 people × 18 months | 900,000 |
| Running both platforms in parallel, months 7–18 | 240,000 |
| Customer data migration and exception handling | 160,000 |
| **Total additional transition spending, before subtracting savings or extra receipts** | **1,300,000** |

These are additional cash requirements: money paid on top of what Larkspur already spends. Existing payroll (employee pay) and maintenance stay in the operating baseline, the spending that continues with or without the project. If current employees do some of the work, distinguish their capacity commitment from extra cash spending so their pay isn’t counted twice. The total is also gross. It is stated before subtracting benefit offsets, the savings or extra customer receipts the new system later brings.

The total is not all spent before the first benefit. The spending is spread over eighteen months. If the country rules move to the new core first, and if the legal and support work is ready, the second country could send its first invoices from the new core around month twelve at the earliest. That is a provisional milestone, not a delivery commitment. The eighteen-month clock starts only when funding starts, so this route leaves no margin against the board’s proposed twelve-month date. An invoice is also not yet cash: the money arrives when customers pay.

How much cash has left the bank by month twelve depends on when payments fall due, so the estimate needs payment assumptions. Alex assumes the four additional people cost €50,000 a month in total, paid monthly from month one. Parallel running costs €20,000 a month, paid monthly in months 7–18. Nothing is paid in advance.

On those assumptions, and excluding migration, about €720,000 would have been paid by the end of month twelve. That is twelve of the eighteen months of extra people (€600,000) plus six of the twelve months of parallel running (€120,000). A different payment schedule changes the figure. If a supplier required the whole €240,000 for parallel running at the start of month seven, the month-twelve amount would be €840,000, although the eighteen-month total would stay the same.

Migration costs come on top as customers move; their timing is not yet planned. The maintenance saving arrives only after the old core is retired. A plan should show these dates and amounts, not a single total.

The annual model in the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget) leaves €0.5 million after its stated payments. That doesn’t establish whether a transition costing €1.3 million over eighteen months can be funded; the two examples use separate assumptions. Alex and Sam, Larkspur’s finance leader, need a dated spending plan, the cash actually available in each period, and any additional financing, meaning money raised from lenders or investors. Staging the work, deferring it or seeking new funding each has consequences to compare before approval.

The plan should define which capability migrates first, how value appears before the whole program is complete, and what happens if the program stops. A staged approach is useful only if intermediate states can operate safely. Dividing an inseparable replacement into nominal phases doesn’t reduce the underlying risk. Also identify **the retirement condition**: if customers remain indefinitely on the old product, the expected maintenance saving never arrives; if forced migration loses valuable customers, the lost customers could cost more than the saving.

![The current and new systems run side by side while data migration, customer support and training take place; the old system retires only after a readiness check, and bands for cash and team capacity run underneath for the whole period. The bands carry no amounts or dates.](private-techuity/posts/11-can-the-team-deliver/assets/images/11-can-the-team-deliver/fund-the-system-overlap.jpeg)

**Figure 2:** *The investment includes the path to the new system and the cost of keeping customers served along the way.*

Match the commitment to the next funding decision. Suppose demand in the second country is untested and the next funding decision is nine months away. The right commitment may then be a small trial with explicit limits. Larkspur would build a **bounded interface**: a small, limited connection that lets a handful of trial customers in the new country be invoiced under their own rules, kept separate, while the existing billing system keeps running unchanged for everyone else. The trial has known limits and a review after actual use. Starting the replacement instead would consume the time needed to learn whether the market matters.

Now suppose funding is already committed to a proven expansion. The temporary interface then becomes a bottleneck, the point that holds everything else up. Larkspur has to cost a setup it can reuse for many customers and further countries. Funding uncertainty can justify limiting scope. It doesn’t justify hiding the cost of completing or safely maintaining the result.

One more question belongs in the assessment. Suppose a parent company, one that owns Larkspur along with other businesses, mandates a group standard: a billing platform, a cloud provider (a supplier of rented computing services) or a release toolchain (the tools used to build, test and release software). What constraints does that create for this plan, and who pays for meeting the standard? Which decisions are made once for a whole group and which stay with the business is one of the questions **enterprise architecture** exists to answer. The integration-depth trade-off is developed in the chapter [Plan Acquisitions and Separations: Account for Extra Work, Not Just Expected Value](#acquisition-adds-work-first), and its design consequences in the chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design).

{id: can-the-team-deliver--the-finding}
## The Finding

The assessment ends in a compact finding that the next two chapters use. Every figure in it is fictional.

| Element | Second-country plan |
| --- | --- |
| Required capability | Invoice, contract with, support and onboard customers in a second country under that country’s tax and pricing rules, with first paying customers proposed within twelve months. |
| Current evidence | Country rules live in the invoicing module and are read by the contract-generation tool, support tooling and product configuration. The last four pricing changes each took about three weeks end to end; commit-to-production time was under two days. The same two specialists review every change and also handle production problems. |
| Preserved strength | A stable scheduling core with few incidents, deep knowledge of customers’ operations, and one deployment path that releases weekly without disruption. |
| Constraint | Market entry depends on coordinated changes to billing, legal work, support and product configuration, because the country rules are coupled into the invoicing module that all four read; every engineering change to those rules passes through the same two specialists and takes about three weeks end to end. |
| Uncertainty | Demand in the second country is untested. How the three weeks divide between approvals, the specialists’ queue and implementation has not been traced, so the share that is knowledge, decision or capacity is unknown. Whether existing customers would accept a migration if the core were replaced is unknown. |
| Transition resources | **Cost:** full replacement, about €1.3 million of additional spending over eighteen months, counted from the month the work is funded and before subtracting savings or extra receipts. **Paid by month twelve:** about €720,000, excluding migration. This assumes even monthly payments for the additional people and for parallel running, and nothing paid in advance. **First benefit:** month twelve is the provisional earliest date for first invoices from the new core, and only if the country rules move first and the legal and support work is ready. **Approval status:** nothing is funded yet, and the board has not set a cash limit. The retirement condition is unresolved. **Alternatives:** two smaller options, described below the table, have not yet been costed against the same date and cash limit. **Scarce capacity in every option:** the two specialists. |

The two smaller options named in the last row are these. One is a bought tax-and-billing service configured for the country. The other is a company-owned boundary: Larkspur separates the country rules into a part of its own software that it maintains, while the rest of billing keeps running.

The finding tells the board what the plan assumes that is not yet true, and gives the people who choose the response something to choose against. Company engineers need to take part in the diagnosis; their knowledge of the system is part of the capability the plan depends on, and an assessment that treats their explanations as resistance loses the information needed to make the investment work.

The next question is why a small country change takes three weeks when commit-to-production takes under two days, and how much of that is approvals, the two specialists’ queue or implementation. The chapter [Trace the Work: Headcount Is Not Capacity](#fix-decisions-before-hiring) answers it by tracing one of these pricing changes from request to production, and decides whether Larkspur should change roles, hire, or both. Only then should Larkspur choose among configuring a supplier, drawing a boundary it owns around the country rules and replacing the core; the chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design) makes that choice against this same finding.

{id: can-the-team-deliver--questions-to-consider}
## Questions to Consider

1. *What does your company’s business plan require the technology and the team to do, at what scale, with what reliability, and have you written that down before assessing the systems?*
2. *For the constraint that most limits your plan, have you separated the end-to-end work lead time from the commit-to-production time, traced where the rest of the time goes, and separated the smallest coherent options from a full replacement?*
3. *What strengths in your current systems and team would a report listing only defects fail to record?*
4. *If a replacement is proposed, when does its first benefit appear, what is the retirement condition, and who funds the months in between?*

{id: can-the-team-deliver--to-probe-further}
## To Probe Further

- **[The WyCash Portfolio Management System](https://c2.com/doc/oopsla92.html)** — Ward Cunningham, experience report at the OOPSLA conference (Object-Oriented Programming, Systems, Languages and Applications), 1992.  
  *The two paragraphs where the debt metaphor was first written down, with a narrow meaning close to this chapter's definition of debt as deliberately deferred future work.*
- **[Managing Technical Debt: Reducing Friction in Software Development](https://www.informit.com/store/managing-technical-debt-reducing-friction-in-software-9780135645932)** — Philippe Kruchten, Robert Nord and Ipek Ozkaya, Addison-Wesley (Software Engineering Institute Series), 2019.  
  *A book-length method for describing debt items by their consequences and costing the work to fix them, which supplies the working format behind this chapter's invoicing-module example.*
- **[Things You Should Never Do, Part I](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)** — Joel Spolsky, 2000.  
  *The best-known argument against rewriting from scratch, and the case that any replacement proposal in this chapter's terms has to answer before it is funded.*
- **[Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html)** — Martin Fowler, 2004, revised 2024.  
  *The pattern behind this chapter's advice that a staged transition only works if each intermediate state can operate safely and deliver value on its own.*
- **[Enterprise Architecture as Strategy: Creating a Foundation for Business Execution](https://store.hbr.org/product/enterprise-architecture-as-strategy-creating-a-foundation-for-business-execution/8398)** — Jeanne Ross, Peter Weill and David Robertson, Harvard Business School Press, 2006.  
  *Frames group-level architecture as a choice of what to standardize and integrate across business units, which is the group-standard question this chapter asks the assessment to include.*
