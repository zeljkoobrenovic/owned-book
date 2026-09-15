{id: can-the-team-deliver}
# 12. Can the Software and the Team Deliver What Was Promised?

![Can the Software and the Team Deliver What Was Promised? — logo](private-techuity/posts/09-can-the-team-deliver/assets/images/09-can-the-team-deliver/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to assess whether the software and the team can deliver the plan, and produce a finding that names the binding constraint, the evidence and the cost of a transition.

> **WHY INVESTORS CARE:** The investment case assumes the systems and team can support the plan; an assessment that finds the binding constraint early lets the investor reprice or resequence rather than discover it in a missed milestone.

> **WHY YOU SHOULD CARE:** If the investment plan assumes a country launch before the systems have been assessed, the assessment tests whether the date and budget are credible, and gives the board its first grounded view of what the plan will cost and when it can arrive.

> **KEY POINTS:**
>
> * Begin with **what the plan requires the company to do**. Name the changes, scale and reliability the business plan needs before judging any system.
> * Judge the technology and the team by **their consequences for that work**, and record strengths as well as constraints. An old system is not, by itself, a bad investment; a fashionable one is not a good one.
> * End with **a finding the next decisions can use**: the binding constraint, the evidence behind it, what is uncertain, and what a transition would cost before its first benefit appears.

Larkspur, the fictional scheduling-software company, plans to serve customers in a second country. The board’s plan proposes the first paying customers there within twelve months. Its software assumes one set of tax and pricing rules, its contracts cover one market, and its support team works in one language. Which changes are needed before expansion can succeed?

The expansion date has been proposed before the dependencies were assessed. That is the condition this chapter starts from, and it is a common one: an investor’s growth assumption or a board’s plan can fix a destination and a timetable before anyone has examined the technology closely. It does not make the plan wrong. It changes the order of the work. Alex’s task is to establish what the systems and the team can support, what must change in the plan, and what changing it would cost, before the company commits money or a customer promise.

Answering that takes more than a look at the software. It takes a view of what the technology and the people who run it can currently do, what changing them would cost, and how much of that can be known before committing. The systems may be built in-house, bought from suppliers or assembled from both; the assessment is the same.

[The Chain From Roadmap to Revenue Breaks Easily](#roadmap-to-revenue) connected a proposed change to customer and business results. This chapter produces the assessment those results depend on: from the business plan to required capabilities, to strengths and constraints, to evidence about delivery and knowledge, to a feasible transition. It stops at a finding. The organizational response to that finding is [Fix the Decision Problem Before Adding People](#fix-decisions-before-hiring); the choice among implementations is [Turn “We Expect Growth” Into a Design Decision](#growth-into-design).

{id: can-the-team-deliver--translate-the-business-plan-into-required-capabilities}
## Translate the Business Plan Into Required Capabilities

A **valuation** estimates what the business or an ownership interest is worth. The investor’s explanation of why the investment should succeed, its **investment thesis**, tells the technology team which assumptions need investigation. Neither is a design specification. [A Valuation Is an Estimate, Not a Fact](#valuation-is-an-estimate) introduces the financial terms.

If the case depends on growth, as Larkspur’s does, the product may need cheaper experiments, faster onboarding or entry into another market. For the second country, the required capability is concrete: invoice customers under that country’s tax and pricing rules, contract with them under its law, support them in their language, and onboard them without the manual setup that already limits the first country. Useful technical work might keep country rules in a distinct part of the software, configure them in a system the company buys, make those settings safer to change, or improve **deployment**, the process of releasing software so people can use it. An expensive redesign that delays customer learning can defeat the purpose even if it promises more flexibility later.

If the case emphasizes **EBITDA**, earnings before interest, taxes, depreciation and amortization, management may focus on sustainable operating costs: removing unused infrastructure, automating support work, retiring duplicate systems. The case must still show transition spending and continued product development, including which costs are expensed and which are capitalized. EBITDA alone doesn’t show the cash requirement.

These priorities overlap. Reliable deployment reduces both the cost of failure and the time needed to experiment. A useful assessment describes the capability required and the trade-offs, rather than picking a technology from the financial target.

![A business need becomes capability requirements before the company compares technical options.](private-techuity/posts/09-can-the-team-deliver/assets/images/09-can-the-team-deliver/business-need-to-system-choice.jpeg)

**Figure 1:** *Start with the constraint the company needs to remove, then compare ways to remove it.*

{id: can-the-team-deliver--start-with-a-constraint-not-a-score}
## Start With a Constraint, Not a Score

A generic technical review of Larkspur might report **tight coupling**: parts of the system depend on one another so closely that changing one means changing others. The finding the plan needs is sharper. Larkspur’s country rules, its tax rates, pricing and invoice formats, live inside the invoicing module, and contracts, support tooling and product configuration all read them from there. Market entry therefore depends on coordinated changes to billing, legal work, support and product configuration. Engineering can change the software; it can’t complete the legal and support work on its own.

The constraint could justify significant technical change. It doesn’t establish that the whole system should be replaced. Compare the smallest coherent options that support the business need, including the possibility that the market-entry plan itself is premature.

Assessment should also **record strengths**. Larkspur’s scheduling core is stable, with few incidents; the team knows its customers’ operations in detail; one deployment path releases weekly without disruption. A diligence report that lists only defects encourages a new owner to dismantle capabilities it doesn’t yet understand.

{id: can-the-team-deliver--technical-debt-is-a-decision-about-future-work}
## Technical Debt Is a Decision About Future Work

**Technical debt** describes future effort or risk created by earlier technical choices or postponed work. It’s a metaphor, not money owed to a lender, and it becomes less useful when every disliked design choice is included without a connection to work the company needs to perform.

Describe a material item through its consequences: which changes become slower, which incidents become more likely, what knowledge is scarce, and what the options cost. Avoid calculating a total “debt balance” by adding estimates with incompatible assumptions. The obligation doesn’t have to sit in code the company wrote. A heavily customized supplier system, an ageing integration layer or a version no longer supported creates the same kind of future work.

The invoicing module is the item that matters for the second country. A **module** is a part of the software with a particular responsibility; this one is fragile enough that the same two specialists review every pricing change, and a change takes about three weeks from request to running in production. The second country’s tax and pricing rules will go through that same module and that same queue. If the growth plan also depends on frequent pricing experiments, three weeks per change stops the company from learning what customers will pay. If pricing will stay stable, the more urgent problem is that those two people are the only ones who understand the module. What needs to improve depends on the plan.

Addressing technical debt competes with other engineering investments. That doesn’t mean it should always lose. Its case should include avoided disruption, lower change cost and preserved options, with uncertainty stated. “We must modernize” is weaker than “the second country’s rules cannot be added without the two people who also handle every production problem.”

{id: can-the-team-deliver--evidence-about-delivery-and-knowledge}
## Evidence About Delivery and Knowledge

**Engineering effectiveness** means the ability to deliver useful, reliable work and sustain that ability. The SPACE research framework examines several dimensions of developer productivity: satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. Its paper argues that developer productivity can’t be represented by a single activity measure or dimension. [S13: SPACE framework](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/) This matters when an investor asks whether a company has too many engineers. Headcount divided by revenue is a cost ratio, not a measure of effectiveness.

**DORA**, the research program on software delivery and organizational performance, provides another perspective. Its metrics guidance, consulted in September 2026, uses five delivery metrics and emphasizes application or service context. It warns against disparate comparisons and metric gaming. [S14: DORA metrics guide](https://dora.dev/guides/dora-metrics/) A portfolio benchmark should not rank a regulated transactional service against a newly launched marketing application without explaining the difference.

Two lead-time measures are easy to confuse, and benchmarking goes wrong when they are mixed. **DORA change lead time** runs from a change being committed to version control until it is running in production. **End-to-end work lead time** runs from the moment a change is requested or started until customers can use it, and includes every wait before the commit. Name the start and end points whenever a number is quoted. For Larkspur’s pricing changes, the DORA change lead time is under two days; the end-to-end work lead time is about three weeks. Most of the elapsed time therefore falls outside commit-to-production. The difference does not say what that time is made of: work before a commit includes implementation as well as approvals and queues, and the DORA measure only starts once the code is committed. A trace of one recent pricing or country change is needed to distinguish approvals, specialist queues and implementation. [Fix the Decision Problem Before Adding People](#fix-decisions-before-hiring) supplies that trace and uses it as the evidence for its diagnosis.

Interviews help explain **telemetry**, the records and measurements collected from systems. A long end-to-end lead time may reflect a shared approval queue, unclear product decisions, an unreliable **test environment**, a separate setup used to check changes before customers receive them, or implementation that is slow because the code is hard to change. More developers resolve only the last of those, and not always that one. Where most delivery is configuring and integrating supplier systems rather than writing software, DORA’s particular measures may not apply, but the questions behind them survive: how long a needed change waits, how often it causes disruption, and how much depends on a single supplier or a single person.

{id: can-the-team-deliver--a-replacement-needs-a-funded-transition}
## A Replacement Needs a Funded Transition

One option a broad review might propose is to replace the billing and configuration core so that country rules become configuration. Any such proposal must account for the period in which old and new systems coexist. This applies whether the company is rewriting software it owns, replacing a core supplier system or moving to a different enterprise platform. The cost categories are shared, additional capacity, parallel running and migration, but the contracts, exit rights and vendor timing differ when the system is bought, and they need their own line in the plan.

For this fictional estimate, Alex costs the replacement over eighteen months:

| Transition cost | € |
| --- | ---: |
| Additional engineering capacity, 4 people × 18 months | 900,000 |
| Running both platforms in parallel, months 7–18 | 240,000 |
| Customer data migration and exception handling | 160,000 |
| **Total transition spending before benefit offsets** | **1,300,000** |

These are additional cash requirements; existing payroll and maintenance stay in the operating baseline. If current employees do some of the work, distinguish their capacity commitment from extra cash spending so their pay isn’t counted twice. The total is not “before any benefit”: the spending is spread over eighteen months, and if the country-rules capability migrates first, the second country could invoice from the new core around month twelve, while the maintenance saving arrives only after the old core is retired. A plan should show both dates, not a single total.

The annual model in [Find the Cash Behind Your Technology Budget](#obligations-before-budget) leaves €0.5 million after its stated payments. That doesn’t establish whether a transition costing €1.3 million over eighteen months can be funded; the two examples use separate assumptions. Alex and Sam need a dated spending plan, available cash balances and any additional financing. Staging the work, deferring it or seeking new funding each has consequences to compare before approval.

The plan should define which capability migrates first, how value appears before the whole program is complete, and what happens if the program stops. A staged approach is useful only if intermediate states can operate safely. Dividing an inseparable replacement into nominal phases doesn’t reduce the underlying risk. Also identify **the retirement condition**: if customers remain indefinitely on the old product, the expected maintenance saving never arrives; if forced migration loses valuable customers, the saving may be economically negative.

![Old and new systems run together during migration, requiring cash and people until the old system can safely retire.](private-techuity/posts/09-can-the-team-deliver/assets/images/09-can-the-team-deliver/fund-the-system-overlap.jpeg)

**Figure 2:** *The investment includes the path to the new system and the cost of keeping customers served along the way.*

Match the commitment to the next funding decision. If demand in the second country is untested and the next funding decision is nine months away, a bounded interface that allows a small customer trial, with known limits and a review after actual use, may be the right commitment; starting the replacement would consume the time needed to learn whether the market matters. If funding is already committed to a proven expansion, the temporary interface becomes a bottleneck and the repeatable capability has to be costed. Funding uncertainty can justify limiting scope. It doesn’t justify hiding the cost of completing or safely maintaining the result.

One more question belongs in the assessment. If a parent company or a group standard mandates a billing platform, a cloud provider or a release toolchain, what constraints does that create for this plan, and who funds compliance? Which decisions are made once for a whole group and which stay with the business is one of the questions **enterprise architecture** exists to answer. The integration-depth trade-off is developed in [An Acquisition Adds Work Before It Adds Value](#acquisition-adds-work-first), and its design consequences in [Turn “We Expect Growth” Into a Design Decision](#growth-into-design).

{id: can-the-team-deliver--the-finding}
## The Finding

The assessment ends in a compact finding that the next two chapters use. Every figure in it is fictional.

| Element | Second-country plan |
| --- | --- |
| Required capability | Invoice, contract with, support and onboard customers in a second country under that country’s tax and pricing rules, with first paying customers within twelve months. |
| Current evidence | Country rules live in the invoicing module and are read by contracts, support tooling and product configuration. The last four pricing changes each took about three weeks end to end; commit-to-production time was under two days. The same two specialists review every change and also handle production problems. |
| Preserved strength | A stable scheduling core with few incidents, deep knowledge of customers’ operations, and one deployment path that releases weekly without disruption. |
| Constraint | Market entry depends on coordinated changes to billing, legal work, support and product configuration, because the country rules are coupled into the invoicing module that all four read; every engineering change to those rules passes through the same two specialists and takes about three weeks end to end. |
| Uncertainty | Demand in the second country is untested. How the three weeks divide between approvals, the specialists’ queue and implementation has not been traced, so the share that is knowledge, decision or capacity is unknown. Whether existing customers would accept a migration if the core were replaced is unknown. |
| Transition resources | Full replacement: about €1.3m of additional cash over eighteen months, first benefit around month twelve, retirement condition unresolved. Smaller options, a bought tax-and-billing service configured for the country or a company-owned boundary around the country rules, have not yet been costed against the same date and cash limit. Scarce capacity in every option: the two specialists. |

The finding tells the board what the plan assumes that is not yet true, and gives the people who choose the response something to choose against. Company engineers need to take part in the diagnosis; their knowledge of the system is part of the capability the plan depends on, and an assessment that treats their explanations as resistance loses the information needed to make the investment work.

The next question is why a small country change takes three weeks when commit-to-production takes under two days, and how much of that is approvals, the two specialists’ queue or implementation. [Fix the Decision Problem Before Adding People](#fix-decisions-before-hiring) answers it by tracing one of these pricing changes from request to production, and decides whether Larkspur should change roles, hire, or both. Only then should Larkspur choose among configuring a supplier, drawing a boundary it owns around the country rules and replacing the core; [Turn “We Expect Growth” Into a Design Decision](#growth-into-design) makes that choice against this same finding.

{id: can-the-team-deliver--questions-to-consider}
## Questions to Consider

1. *What does your company’s business plan require the technology and the team to do, at what scale, with what reliability, and have you written that down before assessing the systems?*
2. *For the constraint that most limits your plan, have you separated the end-to-end work lead time from the commit-to-production time, traced where the rest of the time goes, and separated the smallest coherent options from a full replacement?*
3. *What strengths in your current systems and team would a report listing only defects fail to record?*
4. *If a replacement is proposed, when does its first benefit appear, what is the retirement condition, and who funds the months in between?*

{id: can-the-team-deliver--to-probe-further}
## To Probe Further

- **[The WyCash Portfolio Management System](https://c2.com/doc/oopsla92.html)** — Ward Cunningham, OOPSLA experience report, 1992.  
  *The two paragraphs where the debt metaphor was first written down, with a narrow meaning close to this chapter's definition of debt as deliberately deferred future work.*
- **[Managing Technical Debt: Reducing Friction in Software Development](https://www.informit.com/store/managing-technical-debt-reducing-friction-in-software-9780135645932)** — Philippe Kruchten, Robert Nord and Ipek Ozkaya, Addison-Wesley (SEI Series), 2019.  
  *A book-length method for describing debt items by their consequences and costing remediation, which supplies the working format behind this chapter's invoicing-module example.*
- **[Things You Should Never Do, Part I](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)** — Joel Spolsky, 2000.  
  *The best-known argument against rewriting from scratch, and the case that any replacement proposal in this chapter's terms has to answer before it is funded.*
- **[Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html)** — Martin Fowler, 2004, revised 2024.  
  *The pattern behind this chapter's advice that a staged transition only works if each intermediate state can operate safely and deliver value on its own.*
- **[Enterprise Architecture as Strategy: Creating a Foundation for Business Execution](https://store.hbr.org/product/enterprise-architecture-as-strategy-creating-a-foundation-for-business-execution/8398)** — Jeanne Ross, Peter Weill and David Robertson, Harvard Business School Press, 2006.  
  *Frames group-level architecture as a choice of what to standardize and integrate across business units, which is the group-standard question this chapter asks the assessment to include.*
