{id: decide-who-decides}
# 8. Clarify Authority: Decide Who Decides Before You Disagree

![Clarify Authority: Decide Who Decides Before You Disagree — logo](private-techuity/posts/06-decide-who-decides/assets/images/06-decide-who-decides/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to fill in who proposes, approves, funds and carries out a decision, and plan what happens when the approval does not arrive in time.

> **WHY INVESTORS CARE:** An investor that negotiated the right to approve certain company decisions did so precisely so that those decisions would come to it. An adviser’s remark treated as an instruction bypasses that agreed process. An approval that is never recorded leaves the investor exposed to a plan it did not authorize.

> **WHY YOU SHOULD CARE:** A suggestion from someone close to the investor can start a project nobody approved, and an approval that never arrives can quietly turn into a delivery failure. Clear authority prevents both.

> **KEY POINTS:**
>
> * Agree **who is authorized to decide** before disagreement arises. A suggestion from someone close to the investor can sound like an instruction.
> * Fill in the record with **names, thresholds and dates**. “Management recommends, the board approves” tells nobody whom to call on a Tuesday, or by when.
> * Plan the **missed-deadline branch**. If the approval does not arrive, take the remaining options back to the person authorized to decide and tell the team which funded plan it is executing.

When a company takes on an investor, more people seem to have a say in its decisions. A new board member, an adviser from the investment firm or a lender may each make a request, and it is not always clear which requests are instructions and which are only ideas. If nobody has written down who proposes, approves, funds and carries out a decision, a passing remark can start a project that nobody approved. An approval that nobody tracks can arrive too late and quietly turn into a delivery failure.

This is a problem of **governance**: the arrangements for making decisions, overseeing them and holding people responsible. Good intentions cannot replace an agreed decision process.

**Informal influence** and **unclear delegation** exist under any ownership. Delegation is the authority a body hands to a person to decide within stated limits. A founder’s offhand remark can start a project just as easily as an adviser’s. What an investment changes is the setting in which decisions are made. It can add **board seats** (a place, and a vote, on the board, the group of directors that oversees the company on the shareholders’ behalf), **approval thresholds** (amounts above which a different approval is needed), **reserved matters** (decisions that require a specified party’s approval whatever the amount) and advisers who speak, or seem to speak, for a shareholder. It is easy to give their requests **too much or too little weight**, and either mistake lands on product and engineering teams. Establish the actual authority, funding and deadline before committing.

This chapter begins Part II by examining what an investment can change about your authority and your accountability: who is answerable for a result. It establishes what has changed, shows how to write down who decides what and connects technical choices to the business outcome. It then shows how to make a conditional commitment explicit, plan for a missed deadline, report in a way that asks for a decision and disagree without evasion.

{id: decide-who-decides--setting-up-the-example-a-remark-over-coffee}
## Setting Up the Example: A Remark Over Coffee

Larkspur, the fictional scheduling-software company this book follows, has a new **shareholder**: an investor that now owns part of the company. The cast is fictional. Ines is Larkspur’s chief executive officer (**CEO**), who runs the company and answers to the board. Alex is its chief technology officer (**CTO**), the executive who leads its technology work. Sam is its chief financial officer (**CFO**), who runs its finances, and Priya is its product leader, who decides what the product should do next. Morgan is the **investor’s technology adviser**, the role this book calls the Technology Principal: employed by the investment firm to assess and advise on technology, not to run the company’s technology. Their titles describe their work, but their actual approval rights must still be agreed.

Morgan mentions over coffee that Larkspur should probably change its cloud provider. Alex hears the remark as an instruction from the new shareholder and starts planning a **migration**: moving Larkspur’s systems to another supplier. Morgan, however, thought they were only offering an idea.

The cloud remark illustrates **the boundary of an adviser’s influence**. A separate onboarding proposal shows the **full approval process**, from a filled-in decision record to what happens when the approval it depends on is late. Later in the chapter, a rewrite of the scheduling engine, the software that works out customers’ schedules, shows how a board should **challenge a technical choice**. The first step is to establish what the investment has changed.

{id: decide-who-decides--establish-what-has-changed}
## Establish What Has Changed

**Authority** means permission to make a particular decision. New ownership can change it directly through agreed rights, or change how people expect you to exercise it. Compare the arrangements before and after the investment using actual company documents and conversations with the responsible leaders.

| Area | What to establish |
| --- | --- |
| Ownership | Who now holds **shares**, the units of ownership in the company, and which rights come with them: a seat and vote on the board, a separately agreed right to approve particular decisions, or only a share of the value? |
| Priorities | Which customer, financial or operating outcomes are now expected, and why? |
| Approval | Which hiring, spending, product or business-deal decisions need approval, from whom and by when? |
| Accountability | Who is accountable for each result, what resources have been committed and how will progress be assessed? |

Larkspur’s board has authorized Ines to approve spending up to €500,000 inside the **approved plan**, the year’s budget and the work it funds, which the board adopted (a fictional threshold).

Two kinds of decision stay with the board whatever the amount. The first is any draw on a **reserve**, money the board set aside for needs the plan did not foresee, and any change to what an approved **envelope** funds, an envelope being a fixed sum authorized for a defined bundle of work: Ines spends inside the plan, she doesn’t rewrite it. The second is a permanent hire outside the approved **headcount plan**, the list of positions the budget pays for. These are the delegation rules the rest of this chapter, and the later chapters that draw on a reserve, refer back to.

Now the cloud suggestion. No reserved matter covers the choice of cloud provider. Morgan holds no approval right; the investment firm’s rights are exercised through its seat on the board. So the suggestion is an idea for Alex to evaluate, and a migration would need Ines’s approval if it stays inside the approved plan and below her threshold, or the board’s if it exceeds the threshold or changes what the plan funds. Alex records it as an option to cost, not as a plan, and tells Morgan so.

An investment doesn’t automatically change every entry. Recording what stayed the same helps when employees are unsure whether earlier authority still applies. If you inherited the ownership arrangement, begin with the decisions ahead rather than assuming you took part in agreeing the original terms.

The investor is a **fund**, a pool of money the investment firm manages for its own backers, and the fund’s **investment committee** is the group inside the firm that approved putting the fund’s money into Larkspur. It does not approve Larkspur’s hiring plan. The company’s board and executives approve company work. Operating professionals from the investment firm, people it employs to help the companies it owns improve how they run, contribute expertise. **Lenders**, who advanced money that must be repaid, can hold contractual rights that constrain all of them; a loan agreement may, for example, forbid new borrowing without the lender’s consent.

The survey of **private equity** (**PE**) investors, firms that buy ownership stakes in companies outside the public stock markets, by Gompers and colleagues documents attention to governance, financing and value creation, that is, making the business worth more; it doesn’t establish a uniform organization chart. [S04: PE practitioner survey](https://www.nber.org/papers/w21133) KKR, a large investment firm, publicly describes Capstone, its in-house operating-support team, as working alongside its investment teams, company boards and company management: a stated delivery model, not proof that every intervention succeeds. [S22: KKR Capstone description](https://www.kkr.com/approach/capstone)

{id: decide-who-decides--write-down-who-decides-what}
## Write Down Who Decides What

Priya and Alex want to spend €1 million automating **onboarding**, the setup needed before a new customer can use the product; today Larkspur’s implementation team configures the product for each customer by hand. A customer’s **configuration** is the set of product settings that fit that customer, and the team chooses those settings one customer at a time. Their decision record looks like this:

| | Larkspur’s answer |
| --- | --- |
| Decision | Spend €1 million automating customer onboarding within the year |
| Who recommends | Priya, the product leader, with Alex, the CTO |
| Who resolves trade-offs | Ines, the CEO |
| Accountable for delivery | Priya for the onboarding work; Alex for the engineering build |
| Investor adviser’s contribution | Test whether the 80-hour implementation figure holds across customer types; supply comparable onboarding patterns |
| Whose approval is needed | The board, because the amount exceeds the €500,000 Ines is authorized to approve |
| Funding | Pending: the year’s cash plan has not yet shown where €1 million would come from |
| Response time | Two weeks: the budget cycle closes at month end |
| Evidence that would change the recommendation | Implementation effort that varies widely by customer type, which would favor a narrower first step |

This is the €1 million program discussed in the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget), not an approved commitment to spend it. The board still needs a feasible funding plan, and the chapter [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything) shows why it may fund a smaller step first.

**Escalation** means taking an unresolved issue to someone authorized to decide it. An escalation route that takes six weeks is useless for a financing deadline, a date by which money must be secured, or a service failure. Treating every architectural disagreement as an emergency fails the other way: it stops company leadership from exercising judgment.

![Four numbered cards stacked in one column, propose, approve, fund and deliver, each with one responsible role; a dashed arrow labelled advice only enters the proposal card, and the approval card shows a single formal-approval gate: the chief executive for delegated decisions, the board for reserved or larger decisions.](private-techuity/posts/06-decide-who-decides/assets/images/06-decide-who-decides/decision-rights-map.jpeg)

**Figure 1:** *One responsibility per stage. The product and technology leaders propose. The chief executive approves delegated decisions: those inside the approved plan and within her limit. The board approves reserved matters, such as a reserve draw or a hire outside the headcount plan, and anything larger. The finance leader confirms the cash and its dates. The team delivers. Advice enters the proposal, not the approval.*

Read as roles rather than names, the same record generalizes into a lookup table. The last column names the approval to verify, not the answer; where a row quotes Larkspur’s rule, that is one company’s arrangement. Adapt the table to actual company documents; it doesn’t assert that an investor’s adviser holds any of these rights.

| Decision | Company contribution | Investor adviser’s possible contribution | Approval to verify |
| --- | --- | --- | --- |
| Product priorities within an agreed budget | Product leader and CTO recommend; CEO resolves major trade-offs | Challenge assumptions and supply evidence | The executive delegation and any reserved matters |
| Material technology investment (one large enough to change the plan) | Management prepares options and the financial case: costs, benefits and risks in money terms | Test technical feasibility and delivery dependencies, the work that must be finished first | Board, shareholder or lender approvals where the agreements require them |
| CTO appointment | CEO defines the need, runs the process and recommends | Help assess candidates and context | The actual appointment authority in the agreements |
| Executive appointment (a chief product officer, a head of engineering) | CEO writes the role design, runs the selection and recommends the appointment | Introduce candidates and help assess them against the company’s design | The appointment authority, plus any reserved matter over executive officers’ hiring, dismissal or pay |
| Change to the headcount plan (hires beyond it, a freeze) | Management shows what each role delivers and what a conditional role waits for | Compare the hire with similar companies and challenge its shape | Whoever holds the headcount authority: at Larkspur, the board for hires outside the approved plan and the CEO within it |
| Staffing reduction or restructuring | Management costs the alternatives, names the work that stops and the cash by date | Comparisons from other companies, which are information rather than instruction | The board for a change to what the plan funds, any reserved matter over the **operating plan** (the year’s work and the people and money assigned to it), and employment law where the people are employed |
| Acquisition integration (combining a bought company’s operations with the buyer’s) | Executives are accountable for the integration plan | Assess sequencing, capacity and reusable support | The approvals for the purchase itself, then the company’s ordinary operating governance |

{id: decide-who-decides--several-investors-do-not-make-one-decision-maker}
## Several Investors Do Not Make One Decision-Maker

In a fictional **minority round**, a sale of new shares in which the new investors together buy less than half of the company, Larkspur’s founder keeps most of the **voting shares**, the shares that carry votes at shareholder meetings. One new investor receives a seat on the board; another receives a separately negotiated right to approve specified decisions. Alex is asked for three different versions of the hiring plan. The right response is to establish which **forum**, the meeting or body authorized to settle the choice, can approve the company’s plan and bring the alternatives there. Adding all the requests to the **roadmap**, the plan of what the product team will build next, would turn unresolved shareholder disagreement into the team’s delivery problem.

The National Venture Capital Association (NVCA), the industry body for investors in young companies, publishes separate model documents for share purchases, investor rights and voting arrangements. Its overview also describes funding released in stages, over time or when milestones are reached. This supports looking beyond an ownership percentage: rights are written into agreements, not read off a shareholding. It doesn’t establish the terms of any particular company’s agreement. [S61: NVCA model-document overview](https://nvca.org/model-legal-documents/)

With a **controlling financial sponsor**, an investment firm that owns enough of the company to control it, ask which decisions remain delegated to management and which require its approval. With a **corporate parent**, an operating company that owns this one, map the local board and executives alongside the parent’s product, security, finance and procurement functions. A company that has merely bought a minority stake in Larkspur doesn’t by itself bring that group hierarchy with it.

**Record the source of each relevant authority**, the decision threshold and the response time in language the team can use. When shareholders disagree, the board or another authorized body has to resolve the choice; what that body is, and what happens in a **deadlock**, when the required agreement cannot be reached, depends on the actual agreements. The product and engineering leader supplies the options, evidence and consequences. Shareholder disagreement can’t be resolved by silently promising incompatible work.

{id: decide-who-decides--connect-technical-choices-to-the-business-outcome}
## Connect Technical Choices to the Business Outcome

In a separate illustration, Alex proposes rewriting Larkspur’s scheduling engine because it is hard to change. The board asks how that supports growth. Alex answers that the current **stack**, the set of technologies the engine is built on, is dated. The exchange produces heat but little information.

A better challenge asks for the constrained business outcome: which customer need can’t be served, how often the constraint bites and what it costs. Alex can then compare a focused change, a staged replacement and the full rewrite. Sam can compare their **cash profiles**, how much cash each option needs and when, with the €0.5 million remaining in the annual planning example (see the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget)). The board can decide whether to fund an option and accept its risks. It hasn’t become an architecture committee, a body that designs the system; it has required the connection between an investment and the business plan to be made explicit.

The same discipline applies in reverse. “Cut engineering by 20%” isn’t a complete operating plan. Which work disappears? Which obligations remain? What happens to customer commitments and to **operational coverage**, having enough people on hand to keep the service running and answer support calls? If the decision is still to cut, record its expected consequences rather than quietly converting them into impossible delivery promises.

Requests of that kind reach a company leader in three forms that sound alike and are not.

- A **formal approval right** comes from the agreements: a reserved matter, a board seat, a right of consent over executive pay or the operating plan. The response is to bring the authorized body a decision it can take.
- A **funding condition** attaches money to a plan. Two examples: a **bridge**, short-term financing that covers a gap until longer-term funding arrives, released only once a cost plan is adopted; or a new **funding round**, a sale of new shares to investors, whose **term sheet**, the document setting out the proposed terms before the binding contracts are signed, wants a particular executive in place. The response is to translate the condition into a date and a number, and decide whether to meet it.
- **Influence** is everything else: an adviser’s **benchmark**, a comparison with similar companies, a director’s view of a leader, an introduction. The response is to record it as an option and assess it on the same evidence as any other.

The chapter [Scale the Team Up: Headcount Is Not Capacity](#fix-decisions-before-hiring) works an investor-proposed appointment through that distinction, and [Scale the Team Down: Decide What Work Stops, Not Just Who Leaves](#anatomy-of-a-layoff) a staffing reduction, where all three arrive at the same board meeting.

{id: decide-who-decides--make-a-conditional-commitment-explicit-and-plan-the-missed-deadline}
## Make a Conditional Commitment Explicit, and Plan the Missed Deadline

Back to the onboarding proposal, which shares its calendar with the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget). There, on the first day of the financial year, Ines approved a **pilot** within her delegation: a small trial that builds the reusable setup step for the common customer types and measures it on the first eight customers before more is spent. The pilot costs €180,000 to build plus €30,000 of first-year maintenance, €210,000 in all. That cash comes from what the year is expected to leave after its planned payments, together with the cash the company began the year with. The effort is twelve **engineer-weeks** of the current team. An engineer-week is one engineer’s work for one week, so twelve is three engineers for four weeks, not twelve weeks on the calendar.

The €1 million record above went to the board in the same budget round. The board answered within the two weeks. It did not approve the €1 million program in one year. It endorsed the direction, confirmed the pilot, and kept the two implementation hires as its own decision, because permanent hires outside the approved headcount plan are the board’s whatever they cost.

**The pilot, then completing the first stage.** The pilot’s step is usable from early February for the common customer types, and Priya measures the first eight customers set up with it by 1 April. Completing the first stage is the delivery Alex now has to date: adding the **templates** for the less-common customer types and moving every new customer onto the step, so that manual setup ends for new customers. A template is a reusable set of settings for one customer type; with it, setting up a new customer of that type means filling in the template rather than configuring the product from scratch. Migrating existing customers’ configurations is a second stage, priced separately in the cash chapter. The engineering build is largely done by February. What completion needs is the implementation team’s time, and that team also runs the ordinary setup queue by hand until the step covers everyone.

**What the hires change.** Alex’s estimate: with the current team, completion by January of the following year; with two implementation specialists starting in June to take over part of the setup queue, by October. The hires would cost about €175,000 for June to December and about €300,000 a year after that, recurring: well inside Ines’s €500,000 threshold, but a board decision because they add permanent headcount. The board decides them at its May meeting, on two pieces of evidence: Sam’s **collections** for the first quarter, January to March, meaning the customer payments actually received, against plan, and Priya’s 1 April report on the first eight customers. “October, subject to the hiring approval at the May meeting and two June start dates” is a decision proposal; an unconditional October promise would hide both dependencies. Approval is not the same as people: the board can say yes in May and recruitment can still miss June.

**The specialist.** One contract implementation specialist understands the current configurations, and the less-common templates depend on that knowledge. The specialist’s first-quarter engagement, which ends on 31 March, is already in this year’s operating plan. The days spent writing those configurations down for the build are allocated from that engagement and are not billed again, so they are not part of the €210,000. Alex accepts that written record, or names its gaps, by 31 March. The January plan relies on the record, not on the specialist staying.

**If the record is incomplete**, the cash chapter arranged a contingency. Ines can extend the engagement once, for one quarter at €37,500, by giving notice on or before day 100 of the financial year, which is 11 April. That is additional spending, not part of the €210,000: pilot plus extension is €247,500, before any hiring or the data-quality step discussed below. It is inside Ines’s delegation. The specialist would work from 15 April to 15 July. The cash chapter prices that quarter at €12,500 a month; this chapter assumes payment in arrears, so the three invoices fall due on 15 May, 15 June and 15 July. Ines exercises the option only if Sam’s forecast, rerun on day 100 with the actual receipts and every remaining commitment, shows cash above the reserve on each of those three payment dates. If she exercises it, the remaining templates are specified with the specialist before 15 July.

**If the option lapses**, or its cash condition fails, the implementation team specifies the remaining templates from the written record. A customer type it cannot specify stays on manual setup, its template goes to the next budget round, and Ines tells the team and the affected customers so in writing; the January date stands for every other customer type. For the third quarter, availability is asked for afresh on 30 June, not assumed; that check serves the setup-queue peak, not the templates.

**The January plan is not a hope.** Its cash is the €210,000 already authorized and identified in the cash plan: the €180,000 build covers the contractor time for the remaining templates and the tools and services the build needs, paid on the dates the cash plan gives, and the €30,000 covers the first year of maintenance. The specialist’s documentation days are not in that sum; they come from the first-quarter engagement the operating plan already pays for. Its people are the implementation team, already on payroll, and the twelve engineer-weeks Ines assigned when she approved the pilot, freed by deferring a reporting refresh to the following quarter; the displacement is written into the plan so the same weeks are not promised twice. What is unfunded is only the acceleration; the specialist extension, if the written record turns out to be incomplete, has its own €37,500 and its own cash condition, stated above.

**Now the likely failure**: the May meeting passes and the board has not decided. Alex brings the January option back to Ines and communicates the currently authorized plan. Ines can escalate to the board chair, the director who leads the board’s work and can call a decision between meetings, or confirm January. Either way the team is told, in writing, that January is the plan it is executing, with the cash and people it already has. For any promise made against the October date, Ines chooses one of three responses:

- renegotiate the promise with the customer;
- fund a contract specialist for the peak quarter from the uncommitted cash within her delegation, if the firm confirms on 30 June that one is available; or
- take the hiring back to the board.

Nobody keeps working toward October on the assumption that money will appear.

If the board approves the hires but the two have not started by the end of June, January stays the communicated date. A later start does not restore October by itself, because the October estimate assumed June starts. Once the actual start dates are known, Alex revises the delivery estimate from them, and Ines approves any replacement commitment before it is communicated; she also decides the same three questions about customer promises. If the board refuses the hires, January is the plan and the hiring question waits for the next budget round. If the specialist’s written record is incomplete on 31 March and the extension is not exercised, or the specialist is not available, the customer types that cannot be specified without that knowledge stay on manual setup and their templates go to the next budget round; the January date stands for the rest. The October date depended on the hires, not on the specialist.

Recorded, the decision reads:

| Field | Larkspur’s answer |
| --- | --- |
| Scope | Complete the first stage of onboarding automation: templates for the less-common customer types, and every new customer set up with the step |
| Chosen option | January of the following year with the current team; October if the board approves the two implementation hires at its May meeting and both start in June |
| Alternatives rejected | An unconditional October promise; contractors booked now against a hiring budget that has not been approved |
| Funding: baseline | €210,000 authorized by Ines within her delegation and identified in the cash plan: the €180,000 build (contractor template time, tools and services) paid in instalments through the year, and the €30,000 first-year maintenance charged monthly from February. The engineers, the implementation team and the specialist’s first-quarter engagement are already paid for by the operating plan and are not counted again |
| Funding: the two hires | About €175,000 this year for June to December, and about €300,000 a year recurring; a board decision |
| Funding: optional specialist extension | €37,500, additional, only if the written record is incomplete on 31 March: service from 15 April to 15 July, paid in arrears in three invoices of €12,500 due 15 May, 15 June and 15 July; within Ines’s delegation and only if Sam’s day-100 forecast shows cash above the reserve on each of those three dates |
| Accountable for delivery | Priya for the onboarding work; Alex for the engineering build and the delivery estimate |
| Staff allocation | The implementation team, on payroll; twelve engineer-weeks of the current team, already scheduled; the contract specialist’s first-quarter days, already paid for by the operating plan, including the written record of the less-common configurations that Alex accepts by 31 March, with a one-quarter extension option exercisable by notice on or before 11 April (day 100) |
| Approval contact | Ines, for the stage and the specialist extension, within her delegation; the board, for the hires |
| Conditions for October | Board approval at the May meeting, and two confirmed June start dates |
| Decision date | The May board meeting |
| Fallback | If either condition fails, or no decision is taken, January is the plan; the team is told in writing; customer promises tied to October go back to Ines for an explicit decision. If the hires start after June, Alex revises the estimate from the actual start dates and Ines approves any replacement commitment; October is not restored by itself. If the specialist’s record is incomplete and the extension is not exercised, the customer types that cannot be specified stay on manual setup and their templates go to the next budget round |
| Evidence that would change it | A signed customer commitment tied to October, which would make the hiring decision urgent rather than optional |

The whole sequence on one calendar, with the cash chapter’s day count in brackets:

1. 1 January (day 0): Ines approves the €210,000 pilot within her delegation; the €1 million record goes to the board.
2. Mid-January: the board answers. No €1 million program this year; the pilot continues; the two hires are the board’s decision at its May meeting.
3. Early February (day 35): the step is usable for the common customer types; the implementation team starts on the eight-customer group.
4. 31 March: the contract specialist’s engagement ends; Alex has accepted the written record of the less-common configurations, or named its gaps.
5. 1 April (day 90): Priya reports the eight-customer group.
6. About 10 April (around day 100): the board reviews that evidence, with the report in the next section, and decides the data-quality step; the hires stay on the May agenda.
7. 11 April (day 100): the one-quarter specialist extension option expires; if the record was incomplete, Ines has exercised it on Sam’s rerun forecast, or let it lapse.
8. May meeting: the board decides the hires, or does not.
9. June: the hires start, if approved and recruited; on 30 June the third-quarter specialist availability is confirmed or not.
10. October: the first stage is complete with the hires; or January of the following year with the current team.

![Approval, funding and capacity must be confirmed before a conditional plan becomes a delivery commitment.](private-techuity/posts/06-decide-who-decides/assets/images/06-decide-who-decides/conditional-commitment-gates.jpeg)

**Figure 2:** *Approval, funding and capacity are separate conditions. Record each one, the person who can resolve it and the decision date.*

{id: decide-who-decides--reporting-that-asks-for-a-decision}
## Reporting That Asks for a Decision

A board report should connect **material** outcomes, the ones large enough to affect a decision, with an interpretation and the decision needed. A traffic-light dashboard without an evidence trail can conceal more than it reveals: “green” might mean on time, within budget, lower risk or simply that no one has escalated a problem.

For the onboarding work, a fictional three-sentence update does the job at the board’s April review, about ten days after Priya’s 1 April report: “Across the first eight customers, implementation effort fell from 80 to 62 hours, short of the 50 we assumed, and about 40% of the remaining hours trace to customer **data quality**, records that arrive with missing fields or inconsistent formats, rather than to the product. We propose a data-quality step, €40,000 and four engineer-weeks, before deciding on further implementation hires. Decision requested: approve the €40,000 from the reserve at this meeting; the hiring decision stays with the May meeting, where the January record placed it, once Sam has closed the first quarter’s collections.”

Why does €40,000 go to the board when Ines may approve €500,000? The reserve belongs to an envelope the board approved, so drawing on it is a board decision; and the draw would fund a data-quality step the approved plan did not contain, which changes what the envelope funds. Ines’s €500,000 covers spending inside the plan, not either of those. It is the same path the chapter [Set Priorities: You Cannot Fund Everything at Once](#cannot-fund-everything) follows when its recovery retest draws on the reserve. The figures are the shared pilot record kept in the [Practical Tools for Ownership and Technology Decisions](#toolkit), which also holds the report shapes for an initiative and its outcomes. Keep reporting effort visible; a monthly questionnaire that no decision depends on consumes the capacity the shareholder wants to improve.

{id: decide-who-decides--parallel-instructions-need-one-accountable-leader}
## Parallel Instructions Need One Accountable Leader

Direct access to engineers can help during **due diligence**, the investigation an investor carries out before it invests, or during a clearly scoped support assignment. It becomes a problem when engineers receive priorities from the investor’s adviser, the CTO and the investment team, the firm’s deal professionals, at once: a second chain of command with no agreed remit and nobody answerable for the result. For any assignment, name the accountable company leader and route conflicting instructions back to that person. How an adviser’s influence and information should be used, including the boundaries of confidential coaching, is the subject of the chapter [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#investors-adviser); the written scope and rules for a support assignment are in the chapter [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement).

{id: decide-who-decides--disagreement-without-evasion}
## Disagreement Without Evasion

A leader should be able to say: “We can deliver the cost target, but not the current roadmap with it. Here are the choices.” An investor’s adviser should be able to say: “The evidence no longer supports the original **investment thesis**,” the reasoning for why the investment was expected to succeed. A board should be able to decide against a recommendation while recording what it is accepting.

A useful governance arrangement lets disagreement reach an accountable decision in time to act. The record should make clear who decided, which options were considered and what consequences were accepted.

Authority explains who can decide. It does not explain why the approver wants what they want. The next chapter reads the incentives behind the decision, what the executives’ shares (their **management equity**, the part of the company they own), the fund manager’s **carried interest** or **fund carry** (its contractual share of the fund’s investment profits) and the employees’ jobs each stand to gain or lose: [Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets).

{id: decide-who-decides--questions-to-consider}
## Questions to Consider

1. *For the most important technology decision ahead of your company, who recommends, who is authorized to decide, who funds, who implements, and by when? Can you name people rather than roles?*
2. *When an adviser from the investor makes a suggestion, how do your engineers know whether it is an idea, an assessment or an instruction?*
3. *Which of your current commitments depend on an approval or hire that has not yet arrived? Is the condition recorded, with the decision date and what happens if the date passes?*
4. *When shareholders or board members disagree, which forum resolves the choice? Are incompatible requests being carried into the team’s **backlog**, its list of work waiting to be done, instead?*

{id: decide-who-decides--to-probe-further}
## To Probe Further

- **[Who Has the D?: How Clear Decision Roles Enhance Organizational Performance](https://hbr.org/2006/01/who-has-the-d-how-clear-decision-roles-enhance-organizational-performance)** — Paul Rogers and Marcia Blenko, Harvard Business Review, January 2006.  
  *The Bain consultants' method behind this chapter's "who recommends, who decides, who implements" pattern, showing what goes wrong when several people believe they hold the decision.*
- **[Startup Boards: A Field Guide to Building and Leading an Effective Board of Directors, 2nd Edition](https://feld.com/archives/2022/06/book-startup-boards-2nd-edition-is-available/)** — Brad Feld, Matt Blumberg and Mahendra Ramsinghani, Wiley, 2022.  
  *A practitioner account, from investors and a CEO, of how investor-backed boards work, which fills in the cases of young and fast-growing companies that this chapter only sketches.*
- **[The Wates Corporate Governance Principles for Large Private Companies](https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/the-wates-corporate-governance-principles-for-large-private-companies/)** — Financial Reporting Council, the United Kingdom's regulator for company reporting and governance, December 2018.  
  *Six principles for the boards of large private companies, a reference for what a board is expected to do beyond what its shareholders ask of it.*
- **[Unlock value with PE portfolio company governance](https://www.deloitte.com/us/en/programs/center-for-board-effectiveness/articles/private-equity-portfolio-company-board-governance.html)** — Deloitte Center for Board Effectiveness, January 2026.  
  *Advisory guidance for the board of a portfolio company, a company held as an investment by a fund, appointed by a controlling investment firm, covering composition, the split of board and management responsibilities, and dashboard reporting.*
