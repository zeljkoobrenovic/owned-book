{id: fix-decisions-before-hiring}
# 24. Scale the Team Up: Headcount Is Not Capacity

![Scale the Team Up: Headcount Is Not Capacity — logo](private-techuity/posts/22-fix-decisions-before-hiring/assets/images/22-fix-decisions-before-hiring/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to trace one piece of work through the company, separate decision, knowledge and staffing constraints, assess leaders in their system and decide what hiring the plan needs.

> **WHY INVESTORS CARE:** Headcount, the number of people a company employs or has approved to hire, is one of the few levers an investor can see and fund. It wants to know whether the money buys capacity or just buys people who wait behind the same bottleneck.

> **WHY YOU SHOULD CARE:** Hiring into a queue caused by unclear authority and concentrated knowledge buys people who wait. The diagnosis decides whether new people will help, and what shape the hire should take.

> **KEY POINTS:**
>
> * A company’s capacity includes **how people decide and coordinate**. New tools, locations or hires will not remove a queue made of unclear authority and concentrated knowledge.
> * People changes have **transition costs and a knowledge-transfer test**. Compare the full delivery model, including recruitment, overlap, management effort and the receiving team’s demonstrated competence.
> * The diagnosis should **produce a staffing decision**: hiring proceeds, changes shape or is deferred, with the remaining gap, its funding and the evidence that would reopen the choice named.

New investment naturally opens room to hire. The money that funds the plan can also pay salaries, and investors often push for it to turn into people quickly: headcount is visible, easy to report and easy to compare with the plan. The pressure is understandable, but **hiring naively can backfire**. When work waits on unclear authority and on knowledge held by a few people, new hires join the same queue. They need training from the specialists who are already the bottleneck, they add coordination, and the waits can grow rather than shrink. The friction in how the company decides and delivers must be found before the hiring plan is written.

The plan funded new resources, but not the management time and decision changes needed to use them. An **operating model** is the arrangement of responsibilities, teams and processes through which work gets done. **Capability** is what that arrangement lets people do reliably. Every investment in the preceding chapters depends on people with the time, knowledge and authority to do the work. An investment case, the argument for committing money to a plan, is not complete if it funds the work without funding the capacity to do it.

{id: fix-decisions-before-hiring--setting-up-the-example-a-three-week-pricing-change}
## Setting Up the Example: A Three-Week Pricing Change

Larkspur is the fictional company this book follows; it sells scheduling software. This example starts from the finding in the chapter [Assess Capability: Can the Team Deliver?](#can-the-team-deliver), which read two clocks for a change to Larkspur’s pricing rules, the rules that decide what customers are charged. The first clock runs from the customer’s request until the change is in **production**, the live system customers use. It shows about three weeks.

The second clock starts at the **commit**, the moment an engineer records a version of a code change in the team’s shared version history. A commit is a record, not a finish line: recorded code need not be complete or ready for customers. The clock stops when the change is **released**, that is, put into use in production. Recording and releasing are separate events, and the second clock measures the time between them. It shows under two days.

The assessment could say only that most of the time falls before the commit. It could not say what that time is made of, because at Larkspur the work before the measured commit includes building the change as well as approvals and queues. The trace below supplies the split: sixteen working days (3 + 7 + 2 + 3 + 1), of which two are building, one is release and thirteen are waiting. Larkspur also plans to sell in a second country, and that country’s tax and pricing rules will pass through the same queue.

Larkspur’s board, the group of directors that oversees the company on behalf of its owners, wants a second product team before the next **funding round**, the next time the company raises money from investors. Investors and their advisers may also propose organizational changes directly: a new leader, a cheaper location, a second team. Before Larkspur adds people, it should know what the queue is made of. When an investor proposes an appointment, the same evidence decides whether the role is the answer.

{id: fix-decisions-before-hiring--follow-one-piece-of-work-through-the-company}
## Follow One Piece of Work Through the Company

Start with the customer and operating work the company needs to perform. Who learns about customer needs? Who decides priorities? Who can release a change? Who supports it? Who resolves conflicts across product boundaries?

An organization chart shows reporting lines; it does not capture these dependencies. Trace real pieces of work from request to outcome and record where they wait, where information is lost and which people must intervene repeatedly. The purpose is diagnosis, not a time-and-motion exercise that treats every pause as waste. A deliberate review step may prevent expensive mistakes. **An unclear decision boundary** may cause avoidable delay. Distinguishing the two is more useful than announcing that the organization needs more autonomy or more control.

Here is one of Larkspur’s pricing changes, traced by Alex, who leads technology as chief technology officer (CTO), and Priya, who leads product. Two more people appear below: Ines, the chief executive, who leads the company, and Sam, who leads finance. The change touches the **invoicing module**, the part of the software that prepares customer invoices, the bills sent to customers. The figures are fictional.

| Step | Working days | What the wait is made of |
| --- | ---: | --- |
| Request waits for Priya to confirm the commercial rule, for example whether a new discount is allowed | 3 | A product decision nobody else is authorized to make |
| Change waits in the two specialists’ review queue | 7 | The specialists also handle every problem in production; review is fitted around these incidents |
| Change built and tested | 2 | The only building in the sequence |
| Change waits for Ines to sign off anything that touches customer invoices | 3 | A control introduced after an invoicing error two years ago, never revisited |
| Commit to production | 1 | The second clock, under two days in the assessment. DORA (DevOps Research and Assessment), a research program on software delivery, calls it change lead time. In this fictional trace the commit that starts the clock is recorded only after the change is built and signed off. Many teams commit earlier and more often |
| **Request to production** | **16** | **About three weeks; two days of building, one of release, thirteen of waiting** |

![Two rows compare the same five stages of one customer request. Today: three waiting stages (rule approval 3 days, specialist review 7 days, invoice sign-off 3 days) surround build and test (2 days) and release (1 day), totalling 16 working days. A second row headed “Forecast: 10 working days” crosses out the rule-approval wait and the invoice sign-off wait, each tagged separately “Delegated: 3 days saved”, while the 7-day specialist review remains, tagged “Knowledge gap: still 7 days”. A banner across the whole row reads “Forecast total: 6 days saved, no new hire”. The days saved are forecast, not measured.](private-techuity/posts/22-fix-decisions-before-hiring/assets/images/22-fix-decisions-before-hiring/work-crosses-team-boundaries.jpeg)

**Figure 1:** *The upper row is the trace in the table above: five stages, sixteen working days, three of them waits. The lower row looks ahead to the delegation described in the next section. Each of the two approval waits is removed and each saves three days; the banner gives their combined six. It is a forecast, not a measurement. The seven-day specialist queue stays in both rows, because it is a knowledge constraint rather than a decision one — which is why the hire that follows is one billing engineer and not a second team.*

The trace separates three constraints that “the team is too slow” had merged. The first is a **decision constraint**: two of the waits exist because authority sits with one person. The second is a **knowledge constraint**: the specialists’ queue exists because only two people can safely change the invoicing module. The third, a **staffing constraint**, becomes visible only once the first two are addressed: how much capacity is actually missing?

{id: fix-decisions-before-hiring--change-the-decisions-first}
## Change the Decisions First

Two of the waits can be removed without hiring anyone, and each is removed by the person who holds the authority. In the week after the trace, Priya agrees a catalogue of pricing-rule types that the team may implement without a fresh commercial decision; only new rule types come back to her. Ines delegates the invoice sign-off to Sam’s finance team for changes inside that catalogue, with a monthly review of what was released. The control she introduced after the invoicing error is kept, but moved to the people who already reconcile invoices, which means checking them against the underlying records each month. If the finance check adds no queue of its own, these are forecast to remove about six of the thirteen waiting days. That is the initial forecast, not a result; Alex traces the next three pricing changes to confirm it. Neither change requires a new hire, which is not the same as costing nothing: the monthly review takes Ines’s time, and the sign-off takes finance’s.

The specialists’ queue does not move. It is not a decision problem; it is a knowledge problem, and delegation cannot fix it. The forecast **end-to-end lead time**, measured from the customer’s request to the change running in production, is about ten working days, of which seven are still spent waiting for the two people who understand the invoicing module and are interrupted by production work. That is the **capacity gap the plan actually has**: not a second product team’s worth of engineers, but a third person able to change the invoicing module, and protected time for the two who can.

{id: fix-decisions-before-hiring--decide-what-hiring-the-gap-needs}
## Decide What Hiring the Gap Needs

The board asked for a second product team of five before the next funding round. Alex and Priya compare three responses; every figure is fictional.

- **Hire the second team now.** Five roles, about €450,000 a year once filled, six months of recruitment and onboarding (the period in which new people learn the company and its software), and management time from Alex. It would not touch the specialists’ queue, because none of the five could change the invoicing module for months, and it would lengthen the queue by producing more changes that need review.
- **Hire nobody and rely on the delegation changes.** No additional hire; the delegation still requires finance and management time. The queue stays at seven days, and the second country’s rules still depend on two interruptible people.
- **Change the shape of the hire.** One engineer into the billing area now, with the explicit job of becoming the third person who can change the module; one protected day a week of each specialist’s time for knowledge transfer; the second team deferred until two conditions are both met: second-country demand is evidenced, and the next funding round is committed and the board has approved the roles.

“Committed” has a narrow meaning here: investors have signed an agreement to provide the money, subject to its terms. That is firmer than an intention to invest. It is not yet completed financing, and only money that has arrived can pay salaries, which is one reason the roles also need the board’s approval before anyone is recruited.

They choose the third: one billing engineer now, protected time for the transfer, and the second team deferred on stated conditions.

| Element | What was decided |
| --- | --- |
| Funded now | One billing engineer, about €90,000 a year, plus an agreed reduction in the specialists’ production duties. The engineer fills a vacant engineering position already in the approved **headcount plan**, the board’s list of positions the company may fill. The pay comes from the approved operating budget, the board-approved plan for spending on running the business |
| Deferred | The five-person second team, until demand is evidenced, the next funding round is committed and the board has approved the roles |
| Scarce capacity | The two specialists’ time. The protected day is paid for by a named reassignment, not assumed. The operations lead takes the first response to incidents, and hands the weekly capacity report and the follow-up of support requests raised with suppliers to the support team. The day comes out of work that moves, not work that silently stops |
| Authority | Ines authorizes the hire under her delegation. The position is already in the headcount plan and its pay is in the approved budget, so assigning it to billing needs no new board decision. A position outside the plan would have been the board’s to approve (see the chapter [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides)). She takes the changed shape to the board, which had asked for a team and is asked to accept a conditional plan instead. Alex is accountable for the billing engineer and the transfer, Priya for the catalogue |
| Rejected | The full second team, because it does not address the gap, adds to the queue and commits payroll (the recurring cost of employees’ pay) ahead of money not yet received. No hiring, because it leaves the plan dependent on two people |

- **The lead time is still above two weeks sixty days after the delegation changes.** The response is to trace the next changes, not to hire. If the approvals have gone but the queue persists, the capacity diagnosis is revisited. If the agreed changes were never made, the reasons and the accountability are addressed first.
- **The second country signs customers faster than expected.** That satisfies the demand condition only. The five-person team still requires committed funding and board approval, and until both exist the one-engineer plan remains the authorized response.
- **The billing engineer cannot release a rule change independently six months after starting.** The transfer has failed, and the role is reassessed rather than the specialists released.

That is the sense in which decisions come before people. It is not a rule that hiring always waits. The trace showed which roles the plan needed, and the hire that was made was different in shape from the one the board first asked for.

{id: fix-decisions-before-hiring--assess-leaders-in-their-system}
## Assess Leaders in Their System

A leader who built an early product may need support to lead a larger organization. A leader with large-company experience may introduce processes a small business cannot afford. Neither background establishes fit by itself.

Describe the work the role requires: product judgment, technical direction, operational reliability, people leadership, commercial communication or integration. Assess the evidence in each area and the system around the person. A weak product function, the people and work that identify what customers need and choose what to build, shouldn’t automatically become a verdict on the CTO, and a three-week queue made of two sign-offs and an interrupted pair of specialists is not evidence that the CTO cannot lead. Equally, technical expertise doesn’t excuse an inability to develop people or make hard decisions.

Changing a CTO can be necessary when the company’s needs have changed or leadership is ineffective. It can also be a convenient explanation for an unrealistic plan. Before recommending replacement, state a **hypothesis**, an explanation that can be checked: what must new leadership enable, and what evidence shows that capability is missing? Does the leader make sound decisions but lack product management support? Is delivery blocked by unstable commercial commitments? Has the board asked for incompatible outcomes? A diagnosis that begins and ends with the individual may miss the system around them, and a replacement who inherits the same system reproduces the failure while losing knowledge. The chapter [Compare Incentives and Stakes: Equity, Carry and Jobs](#different-bets) adds one distortion to watch. A leader’s pay, or expectations about an **exit** (the eventual sale of the company or of the investors’ stake, when owners turn their shares into money), can shape how that leader is assessed.

The hypothesis cuts both ways, and that is how it preserves accountability. Suppose the sequence at Larkspur had gone differently. Priya’s catalogue and Ines’s delegation were agreed and the engineer was funded. When Ines reviews the sixty-day trace, the queue is unchanged.

The release log shows every catalogue change now waiting for Alex’s personal approval before finance sees it, so the sign-off wait has moved rather than gone. The specialists’ protected day has gone to incidents that Alex chose not to reassign. The billing engineer has been moved onto feature work.

The conditions were changed and the leader did not use them. The hypothesis “an engineering leader who will delegate release authority and protect knowledge transfer removes the queue” is now testable against evidence about this person.

Coaching or a delivery manager under Alex would leave release authority with the person who has declined to give it up, so added support is not enough on its own. The evidenced choice is added leadership with authority: a head of engineering who owns the release process and the transfer, reporting to Ines, with Alex keeping technical direction. If Alex will not accept the narrowed role, the choice is replacement. Recruitment then follows a role design, a written statement of the job’s responsibilities, authority and expected results, not a search for someone willing to repeat the plan more confidently.

{id: fix-decisions-before-hiring--when-the-investor-proposes-an-appointment}
## When the Investor Proposes an Appointment

Investors take part in key appointments in five ways, and the ways carry different weight: proposing a role, introducing candidates, taking part in selection, approving compensation and assessing the people already in post. Only some of these are rights.

**A formal approval right.** Larkspur’s fictional shareholders’ agreement is the contract between the company’s owners that states their rights. Under it, hiring or dismissing an executive officer (one of the company’s most senior managers, such as the head of technology, product or finance), or changing their pay, needs the consent of one particular director: the one appointed by the lead investor, the investor that led the negotiation of the last investment. Agreements often call a decision like this a **reserved matter**: it cannot go ahead without a specified additional approval. At Larkspur, then, the appointment is the board’s to make and one named director’s to consent to.

Clauses of that shape exist in real agreements, and one filed example shows what they look like in practice. That agreement lists “hire, terminate, or change the compensation of the executive officers” among the board matters requiring the approval of the preferred directors. **Shares** are the units into which a company’s ownership is divided, so whoever holds them owns that fraction of the company. The preferred directors are elected by the holders of **preferred shares**, a class of shares carrying extra rights beyond ordinary ownership; in that filed agreement, it is the investors in the company that filed it who hold those shares. The real clause illustrates the shape of the mechanism; it does not supply Larkspur’s fictional rule, which turns on a single investor-appointed director rather than on a majority of preferred directors. [S76: Avalyn Pharma investors’ rights agreement](https://www.sec.gov/Archives/edgar/data/1540171/000119312526147573/ck0001540171-ex4_2.htm)

**A funding condition.** A **term sheet** is the short document that states the main proposed terms of an investment before the full contracts are written. **Closing** is the point at which the investment is completed and the money is paid. A funding round whose term sheet makes “a chief product officer in place before closing” a condition attaches money to an appointment.

**Influence.** Morgan is the technology adviser to Larkspur’s investor, and is not the investor-appointed director. An introduction from Morgan’s network, or the investor director’s view that Priya “has not run product at scale”, is influence: real, worth hearing, and not authority.

The chapter [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides) separates the three; the chapter [Choose the Right Help: Compare Investor Support With Other Options](#help-that-changes-capability) covers what investor recruiting support can and cannot supply.

Here is a fictional proposal. Suppose that, later in the same scenario, the second country has signed customers faster than expected, the funding round has closed, so the money has been received, and the board has approved and funded the second team.

The investor director proposes a chief product officer (**CPO**), an executive who would lead product direction and prioritization, above Priya. Two teams and two countries, the argument runs, need product leadership that has done this at scale. Morgan has two candidates in mind, one of them a former product executive at another company in the investor’s **portfolio**, the set of companies it has put money into.

Ines neither accepts nor refuses the proposal. She treats it as the hypothesis test above, applied to a role that does not yet exist: what must a CPO enable that Larkspur cannot do today, and what evidence shows the capability is missing?

The pricing trace found product decisions waiting for Priya, and the catalogue removed that wait; since then no product decision has been the queue. The trace did not test the board’s concern: prioritizing across two teams and two countries, and building a product management function rather than doing product management. That is a gap in the future, not a failure in the present. Three responses are compared, with fictional figures:

| Option | What it enables | Cost and timing | Risk |
| --- | --- | --- | --- |
| Recruit an external CPO | Prioritization across teams and countries; a leader who has built a product function before | About €180,000 a year plus equity (an ownership stake, or a right to acquire shares later); four to six months to start; a search fee if a recruitment firm is used | Priya reports into a role she was not offered and may leave with the customer knowledge the second country depends on; the new leader inherits a system they did not design |
| Develop Priya into the role | The same prioritization, learned in the company that needs it, with the customer knowledge kept | Coaching of about €15,000; explicit accountability for both teams’ product decisions; a dated review | If the gap is real and development does not close it, six months are lost |
| Add narrower support now | A senior product manager for the second country and the second team, so Priya’s time goes to prioritization rather than one country’s rules | About €95,000 a year for a role the board has already approved in the second team, funded from the operating budget; two to three months to start | Does not by itself address prioritization if that turns out to be the gap |

Ines chooses the third and the second together. The senior product manager is recruited now. Priya takes explicit accountability for prioritization across both teams, with a coach.

The evidence is reviewed in six months, and what will count as evidence is agreed now, when the support begins, not chosen at the review. Ines will examine three records:

- **Decisions made on time.** Each priority decision across the two teams is given a date when it is raised. Was it made by that date?
- **Results checked.** Each decision states the result it is meant to produce, such as a shorter wait or a customer signed. Did someone go back and check whether that happened? Making a decision and checking its result are separate, and the review looks for both.
- **Customers’ waiting time.** How long do second-country customers wait for a requested change, measured by the same kind of trace as above? Did that wait stay within the target agreed at the start?

The scenario gives that target no number. What matters is that the comparison is fixed before the results are known.

| Element | What was decided |
| --- | --- |
| Rejected | An external CPO now, because the evidence does not yet show the capability missing and the search would consume the six months in which the evidence will arrive. Dismissing the question, because the gap the board describes is plausible |
| Funding and headcount | The senior product manager is one of the five roles the board approved and funded for the second team. The hire therefore sits inside the approved headcount plan, as the billing engineer’s position did, and Ines appoints within her delegation. The coaching comes from the operating budget under the same delegation |
| If the role had been outside the plan | It would have been the board’s decision whatever cash the operating budget held, because available cash does not establish hiring authority (see the chapter [Clarify Authority: Decide Who Decides Before You Disagree](#decide-who-decides)) |
| What a CPO would need | A CPO would be a new executive position outside the headcount plan. It needs the board’s approval of the role and its budget and, under the reserved matter, the investor director’s consent to the hiring and the compensation. Dismissing an executive officer, or changing an executive officer’s pay, Priya’s included, would need the same consent. The clause names hiring, dismissal and pay, and nothing else. A change to Priya’s title or reporting line that left her pay untouched is not named, so Ines would check the agreement’s actual wording before acting rather than assume either answer |
| Authority | Ines appoints below her and decides this. Priya is not dismissed and her pay is unchanged, so no consent is triggered now. Morgan’s two candidates are told the role is not open now and would be assessed against the same role design if it opens |
| Evidence that would change the decision | At the six-month review: priority decisions missing their agreed dates, their intended results left unchecked, or second-country customers waiting longer than the agreed target. Any of these reopens the diagnosis; none settles it. The response is another trace, not a search (see below) |

The first two — decisions made late, results left unchecked — point at the product decisions themselves. The third does not, because a customer can wait for reasons this chapter has already separated: a specialist queue, an incident that took the protected day, or country rules still written into the invoicing module.

So the response is another trace. It asks of each waiting day whether a product decision was late or whether the delay sat in engineering, knowledge or operations. It tests the product responsibilities the role design actually assigned — decisions made by their agreed dates, and their intended results checked — rather than lateness alone, because a decision made on time whose result nobody ever checked is a product failure too.

Only where that trace finds those responsibilities unmet does the CPO hypothesis become testable. The role design is written now, so a search, if one follows, follows a design rather than a candidate.

A candidate from the investor’s network is assessed against the company’s role design like any other, with references the company takes itself. And any relationship that could create a conflict of interest, such as a candidate the investor has worked with before, a search firm the investor pays or a director who would prefer a familiar face, is declared and recorded rather than assumed away. The company appoints and manages the person and remains accountable for the result; an investor who introduced the candidate does not thereby own the outcome.

The role design must spell out the implications for the rest of the organization, because the title says nothing about them:

| Responsibility | Today | With a senior product manager | With a CPO |
| --- | --- | --- | --- |
| Product priorities across teams | Priya, with Ines resolving trade-offs | Priya | The CPO, with Ines resolving trade-offs |
| Product management for one team or country | Priya and one product manager | The senior product manager for the second country and the second team | Product managers reporting to the CPO |
| Design and user research | The two designers report to Priya; research is done by the product managers | Unchanged | Report to the CPO; a research capability would be the CPO’s to propose and fund |
| Engineering | Alex; the release process and the transfer remain his | Unchanged | Unchanged; a proposal that bundles product and engineering under one executive is a proposal about Alex’s role, and triggers the assessment above |

Success for a role is assessed on what it was appointed to enable, stated at appointment:

- **The senior product manager:** the second country’s rule decisions no longer wait for Priya, which the next trace shows; those decisions are made by their agreed dates and their intended results are checked. Second-country customers’ waiting time is watched but is the company’s measure, not this role’s alone, for the same reason it is not the CPO’s: the trace can put those days in engineering, knowledge or operations.
- **Priya:** by the review date, both teams’ priority decisions have been made by their agreed dates, and their intended results have been checked.
- **A CPO, if one is appointed:** the priority decisions across both teams are made by their agreed dates and their results are checked. Customers' waiting time is the company's measure, not this role's alone, because the trace can put those days in engineering, knowledge or operations; what the CPO is accountable for is the decisions and the product function built to make them.

An appointment made without that statement is judged, later, on whatever the board is worried about at the time.

The opposite movement, a plan that must shrink rather than grow, has its own chapter: [Scale the Team Down: Decide What Work Stops, Not Just Who Leaves](#anatomy-of-a-layoff) follows a reduction from the investor’s request to the people it affects.

{id: fix-decisions-before-hiring--cheaper-locations-do-not-automatically-save-money}
## Cheaper Locations Do Not Automatically Save Money

Nearshoring and offshoring mean locating work in other countries, with “near” describing geographic or time-zone proximity. Cultural similarity is often assumed alongside it and must be checked separately. The labels don’t determine the delivery model. A company can hire employees, use a supplier, open its own development office or combine arrangements.

A wage comparison is only one input. Include recruitment, management, onboarding of new staff, travel, knowledge transfer, the supplier’s margin (what it charges above its own costs), legal and employment arrangements, departures, rework and the period of overlapping teams. Add the time before a new team can own useful outcomes.

In a fictional case, replacing €1 million of annual external development spending with a €650,000 team of the company’s own appears to save €350,000. If the transition costs €250,000 and recurring coordination and specialist support add €150,000 a year, the recurring cost is €800,000 and the annual saving after transition falls to €200,000 before any quality or delivery effects. Even with a full year at the lower operating cost, the €250,000 transition payment makes first-year spending €1.05 million, €50,000 above the original. The comparison is between supplier invoices and the full cost of an employed team, not between two salary bills; the numbers illustrate the model, not a benchmark for any location.

The more important question is **whether the work can be transferred coherently**. If every decision depends on a small group elsewhere, lower hourly cost may come with more waiting and rework; Larkspur’s queue would acquire a time zone. A bounded product or service responsibility, adequate context and a clear escalation path, the agreed route for getting help or a higher-level decision, can matter more than geography.

![The cost of a team change includes transition spending and continuing coordination and support, as well as pay.](private-techuity/posts/22-fix-decisions-before-hiring/assets/images/22-fix-decisions-before-hiring/full-cost-of-a-team-change.jpeg)

**Figure 2:** *Compare the complete delivery model over time, including the cost of reaching it. The salary on the price tag is only one item. The basket adds one-time transition costs, such as recruitment and the overlap of old and new teams, to the costs that continue every year. “Total cost of ownership” is the drawing’s label for the whole sum over the period compared: setting the arrangement up, running it and changing over to it.*

{id: fix-decisions-before-hiring--preserve-the-knowledge-only-a-few-people-hold}
## Preserve the Knowledge Only a Few People Hold

Code and documentation don’t hold all the knowledge. Some of it is why a customer behaves differently, which earlier move to a new system failed, and which operational symptoms precede a problem. Restructuring can remove that knowledge before a replacement team knows it’s missing.

Make transition obligations explicit. Which business capabilities must continue? Who can independently operate and change them? How will the receiving team demonstrate readiness? What overlap is necessary? What evidence will show that the handoff is complete?

A document delivered isn’t capability transferred. The receiving team should perform the work under realistic conditions. At Larkspur, the test is that the billing engineer releases a new country rule change without either specialist reviewing it and the monthly reconciliation shows no errors. Don’t release the outgoing team because a calendar milestone has arrived while critical operational dependencies remain unresolved.

{id: fix-decisions-before-hiring--organizational-health-is-an-operating-signal}
## Organizational Health Is an Operating Signal

Overload, persistent vacancies, loss of key people and repeated priority changes can weaken the company’s ability to deliver. They aren’t cultural preferences to discuss once the financial targets are met. They can decide whether the targets are feasible at all.

**DORA** (DevOps Research and Assessment), the research program on software delivery and organizational performance whose lead-time measure appeared in the trace, associates unstable priorities with poorer productivity and greater burnout in its 2024 survey analysis. [S15: DORA 2024 report](https://dora.dev/research/2024/dora-report/) The practical lesson is to investigate the source of instability and its consequences, not to infer a precise financial loss from a survey relationship.

Choose measures that help management act: dependence on particular individuals, unplanned work, sustained overload from on-call duties (being available to respond to problems outside planned working time), time to fill material roles, and the team’s understanding of priorities. Use qualitative evidence alongside counts. A company can meet a hiring target while losing the knowledge or trust the work depends on.

{id: fix-decisions-before-hiring--one-boundary-question}
## One Boundary Question

The staffing choice above assumes the invoicing module stays Larkspur’s to change. Suppose instead that a parent company (a company that owns Larkspur), or a standard imposed across a group of related companies, mandated a shared billing platform. The third specialist’s job would then be integration, connecting Larkspur’s software to that platform, rather than rule changes, and the knowledge worth transferring would be different. Decide where that boundary sits before designing the roles around it: the chapter [Plan Acquisitions and Separations: Account for Extra Work, Not Just Expected Value](#acquisition-adds-work-first) treats the choice of how deeply to integrate, and [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design) its design consequences.

A boundary that large is usually designed with outside help, which raises a second question: who coordinates the work once the design is settled? An investor’s adviser can facilitate that design but shouldn’t become the permanent coordinator of every dependency by default. If the adviser is still at every planning meeting a year later, ask which of two things that is: a continuing service the company has chosen to buy, with its cost and responsibilities agreed, or an internal responsibility the team agreed to hold and cannot yet perform. Only the second is a failed transfer; the chapter [Set the Terms of Help: Agree the Work, Authority and Handover](#useful-engagement) is where the choice between them is made explicit.

{id: fix-decisions-before-hiring--the-people-plan-belongs-in-the-value-plan}
## The People Plan Belongs in the Value Plan

For every material initiative, identify the skills, leadership time and operating capacity it needs. Distinguish hiring from capability: a filled vacancy doesn’t mean a team can perform independently. Put the learning period in the economic and delivery plan. Distinguish funded roles from roles conditional on new money, and agree when those conditions must be resolved.

Tell investors and teams the same plan. Don’t promise employees durable roles while privately treating their funding as provisional, or call a capability indispensable while approving its removal without a replacement. When cost reduction is necessary, state what work will stop and which risks remain. When a leader needs development, define the support and the evidence of progress. Judge an organizational change by the work people can now carry out: decisions made, responsibilities understood and knowledge transferred, with the cost of the transition and the treatment of the people affected included.

With the queue reduced to its knowledge core and the hire reshaped to close it, Larkspur still has the system constraint from the finding: country rules coupled into the invoicing module. The rules are written into the billing code itself, so serving a new country means changing that code. There are three candidates: buy a supplier’s tax-and-billing service and configure it for the second country through settings; move the country rules out of the invoicing module into a separate part with an interface, an agreed way for software parts to exchange information, that Larkspur owns; or replace the core billing system. The chapter [Plan for Growth: Decide What (Not) to Change in Your Systems](#growth-into-design) compares the three against the same customer need, date, ongoing responsibility and cash limit, and chooses one.

{id: fix-decisions-before-hiring--questions-to-consider}
## Questions to Consider

1. *Trace one real piece of work through your company from request to outcome. How many days are building, and how many are waiting for a decision or for one person?*
2. *Which waits could be removed by changing who is authorized to decide, and which remain because knowledge sits with one or two people?*
3. *If a location or supplier change is proposed, does the comparison include transition, coordination, rework and the period before the new team can own outcomes?*
4. *Which planned hires are funded, which are conditional on money not yet received, and what evidence would change their shape?*

{id: fix-decisions-before-hiring--to-probe-further}
## To Probe Further

- **[How Do Committees Invent?](https://www.melconway.com/research/committees.html)** — Melvin Conway, Datamation, 1968; full text on the author's site.  
  *The paper behind Conway's law, the observation that a system's design tends to mirror the communication structure of the organization that built it. It explains why following a piece of work through the company, as this chapter recommends, reveals the shape of the software too.*
- **[Team Topologies](https://teamtopologies.com/book)** — Matthew Skelton and Manuel Pais, IT Revolution Press, 2019; second edition 2025.  
  *Gives the question of shared methods versus local decisions a vocabulary. It shows how a platform team, which supplies shared technical services, or an enabling team, which helps other teams acquire skills, can support local product decisions without creating a central queue.*
- **[The Mythical Man-Month: Essays on Software Engineering, Anniversary Edition](https://www.pearson.com/en-us/subject-catalog/p/mythical-man-month-the-essays-on-software-engineering-anniversary-edition/P200000000149/9780201835953)** — Frederick Brooks, Addison-Wesley, 1995 edition.  
  *The source of the observation that adding people to a late project makes it later, and the classic argument for treating a headcount target as a transition cost.*
- **[A Novel Approach for Estimating Truck Factors](https://arxiv.org/abs/1604.06766)** — Guilherme Avelino, Leonardo Passos, Andre Hora and Marco Tulio Valente, International Conference on Program Comprehension, 2016.  
  *A measurable check on this chapter's warning about knowledge held by a few people. A truck factor estimates how many key developers would have to leave before a project is incapacitated. The authors estimate it at two or fewer for about two thirds (65%) of the 133 open-source projects they studied. Open-source projects publish their code under a licence that lets anyone use and change it.*
- **[Offshoring Information Technology: Sourcing and Outsourcing to a Global Workforce](https://www.cambridge.org/core/books/offshoring-information-technology/0DE2B333FCFBC951A79177BA5B5736B4)** — Erran Carmel and Paul Tjia, Cambridge University Press, 2005.  
  *Older than current wage levels, but its cost categories for moving software work abroad are the ones the chapter's fictional location example asks you to include.*
