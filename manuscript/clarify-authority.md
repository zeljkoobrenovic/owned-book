{id: clarify-authority}
# 9. Clarify Authority: Decide Who Decides Before You Disagree

![Clarify Authority: Decide Who Decides Before You Disagree — logo](private-techuity/posts/06-clarify-authority/assets/images/06-clarify-authority/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to record who proposes, approves, funds and carries out a decision, and to plan for an approval that does not arrive in time.

> **WHY INVESTORS CARE:** An investor negotiates approval rights so that certain decisions come to it. A decision that goes ahead without a recorded approval exposes the investor to a plan it never authorized.

> **WHY YOU SHOULD CARE:** A suggestion from someone close to the investor can start a project nobody approved. An approval that never arrives can quietly become your delivery failure. Knowing who decides, and by when, prevents both.

> **KEY POINTS:**
>
> * Agree **who is authorized to decide** before disagreement arises. A suggestion from someone close to the investor can sound like an instruction.
> * Put **names, thresholds and dates** in the record. “Management recommends, the board approves” tells nobody whom to call, or by when.
> * Plan the **missed-deadline branch**. If approval does not arrive, take the remaining options to the authorized decision-maker and tell the team which funded plan it is executing.

> **[DYSFUNCTIONS THIS SECTION ADDRESSES](#where-investment-goes-wrong):**
>
> * **The Ghost Veto** — Records the approver, authority and deadline behind each decision.
> * **The Accidental Gatekeeper** — Separates suggestions from authorized instructions and assigns responsibility for the result.

When a company takes on an investor, more people seem to have a say in its decisions. A **new board member**, an **adviser** from the investment firm or a lender may each make a request, and it is not always clear which requests are instructions and which are only ideas. If nobody has written down who proposes, approves, funds and carries out a decision, a passing remark can start a project nobody approved. An approval that nobody tracks can arrive too late and quietly turn into a delivery failure.

This is a problem of **governance**: the arrangements for making decisions, overseeing them and holding people responsible. Good intentions cannot replace an agreed decision process.

**Informal influence** and **unclear delegation** exist under any ownership. Delegation is the authority a body hands to a person to decide within stated limits. A founder’s offhand remark can start a project as easily as an adviser’s. An investment changes the setting in which decisions are made. It can add **board seats** (a place, and a vote, on the board, the group of directors that oversees the company on the shareholders’ behalf), **approval thresholds** (amounts above which a different approval is needed), **reserved matters** (decisions that require a specified party’s approval whatever the amount) and advisers who speak, or seem to speak, for a shareholder. It is easy to give their requests **too much or too little weight**, and either mistake lands on product and engineering teams. Establish the actual authority, funding and deadline before committing.

This chapter begins Part II by examining what an investment can change about your authority and accountability: who is answerable for a result. It establishes what has changed, shows how to write down who decides what and connects technical choices to the business outcome. It then shows how to make a conditional commitment explicit, plan for a missed deadline, report in a way that asks for a decision and disagree without evasion.

{id: clarify-authority--setting-up-the-example-a-remark-over-coffee}
## Setting Up the Example: A Remark Over Coffee

Rotaline, the fictional scheduling-software company this book follows, appears here with a new **shareholder**: an investor that now owns part of the company. The onboarding decision below shares its figures and calendar with the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow); the ownership is this chapter's own. The cast is fictional. Ines is Rotaline’s chief executive officer (**CEO**), who runs the company and answers to the board. Alex is its chief technology officer (**CTO**), the executive who leads its technology work. Sam is its chief financial officer (**CFO**), who runs its finances, and Priya is its product leader, who decides what the product should do next. Morgan is the **investor’s technology adviser**, the role this book calls the **Technology Principal**: employed by the investment firm to assess and advise on technology, not to run the company’s technology. Their titles describe their work, but their actual approval rights must still be agreed.

Morgan **mentions over coffee** that Rotaline should probably change its cloud provider. Alex hears the **remark as an instruction** from the new shareholder and starts planning a migration: moving Rotaline’s systems to another supplier. Morgan, however, thought they were only offering an idea.

The chapter uses three examples, each teaching a different lesson:
- **Morgan’s cloud remark** shows **where an adviser’s influence ends**: an idea from the investor’s technology adviser is not an instruction until someone with authority approves it.
- **A separate onboarding proposal** walks through the **full approval process**, from a filled-in decision record that names who proposes, approves, funds and does the work, to what happens when the approval it depends on arrives late.
- **A rewrite of the scheduling engine**, the software that works out customers’ schedules, shows how a board should **challenge a technical choice** before funding it.

Before any of these, the first step is to establish what the investment has actually changed.

{id: clarify-authority--establish-what-has-changed}
## Establish What Has Changed

**Authority** means permission to make a particular decision. New ownership can change it in two ways. It can change it **formally**, through rights written into the investment, such as a board seat for the investor or a spending limit above which the board must approve. It can also change it **informally**, by changing what people expect, as when Alex treated Morgan’s passing remark as an instruction. To see which has happened, compare how decisions were made before and after the investment. Check the actual company documents, such as the shareholders’ agreement and any approval limits, and talk to the leaders responsible, rather than relying on assumptions about what an investor usually wants.

| Area | What to establish |
| --- | --- |
| Ownership | Who now holds **shares**, the units of ownership in the company, and which rights come with them: a seat and vote on the board, a separately agreed right to approve particular decisions, or only a share of the value? |
| Priorities | Which customer, financial or operating outcomes are now expected, and why? |
| Approval | Which hiring, spending, product or business-deal decisions need approval, from whom and by when? |
| Accountability | Who is accountable for each result, what resources have been committed and how will progress be assessed? |

For example, Rotaline’s board has given Ines, the CEO, a **spending limit**: she may approve up to €500,000 on her own, as long as the spending is part of the **approved plan**, the year’s budget and the work it pays for, which the board has adopted. Anything above that limit, or outside the plan, goes back to the board.

Two kinds of decision stay with the board whatever the amount. The first is any draw on a **reserve**, money the board set aside for needs the plan did not foresee, and any change to what an approved **envelope** funds, an envelope being a fixed sum authorized for a defined bundle of work: Ines spends inside the plan, she doesn’t rewrite it. The second is a permanent hire outside the approved **headcount plan**, the list of positions the budget pays for. These are the delegation rules the rest of this chapter, and the later chapters that draw on a reserve, refer to.

Now the cloud suggestion. No reserved matter covers the choice of cloud provider. Morgan holds **no approval right**; the investment firm’s rights are exercised through its **seat on the board**. So the suggestion is an idea for Alex to evaluate, and a migration would need Ines’s approval if it stays inside the approved plan and below her threshold, or the board’s if it exceeds the threshold or changes what the plan funds. Alex records it as an option to cost, not as a plan, and tells Morgan so.

An investment doesn’t automatically change every entry. Recording **what stayed the same** helps when employees are unsure whether earlier authority still applies. If you inherited the ownership arrangement, begin with the decisions ahead rather than assuming you took part in agreeing the original terms.

The investor is a **fund**, a pool of money the investment firm manages for its own backers. The fund’s **investment committee** is the group inside the firm that approved putting the fund’s money into Rotaline. That committee does not approve Rotaline’s hiring plan: the company’s board and executives approve company work. The firm’s operating professionals, people it employs to help the companies it owns run better, contribute expertise. **Lenders**, who advanced money that must be repaid, can hold contractual rights that constrain all of them; a loan agreement may, for example, forbid new borrowing without the lender’s consent.

Do not assume your investor organizes its involvement the way another does; the **evidence does not show one standard model**. Gompers and colleagues surveyed private equity (PE) investors, firms that buy ownership stakes in companies outside the public stock markets. The investors described paying attention to three things: how the company is governed, how it is financed and **value creation**, that is, making the business worth more. The survey does not show a single common structure for who does what. [S04: PE practitioner survey](https://www.nber.org/papers/w21133) Some firms have dedicated teams. KKR, a large investment firm, describes **Capstone**, its in-house **operating-support team**, as working alongside its investment teams, company boards and company management. That is the firm’s own description of how it intends to work, not evidence that every such intervention succeeds. [S22: KKR Capstone description](https://www.kkr.com/approach/capstone)

{id: clarify-authority--write-down-who-decides-what}
## Write Down Who Decides What

Priya and Alex **want to spend €1 million** automating onboarding, the setup needed before a new customer can use the product; today Rotaline’s implementation team configures the product for each customer by hand. A customer’s configuration is the set of product settings that fit that customer, and the team chooses those settings one customer at a time. Their decision record:

| | Rotaline’s answer |
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

This is the €1 million program discussed in the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow), not an approved commitment to spend it. The board still needs a **feasible funding plan**, and the chapter [Set Priorities: Say No With Evidence, Not Opinion](#set-priorities) shows why it may fund a smaller step first.

**Escalation** means taking an unresolved issue to someone authorized to decide it. The route has to match the urgency, and it can fail in two directions. **Too slow:** if escalating takes six weeks, for example waiting for the next board meeting, it is useless for a financing deadline, a date by which money must be secured, or for a service failure that is hurting customers today. **Too fast:** if every disagreement about system design is sent straight to the board or the investor as an emergency, the company’s own leaders never get to use their judgment on decisions that are theirs to make.

![Four numbered cards stacked in one column, propose, approve, fund and deliver, each with one responsible role; a dashed arrow labelled advice only enters the proposal card, and the approval card shows a single formal-approval gate: the chief executive for delegated decisions, the board for reserved or larger decisions.](private-techuity/posts/06-clarify-authority/assets/images/06-clarify-authority/decision-rights-map.jpeg)

**Figure 1:** *One responsibility per stage. The product and technology leaders propose. The chief executive approves delegated decisions: those inside the approved plan and within her limit. The board approves reserved matters, such as a reserve draw or a hire outside the headcount plan, and anything larger. The finance leader confirms the cash and its dates. The team delivers. Advice enters the proposal, not the approval.*

The Rotaline record above names people: Priya, Alex, Ines. Replace each name with a role (product leader, CTO, CEO) and the record becomes the general table below, usable for any company. Read it with three cautions. First, the last column, **Approval to verify**, names the document to check, such as the executive delegation or the shareholder agreement, not the person who approves; who that is depends on your company. Second, where a row quotes a Rotaline rule, that is one company’s arrangement, not a standard. Third, the **Investor adviser’s possible contribution** column lists help the adviser might offer, such as challenging assumptions or assessing candidates; it gives the adviser no right to approve anything. Fill in the last column from your own company’s documents.

| Decision | Company contribution | Investor adviser’s possible contribution | Approval to verify |
| --- | --- | --- | --- |
| Product priorities within an agreed budget | Product leader and CTO recommend; CEO resolves major trade-offs | Challenge assumptions and supply evidence | The executive delegation and any reserved matters |
| Material technology investment (one large enough to change the plan) | Management prepares options and the financial case: costs, benefits and risks in money terms | Test technical feasibility and delivery dependencies, the work that must be finished first | Board, shareholder or lender approvals where the agreements require them |
| CTO appointment | CEO defines the need, runs the process and recommends | Help assess candidates and context | The actual appointment authority in the agreements |
| Executive appointment (a chief product officer, a head of engineering) | CEO writes the role design, runs the selection and recommends the appointment | Introduce candidates and help assess them against the company’s design | The appointment authority, plus any reserved matter over executive officers’ hiring, dismissal or pay |
| Change to the headcount plan (hires beyond it, a freeze) | Management shows what each role delivers and what a conditional role waits for | Compare the hire with similar companies and challenge its shape | Whoever holds the headcount authority: at Rotaline, the board for hires outside the approved plan and the CEO within it |
| Staffing reduction or restructuring | Management costs the alternatives, names the work that stops and the cash by date | Comparisons from other companies, which are information rather than instruction | The board for a change to what the plan funds, any reserved matter over the **operating plan** (the year’s work and the people and money assigned to it), and employment law where the people are employed |
| Acquisition integration (combining a bought company’s operations with the buyer’s) | Executives are accountable for the integration plan | Assess sequencing, capacity and reusable support | The approvals for the purchase itself, then the company’s ordinary operating governance |

{id: clarify-authority--several-investors-do-not-make-one-decision-maker}
## Several Investors Do Not Make One Decision-Maker

In a fictional **minority round**, a sale of new shares in which the new investors together buy less than half the company, Rotaline’s founder keeps most of the **voting shares**, the shares that carry votes at shareholder meetings. One new investor receives a seat on the board; another receives a separately negotiated right to approve specified decisions. Alex is asked for three versions of the hiring plan. The right response is to establish which **forum**, the meeting or body authorized to settle the choice, can approve the company’s plan and bring the alternatives there. Adding all the requests to the **roadmap**, the plan of what the product team will build next, would turn unresolved shareholder disagreement into the team’s delivery problem.

The National Venture Capital Association (NVCA), the industry body for investors in young companies, publishes separate model documents for share purchases, investor rights and voting arrangements. Its overview also describes funding released in stages, over time or when milestones are reached. This supports looking beyond an ownership percentage: rights are written into agreements, not read off a shareholding. It doesn’t establish the terms of any particular company’s agreement. [S61: NVCA model-document overview](https://nvca.org/model-legal-documents/)

With a **controlling financial sponsor**, an investment firm that owns enough of the company to control it, ask **which decisions remain** delegated to management and which require its approval. With a **corporate parent**, an operating company that owns this one, map the local board and executives alongside the parent’s product, security, finance and procurement functions. A company that has merely bought a minority stake in Rotaline doesn’t by itself bring that group hierarchy with it.

**Record, for each decision, where the authority comes from**: the document that grants it, such as a clause in the shareholder agreement or the board’s delegation to the CEO. Record also the **threshold** that sends a decision upward (a spend above a set amount, say) and how long the approver takes to answer, in plain words the team can use. When shareholders disagree, the board or another authorized body must make the call; which body that is, and what happens in a **deadlock**, when the required agreement cannot be reached, depends on the actual agreements. The product and engineering leader supplies the options, the evidence and the consequences of each. What the leader must not do is settle the disagreement quietly by promising each shareholder work that cannot both be done, such as a new market to one and a cost cut to the other.

{id: clarify-authority--connect-technical-choices-to-the-business-outcome}
## Connect Technical Choices to the Business Outcome

In a second example, Alex proposes rewriting Rotaline’s scheduling engine because it is hard to change. The board asks **how that supports business growth**. Alex answers that the current **stack**, the set of technologies the engine is built on, is dated. The exchange produces heat but little information.

A better challenge asks what the engine stops the business from doing, the **constrained business outcome**: which customer need it can’t serve (a scheduling rule a new client requires, say), how often that happens and what it costs in lost or delayed revenue. With those answers, Alex can lay out three options: a **focused change** to the part that blocks the customer, a **staged replacement**, and the **full rewrite**. Sam can compare their **cash profiles**, how much cash each option needs and when, against the €0.5 million left in the annual planning example (see the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow)). The board can then decide which option to fund and which risks to accept. It has not turned into an architecture committee, a body that designs the system; it has only required that the link between the investment and the business plan be spelled out.

The same discipline applies in reverse. “Cut engineering by 20%” isn’t a complete operating plan. Which work disappears? Which obligations remain? What happens to customer commitments and to **operational coverage**, having enough people on hand to keep the service running and answer support calls? If the decision is still to cut, record its **expected consequences** rather than quietly converting them into impossible delivery promises.

These requests reach a company leader in three forms that sound alike and are not.

- A **formal approval right** comes from the agreements: a reserved matter, a board seat, a right of consent over executive pay or the operating plan. The response is to bring the authorized body a decision it can take.
- A **funding condition** attaches money to a plan. Two examples: a **bridge**, short-term financing that covers a gap until longer-term funding arrives, released only once a cost plan is adopted; or a new **funding round**, a sale of new shares to investors, whose **term sheet**, the document setting out the proposed terms before the binding contracts are signed, wants a particular executive in place. The response is to translate the condition into a date and a number, and decide whether to meet it.
- **Influence** is everything else: an adviser’s **benchmark**, a comparison with similar companies, a director’s view of a leader, an introduction. The response is to record it as an option and assess it on the same evidence as any other.

The chapter [Scale the Team Up: Headcount Is Not Capacity](#scale-the-team-up) works an investor-proposed appointment through that distinction, and [Scale the Team Down: A Cut Is a Number, Not a Plan](#scale-the-team-down) a staffing reduction, where all three arrive at the same board meeting.

{id: clarify-authority--make-a-conditional-commitment-explicit-and-plan-the-missed-deadline}
## Make a Conditional Commitment Explicit, and Plan the Missed Deadline

Back to the onboarding proposal, which follows the same scenario and dates as the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow). In that chapter, on the first day of the financial year, Ines approved a **pilot** within her delegation, the spending she may approve without going to the board. The pilot is a small trial: it builds the reusable setup step for the common customer types and measures it on the first eight customers before more money is spent. It costs €180,000 to build plus €30,000 of first-year maintenance, €210,000 in all. The money comes from two places: the cash the company had at the start of the year, and the cash the year is expected to leave over once its planned payments are made. The effort is twelve **engineer-weeks** from the current team. An engineer-week is one engineer’s work for one week, so twelve means, for example, three engineers for four weeks, not twelve weeks on the calendar.

The €1 million record above went to the board in the same budget round, and the board answered within the two weeks the record asked for, before the budget cycle closed. It did not approve spending the full €1 million in one year. Instead it made three calls. It **endorsed the direction**: automating customer onboarding is worth pursuing. It **confirmed the pilot** Ines had already approved. And it **reserved the two implementation hires**, the specialists who would take over part of the setup queue: Ines cannot make them under her delegation, and the board will decide them itself at its May meeting. Any permanent hire outside the approved headcount plan needs the board, whatever it costs.

**The pilot, then completing the first stage.** The reusable setup step the pilot builds is usable from early February for the common customer types, and by 1 April Priya has measured the first eight customers set up with it. The next milestone, and the one Alex now has to put a date on, is completing the first stage: building **templates** for the less-common customer types and moving every new customer onto the step, so that no new customer is set up by hand. A template is a reusable set of settings for one customer type; with it, setting up a new customer of that type means filling in the template rather than configuring the product from scratch. Moving existing customers onto the new setup is a separate second stage, priced in the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow). The engineering build is largely done by February, so what limits the completion date is not engineers but the implementation team: the same people who write the templates also keep setting up new customers by hand until the step covers every customer type.

**What the hires change.** Alex estimates that the current team can complete the first stage by January of the following year. With two implementation specialists starting in June to take over part of the setup queue, it would be done by October. The hires would cost about €175,000 for June to December and about €300,000 a year after that, every year. That is well inside Ines’s €500,000 **approval limit**, but it is still a **board decision** because it adds permanent headcount. The board decides at its May meeting, on two pieces of evidence: Sam’s **collections** for the first quarter, January to March, meaning the customer payments actually received, compared with the plan; and Priya’s 1 April report on the first eight customers. So Alex should present October as a proposal with its conditions attached: “October, if the board approves the hires in May and both start in June.” An unconditional “October” would hide both conditions. And approval does not put people in seats: the board can say yes in May and recruitment can still miss June, which pushes October back.

**The specialist.** Only one person understands how the current customer configurations are set up: an implementation specialist working on contract, not an employee. The templates for the less-common customer types depend on that knowledge. The specialist’s contract runs to 31 March and is already paid for in this year’s operating plan. Part of those contracted days goes to writing the configurations down for the build team; the days cost nothing extra, so they are not part of the €210,000. By 31 March, Alex either accepts that written record as complete or lists what is missing. That way the January completion date depends on the written record, not on the specialist renewing the contract.

**If the record is incomplete**, the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow) already set up a **fallback**: Ines can extend the specialist’s contract once, by one quarter, for €37,500. She must give notice by day 100 of the financial year, which is 11 April. That money is extra, not part of the €210,000: pilot plus extension comes to €247,500, before any hiring or the data-quality step discussed below. It is still within what Ines may approve on her own. The specialist would then work from 15 April to 15 July. The quarter costs €12,500 a month, and this chapter assumes each month is paid after it is worked, so the three invoices fall due on 15 May, 15 June and 15 July. Ines extends the contract only if Sam’s cash forecast, rerun on day 100 with the payments actually received and every remaining commitment, shows cash staying above the reserve, the minimum balance the company has agreed to keep, on each of those three dates. If she extends it, the remaining templates are written down with the specialist before 15 July.

**If the extension does not happen**, because Ines lets the 11 April deadline pass or because the forecast shows cash falling below the reserve, the implementation team writes the remaining templates from the written record alone. Any customer type it cannot cover that way stays on manual setup, and its template moves to the next budget round; Ines tells the team and the affected customers in writing. The January date still holds for every other customer type. Separately, on 30 June the company asks the specialist whether they are free for the third quarter rather than assuming so; that question is about extra hands for the busiest period of the setup queue, not about the templates.

**The January plan is not a hope: its money and people are already secured.** The money is the €210,000 already approved and set aside in the cash plan. The €180,000 build pays for contractor time on the remaining templates and for the tools and services the build needs, on the dates the cash plan sets; the €30,000 pays for the first year of maintenance. The specialist’s days spent writing the configurations down are not in that sum; they come from the first-quarter contract the operating plan already pays for. The people are the implementation team, already on payroll, plus the twelve engineer-weeks Ines assigned when she approved the pilot. Those weeks were freed by postponing a refresh of the company’s reports to the following quarter, and the plan records that postponement so the same weeks are not promised to two projects. Only the faster October date, which needs the two hires, is not yet funded. The specialist extension, needed only if the written record is incomplete, has its own €37,500 and its own cash condition, set out above.

**Now the most likely way this goes wrong**: the May meeting ends and the board has not decided on the hires. Alex goes back to Ines with the January option, the plan that is already funded, and says so openly: without the hires, January is the date. Ines then has two choices. She can take the question to the board chair, the director who leads the board’s work and can call a decision between meetings, or she can confirm January. Either way, the team is told in writing that January is the plan it is working to, with the cash and people it already has. And anyone who was promised October, such as a customer or the sales team, gets one of three responses, which Ines chooses:

- **renegotiate** the promise with the customer;
- **fund** a contract specialist for the peak quarter from the uncommitted cash within her delegation, if the firm confirms on 30 June that one is available; or
- take the hiring **back to the board**.

Three other outcomes are possible, and each has a set answer. **The board approves the hires, but they start late.** If the two have not started by the end of June, the team and customers keep hearing January. A later start does not bring October back on its own, because the October estimate assumed both started in June. Once the real start dates are known, Alex works out a new completion date from them, and Ines approves it before anyone is told; for customers already promised October, she again picks one of the three responses above. **The board refuses the hires.** January is the plan, and the hiring question waits for the next budget round. **The specialist’s knowledge is not captured.** If the written record is still incomplete on 31 March and the contract is not extended, or the specialist is not available, the customer types that cannot be covered without that knowledge stay on manual setup, and their templates move to the next budget round; January still holds for every other type. This case does not touch October, because October depended on the hires, not on the specialist.

| Field | Rotaline’s answer |
| --- | --- |
| Scope | Complete the first stage of onboarding automation: templates for the less-common customer types, and every new customer set up with the step |
| Chosen option | January of the following year with the current team; October if the board approves the two implementation hires at its May meeting and both start in June |
| Alternatives rejected | An unconditional October promise; contractors booked now against a hiring budget that has not been approved |
| Funding: baseline | €210,000 authorized by Ines within her delegation and identified in the cash plan: the €180,000 build (contractor template time, tools and services) paid in instalments through the year, and the €30,000 first-year maintenance charged monthly from February. The engineers, the implementation team and the specialist’s first-quarter engagement are already paid for by the operating plan and are not counted again |
| Funding: the two hires | About €175,000 this year for June to December, and about €300,000 a year recurring; a board decision |
| Funding: optional specialist extension | €37,500, additional, only if the written record is incomplete on 31 March: service from 15 April to 15 July, paid in arrears in three invoices of €12,500 due 15 May, 15 June and 15 July; within Ines’s delegation and only if Sam’s day-100 forecast shows cash above the reserve on each of those three dates |
| Accountable for delivery | Priya for the onboarding work; Alex for the engineering build and the delivery estimate |
| Staff allocation | The implementation team, on payroll; twelve engineer-weeks of the current team, already scheduled; the contract specialist’s first-quarter days, already paid for by the operating plan, including the written record of the less-common configurations that Alex accepts by 31 March, with a one-quarter extension option exercisable by notice by 11 April (day 100) |
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

![Approval, funding and capacity must be confirmed before a conditional plan becomes a delivery commitment.](private-techuity/posts/06-clarify-authority/assets/images/06-clarify-authority/conditional-commitment-gates.jpeg)

**Figure 2:** *Approval, funding and capacity are separate conditions. Record each one, the person who can resolve it and the decision date.*

{id: clarify-authority--reporting-that-asks-for-a-decision}
## Reporting That Asks for a Decision

A board report should do three things for each **material** outcome, one large enough to change a decision: state the **result**, say **what it means**, and **name the decision** the board now needs to make. A traffic-light dashboard, where each project is marked green, amber or red with no evidence behind the colour, can hide more than it shows. “Green” might mean on time, within budget or lower risk, or simply that no one has reported a problem yet, and the board cannot tell which.

For the onboarding work, a three-sentence update is enough at the board’s April review, about ten days after Priya’s 1 April report. In this fictional example it reads: “Across the first eight customers, the hours needed to set up each customer fell from 80 to 62, short of the 50 we assumed, and about 40% of the remaining hours go on fixing customer **data quality**, records that arrive with missing fields or inconsistent formats, not on the product. We propose a data-quality step, an automatic check and clean-up of customer records before setup, costing €40,000 and four engineer-weeks, before deciding on further implementation hires. Decision requested: approve the €40,000 from the reserve at this meeting; the hiring decision stays with the May meeting, as the board decided in January, once Sam has closed the first quarter’s collections.”

Why does €40,000 go to the board when Ines may approve up to €500,000? For two reasons. First, the money would come from the reserve, which sits inside an envelope the board approved, and any draw on the reserve is the board’s decision. Second, it would pay for a data-quality step the approved plan did not include, which changes what the envelope funds, and that too is the board’s call. Ines’s €500,000 limit covers spending inside the approved plan, so neither case falls under it. The chapter [Set Priorities: Say No With Evidence, Not Opinion](#set-priorities) follows the same path when it pays for its recovery retest from the reserve. The figures here come from the shared pilot record in the [Toolkit: Records That Make a Decision Concrete](#toolkit), which also holds templates for reporting on an initiative and its outcomes. Keep the cost of reporting in view: a monthly questionnaire that no decision depends on takes up the team time the shareholder wants spent on improving the company.

{id: clarify-authority--parallel-instructions-need-one-accountable-leader}
## Parallel Instructions Need One Accountable Leader

Letting investor-side people **talk to engineers directly** can help in two situations: during **due diligence**, the investigation an investor carries out before it invests, and during a **support assignment** with a clear, written scope. It becomes a problem when engineers take priorities from several directions at once: the investor’s adviser, their own CTO, and the investment team, the firm’s deal professionals. That is a second chain of command, with no agreed remit and nobody answerable for the result; an engineer told by the adviser to fix the data pipeline and by the CTO to ship a feature has no one to settle which comes first. For any assignment, name the one company leader accountable for it, and send every conflicting instruction back to that person to resolve. How an adviser’s influence and information should be used, including the limits of confidential coaching, is the subject of the chapter [Clarify the Adviser’s Role: Are They Helping, Assessing or Deciding?](#clarify-adviser-role); the written scope and rules for a support assignment are in the chapter [Set the Terms of Help: Agree the Work, Authority and Handover](#set-terms-of-help).

{id: clarify-authority--disagreement-without-evasion}
## Disagreement Without Evasion

Each party should be able to **deliver bad news plainly**. A leader should be able to say: “We can hit the cost target, but not deliver the current roadmap as well. Here are the choices.” An investor’s adviser should be able to say: “The evidence no longer supports the original **investment thesis**,” the reasoning for why the investment was expected to succeed, for example that customers would adopt a new product line faster than they have. And a board should be able to overrule a recommendation, as long as it writes down what it is accepting by doing so: the risk, the cost or the delay the recommendation was meant to avoid.

Authority explains who can decide. It does not explain why the approver wants what they want. The next chapter, [Compare Incentives and Stakes: Equity, Carry and Jobs](#compare-incentives-stakes), reads the incentives behind a decision: what the executives, the fund manager and the employees each stand to gain or lose.

{id: clarify-authority--questions-to-consider}
## Questions to Consider

1. *For the most important technology decision ahead of your company, who recommends, who is authorized to decide, who funds, who implements, and by when? Can you name people rather than roles?*
2. *When an adviser from the investor makes a suggestion, how do your engineers know whether it is an idea, an assessment or an instruction?*
3. *Which of your current commitments depend on an approval or hire that has not yet arrived? Is the condition recorded, with the decision date and what happens if the date passes?*
4. *When shareholders or board members disagree, which forum resolves the choice? Are incompatible requests being carried into the team’s **backlog**, its list of work waiting to be done, instead?*

{id: clarify-authority--to-probe-further}
## To Probe Further

- **[Who Has the D?: How Clear Decision Roles Enhance Organizational Performance](https://hbr.org/2006/01/who-has-the-d-how-clear-decision-roles-enhance-organizational-performance)** — Paul Rogers and Marcia Blenko, Harvard Business Review, January 2006.  
  *The Bain consultants' method behind this chapter's "who recommends, who decides, who implements" pattern, showing what goes wrong when several people believe they hold the decision.*
- **[Startup Boards: A Field Guide to Building and Leading an Effective Board of Directors, 2nd Edition](https://feld.com/archives/2022/06/book-startup-boards-2nd-edition-is-available/)** — Brad Feld, Matt Blumberg and Mahendra Ramsinghani, Wiley, 2022.  
  *A practitioner account, from investors and a CEO, of how investor-backed boards work, which fills in the cases of young and fast-growing companies that this chapter only sketches.*
- **[The Wates Corporate Governance Principles for Large Private Companies](https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/the-wates-corporate-governance-principles-for-large-private-companies/)** — Financial Reporting Council, the United Kingdom's regulator for company reporting and governance, December 2018.  
  *Six principles for the boards of large private companies, a reference for what a board is expected to do beyond what its shareholders ask of it.*
- **[Unlock value with PE portfolio company governance](https://www.deloitte.com/us/en/programs/center-for-board-effectiveness/articles/private-equity-portfolio-company-board-governance.html)** — Deloitte Center for Board Effectiveness, January 2026.  
  *Advisory guidance for the board of a portfolio company, a company held as an investment by a fund, appointed by a controlling investment firm, covering composition, the split of board and management responsibilities, and dashboard reporting.*
