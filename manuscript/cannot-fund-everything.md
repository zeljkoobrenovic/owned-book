{id: cannot-fund-everything}
# 11. You Cannot Fund Every Good Project at Once

![You Cannot Fund Every Good Project at Once — logo](private-techuity/posts/09-cannot-fund-everything/assets/images/09-cannot-fund-everything/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to choose a combination of work that fits both the cash and the team time available, and revise the whole combination when a test fails.

> **WHY INVESTORS CARE:** Larkspur’s investor agreed to fund growth on one assumption: the company can take on many more new customers without adding staff at the same rate. The work that tests that assumption needs the same engineers as an improvement the company has already promised. A plan that gives the same people to both shows up later as delays, in front of the board where the investor sits.

> **WHY YOU SHOULD CARE:** A plan that fits the cash but not the team time, or ignores an agreed obligation, gets overrun by the limit nobody counted. Choosing a combination the company can deliver is what makes its commitments worth something.

> **KEY POINTS:**
>
> * Choose a **combination of work the company can actually deliver**. Several attractive projects can fit the cash limit and still exceed the team time available.
> * Sort the requests by **what they rest on**: an agreed obligation, tested customer evidence or an assumption. A growth target starts the discussion; it does not choose the project.
> * Make the **next review part of the decision**, and revise the whole combination, not just one project, when a test fails or new evidence arrives.

Larkspur is the fictional company this book follows; it sells scheduling software to maintenance businesses. Its investor wants faster growth. Priya, the product leader, has requests for a new customer portal, an online workspace where customers manage their own work. Alex, the technology leader, wants to improve recovery from system failures. The customer team wants simpler setup for new accounts. Each request has a plausible benefit. They can’t all use the same people at the same time.

A **company investment** commits resources now in the expectation of a future benefit. **Team capacity** is the time and capability people have available to do the work. Choosing investments needs both a cash plan and a capacity plan. This chapter shows one way to make the choice, as a proposed working method illustrated with fictional figures.

{id: cannot-fund-everything--competing-requests-two-limits}
## Competing Requests, Two Limits

In this **fictional planning exercise**, Larkspur’s board sets one limit for the first hundred days after **closing**, the day the investment is completed. The board is the group of directors who oversee the company and approve its major decisions; the investor has a seat on it. The limit is up to €500,000 of additional cash and 24 engineer-weeks. This book calls that approved limit the **envelope**. One **engineer-week** means one person’s working time for one week; it’s a planning estimate, not a guarantee that people are interchangeable.

The envelope limits what the company may **commit** in those hundred days: the money it agrees to spend and the weeks it assigns to named work. It does not promise that the work is finished, or every invoice paid, by day 100. Some approved work and some payments run past that date, so the record keeps three things apart: committed, spent and finished.

It is the same plan that the chapter [The First Hundred Days: Turn Expectations Into a Funded Plan](#first-hundred-days) follows from the **diligence** findings, the results of the checks the investor made before investing, to the day-100 review. This chapter shows how the combination inside it was chosen and then revised. Ines, the chief executive officer (CEO), proposes the combination. The board approves it on day 0, at the meeting that adopts the operating plan: the agreed work for the period, with people and money assigned.

Routine operating work is already budgeted. The envelope is a change budget: it pays for improvements. One of them is not optional, because it serves a requirement the company has already agreed. That **recovery requirement** has two parts. After a failure, dispatch must be working again within four hours; dispatch is the part of the product customers use to assign each day’s jobs. And no more than fifteen minutes of schedule updates may be lost.

The cash estimates concern additional spending, such as specialist help and new services. Existing employees’ pay is already in the ordinary operating budget; their available time is shown separately. The amounts are one-time costs; the one continuing cost this plan creates appears in the decision record below. The identifiers in the table (REC-1, ONB-1, KNW-1) are the ones the diligence findings and the [Practical Tools for Ownership and Technology Decisions](#toolkit) use for the same work.

The table has five rows: four proposals that need additional cash, and one training item that needs none.

| Proposed work | Additional cash | Engineer-weeks | Intended result |
| --- | ---: | ---: | --- |
| Improve and test service restoration (REC-1) | €80,000 | 4 | Meet the recovery requirement: dispatch back within four hours, no more than fifteen minutes of updates lost |
| Simplify one customer-setup step (ONB-1) | €180,000 | 12 | Test whether customers can start using the product with less help |
| Teach a second engineer to release and recover the scheduling engine (KNW-1) | €0 | (about 8) | Remove a dependency on one person |
| Build the full proposed customer portal | €220,000 | 12 | Offer a broader way for customers to manage their work |
| Test the portal need with customer research | €20,000 | 2 | Learn which problems would justify a larger product commitment |
| **All proposed work** | **€500,000** | **30, against 24** | **Fits the cash limit but exceeds available engineering time** |

The money fits. The time does not: the four priced rows need 30 engineer-weeks, six more than the 24.

The training row’s figure is in brackets because it is outside that comparison. It is about eight protected person-weeks, none of them from the 24: four from the specialist and about four from the second engineer. Those weeks were set aside before the 24 were counted. So they add nothing to the shortfall, and they can’t be used to close it.

The second row concerns **setup**, the work of helping a new customer configure the product and start using it. Other chapters call the same work onboarding or implementation, and the people who do it the implementation team. The last two rows are stages of one idea: the portal research comes before a full build. The table shows what funding both stages would require; the company still has to decide whether the research justifies that later commitment.

KNW-1 changes neither total. The **scheduling engine** is the software that works out which job goes to which person and when. Diligence found that only one specialist could **release** it, meaning put a new version into use, and recover it after a failure. KNW-1 has that specialist teach a second engineer to do both. It needs no additional cash, because both people are existing employees paid from the operating budget.

Being paid is not the same as being free, so the plan counts their time too. The specialist gives four weeks. The second engineer, who already works on the engine, spends about the same four weeks alongside the specialist during the first 60 days, on real releases and a recovery rehearsal. That makes about eight person-weeks in all, the figure in the table. None of it comes from the 24, which were counted after both people’s KNW-1 time had been set aside, so no week is counted twice. The price is paid in ordinary work: Alex postpones non-urgent changes to the scheduling engine for those weeks, and urgent fixes still come first. The row is in the table so that nothing else can claim that time.

The totals are only a first check. Confirm that the required specialists are available in the weeks each project needs them. Twenty-four engineer-weeks spread across several teams or months may not support a plan that needs the same specialist for twelve consecutive weeks.

{id: cannot-fund-everything--sort-the-rows-by-what-they-rest-on}
## Sort the Rows by What They Rest On

Before choosing among the rows, establish what each one depends on. The table gives every row the same shape; the rows are not the same kind of choice.

**An agreed obligation.** Some work protects an existing commitment: continuing a contracted service, meeting an applicable requirement or resolving a risk the company has decided it can’t accept. At Larkspur the recovery requirement above is one: Ines approved it, and customers plan their mornings around it. The restoration row is what proving and meeting it costs. KNW-1 is the other obligation on the table: the company decided not to carry the risk of one person being the only one who can release and recover the scheduling engine. That doesn’t make every proposed security or maintenance project mandatory. Establish the specific obligation or failure scenario, the minimum acceptable result and the feasible alternatives, with specialist interpretation where necessary. The company still chooses how to meet the need.

**An expected result.** An **investment thesis** is the investor’s explanation of why the investment should succeed; it is a revisable prediction, not an instruction. Larkspur’s says the company can grow faster. “Grow faster” could mean winning more customers, getting customers who have already signed started on the product, or helping existing customers buy additional services. Those are different problems, and more marketing won’t fix a setup process that can’t handle the customers already sold. For each row, ask what evidence supports the intended result: a customer request, a measured problem and a guess deserve different confidence.

**Dependencies and displaced work.** The **opportunity cost** of a choice is the benefit of the best alternative you give up. If two rows need the same specialist, approving one delays the other even when both have funding. Include preparation, transition, the cost of keeping the result running afterwards and the work each row pushes aside.

**What a smaller step could teach.** An **experiment** is a limited test designed to learn whether an assumption holds. Its immediate result may be a better decision rather than sales income. The portal research row is one; it exists because the portal’s benefit is the least supported claim on the table.

{id: cannot-fund-everything--the-condition-that-applies-here}
## The Condition That Applies Here

Having an investor changes the conditions of the decision. Establish the actual funding, authority and deadline before committing. In this exercise the condition is specific. Larkspur’s growth funding, the money the investor put in to pay for expansion, was agreed on a plan with one central assumption: the company can set up many more new customers without the implementation team growing at the same rate. The plan’s own test is one and a half times as many new customers with the same team.

That gives the setup row a priority the company’s own view might not. The setup change is run as a **pilot**, a limited trial, with a first **cohort**: a group of customers set up the new way and measured together. The pilot’s evidence is a condition of the next expansion step. Other funding arrangements set other conditions; the chapter [Match the Funding to the Work](#raise-what-you-need) compares them, and the [Introduction & Reading Guide](#introduction) explains how the book’s alternative scenarios relate to each other.

A board that wants the expansion date without funding the necessary capacity has an unresolved choice. **Present the feasible combinations.** Don’t turn the gap into an unrecorded demand for the team to work harder. A plan chosen by team preference or the loudest request has a specific weakness. It leaves out three things: which limit will be reached first, how much money and team time are available, and what result the funding was agreed on. So it can’t say what it displaces or what evidence would change it.

{id: cannot-fund-everything--select-the-combination}
## Select the Combination

Suppose the recovery requirement is agreed, the setup problem is supported by customer evidence and the portal’s benefit remains uncertain. Ines proposes restoration, the smaller setup change and the customer research, with KNW-1’s protected time alongside them, and the board approves that plan. It commits €280,000 and 18 engineer-weeks, leaving €220,000 and six engineer-weeks uncommitted. That uncommitted part is the **reserve**: money and time held back for later decisions.

Record the decision in full:

- **Chosen:** restoration, REC-1 (€80,000, four weeks); the setup change, ONB-1 (€180,000, twelve weeks); the portal research (€20,000, two weeks); and KNW-1 (no additional cash; about eight protected person-weeks, four from the specialist and about four from the second engineer, all outside the 24).
- **Rejected for now:** the full portal build. The unused money doesn’t make it feasible: its twelve engineer-weeks still exceed the remaining six, and its benefit still needs investigation. Deferred and recorded rather than rejected: hiring two implementation specialists (about €300,000 a year, recurring) and the second-country expansion, both waiting on the pilot’s evidence.
- **Funding and scarce capacity:** €280,000 of the €500,000 envelope, and 18 of the 24 engineer-weeks. The setup change needs the implementation specialist, the in-house person who sets customers up, for twelve consecutive weeks. Outside the 24, KNW-1’s time stays protected: the scheduling specialist’s four weeks and the second engineer’s four or so.
- **Continuing cost:** once built, the setup step needs upkeep of about €30,000 a year, starting in the next financial year. That is paid from the operating budget, not from the €500,000 envelope, so it is not part of the €280,000. It is recorded here because approving ONB-1 also commits the company to it.
- **Authority:** Ines proposes; the board approves the plan and the envelope. Inside the approved plan Ines authorizes spending; any draw on the reserve, and any change to what the envelope funds, stays with the board. The chapter [Decide Who Decides, Before You Disagree](#decide-who-decides) records that delegation rule. Alex is accountable for restoration and KNW-1, Priya for the setup change and the research.
- **Evidence that would change it:** research showing the portal is essential to retain a major customer, or the first setup cohort showing no reduction in effort.

The remaining €220,000 and six weeks provide room for uncertainty and for a later decision. They aren’t automatically savings or permission to start another project, and drawing on them is the board’s decision, not Ines’s. The review below shows what part of them was for.

An estimated score can help organize this conversation, but it shouldn’t hide that an agreed obligation, a speculative product opportunity and a learning step answer different questions. **Explain the trade-off in words** as well as numbers.

![A group of projects must fit both the cash budget and the available team and specialist time.](private-techuity/posts/09-cannot-fund-everything/assets/images/09-cannot-fund-everything/money-and-capacity-two-limits.jpeg)

**Figure 1:** *A project can be affordable and still be impossible to schedule.*

{id: cannot-fund-everything--make-the-commitment-in-stages-where-that-helps}
## Make the Commitment in Stages Where That Helps

A **funding stage** commits resources for a defined piece of work before deciding whether to commit more. The stage needs a useful outcome or a decision it can inform. Dividing a project into calendar phases doesn’t by itself reduce risk.

For the portal, the research is the first stage; the next decision might be to build a narrow function, investigate another need or stop. For restoration, the stage is the test itself: can the service recover within the agreed conditions?

Check the connections between stages. Can the company operate safely if it stops after the first? **Who maintains anything already delivered?** What spending is unavoidable once the first commitment is made? The setup step’s yearly upkeep is that kind of cost, which is why the record carries it from day 0. Some transitions require a larger coordinated commitment, which should be visible from the start.

![An initial funded test leads to a review before the company expands, changes or stops the work.](private-techuity/posts/09-cannot-fund-everything/assets/images/09-cannot-fund-everything/staged-investment-with-review.jpeg)

**Figure 2:** *Commit enough to answer the next decision, then use the evidence before committing more.*

{id: cannot-fund-everything--review-the-combination-not-just-each-project}
## Review the Combination, Not Just Each Project

New evidence can change the whole plan, and in this exercise it did. Restoration had been approved at €80,000 and four engineer-weeks. By the day-45 test all of it had been spent: on a **restore environment**, a separate set of systems on which the service can be rebuilt; on access to the **backups**, the saved copies of the company’s data; on backing up schedule data every fifteen minutes instead of once a night; and on the test itself.

The test failed both parts of the requirement. The service came back after eleven hours against the agreed four, for two reasons. The account that could read the backups belonged to an engineer who had left, so nobody held a working **credential**, the information that proves someone may access a system. And the backup could only be loaded by the version of the database software it was made with, which could no longer be installed. (The database stores and organizes the application’s data.)

When the service did come back, its data was from the previous night. The fifteen-minute backups existed, but nobody had written down the step that applies them, so a night of schedule updates was lost against an allowed fifteen minutes. The chapter [Prove You Can Restore, Not Just That You Back Up](#prove-you-can-restore) walks through the failure.

The €80,000 and four weeks are **sunk cost**: resources already spent that can’t be recovered. They belong in the record, but they are not a reason to spend more. The next commitment depends on remaining costs and expected benefits, and here the obligation has not gone away.

The correction has three parts. The restore environment is kept on the same database version as the live service. The backup credentials move out of one person’s account into a single, centrally controlled store for access credentials, which records who may use them. An emergency procedure that two named people can carry out goes with it. And a written rehearsal includes the missing step that applies the fifteen-minute backups. With a retest, this needs about €20,000 and two more engineer-weeks.

Those can only come from the reserve, and the reserve is the board’s. Ines’s delegation covers spending inside the approved plan; it excludes any draw on the reserve and any change to what the envelope funds (the chapter [Decide Who Decides, Before You Disagree](#decide-who-decides) records the rule). So around day 47 Ines asks the board, and the board approves. The revised commitment:

- **Chosen:** the correction and a retest by day 85 are added, taking restoration to €100,000 and six engineer-weeks in total; the setup change, KNW-1 and the portal research continue unchanged. Total committed: €300,000 and 20 engineer-weeks allocated; €200,000 and four engineer-weeks remain in reserve.
- **Rejected:** pausing the setup change to free its specialist for recovery work, because its cohort evidence is the condition on the expansion decision; and starting the portal build with the remaining money, which is still infeasible in capacity and still unsupported by evidence.
- **Funding and scarce capacity:** €20,000 and two of the six spare engineer-weeks, in the weeks the operations lead is available for the retest.
- **Authority:** the board, on Ines’s request, because the money is a reserve draw. Alex remains accountable for the result.
- **Evidence that would change it:** a second failed test, which would send the remaining reserve to recovery before anything else and delay the setup change’s second cohort.

The retest at day 85 passed both parts: dispatch was working again within four hours, with under fifteen minutes of schedule updates lost. It proved that for one kind of failure: the loss of the application environment, meaning the servers, database and configuration the service runs on.

The limit of that proof is about place. Larkspur rents its computing from a cloud provider, and a **cloud region** is one geographic group of that provider’s computing facilities. In the retest the region itself kept working, and Larkspur rebuilt its own systems inside it from the backups. If the whole region were unavailable, there would be nowhere in it to rebuild, and the service would have to come back in another location. That larger failure was not tested, and the record lists it as a risk that remains.

The sequence continued in the same way. At the day-100 review the board approved another €40,000 and the last four unallocated engineer-weeks for a data-quality step: checking and correcting each customer’s data before setup begins. The first setup cohort had pointed there, because about 40% of the setup hours that remained traced to problems in customers’ data. That took the envelope to €340,000 committed and all 24 engineer-weeks allocated, with €160,000 of cash still uncommitted.

Allocated does not mean finished, and committed does not mean spent. At day 100 the setup change had used about ten of its twelve weeks, and about €90,000 of its €180,000 had been **incurred**, meaning the work or services had been received. The other €90,000 falls due over the next two quarters, and the data-quality step’s four weeks were all still to come. The chapter [The First Hundred Days: Turn Expectations Into a Funded Plan](#first-hundred-days) carries that review, with a table of what was committed and what was incurred. The point here is that each step changed the combination, and each was decided by the body that owned the reserve.

Review the starting assumptions, actual spending, team burden and observed outcomes together, not project by project. A supplier failure may use the spare capacity. Customer research may invalidate an expected benefit. One completed improvement may remove the need for another. Decide which work continues, which changes and which stops.

{id: cannot-fund-everything--keep-the-record}
## Keep the Record

The [Practical Tools for Ownership and Technology Decisions](#toolkit)’s record for comparing investment choices and capacity (Tool 12) holds exactly the fields used above: the required commitments, the money and team time available, the options, the combination proposed, the first stages and the review decision. Fill it in before the board conversation, and update it after each review rather than starting a new one; the same shared decision record runs from the diligence findings to the record handed to the company’s next owner.

The setup change was chosen on customer evidence. Whether its benefit is real is a separate question, and the next chapter follows that one change from the work proposed to the measured customer and business result: [The Path From Roadmap to Revenue Is Fragile](#roadmap-to-revenue).

{id: cannot-fund-everything--questions-to-consider}
## Questions to Consider

1. *For your current plan, what are the cash limit and the capacity limit, which one is reached first, and does the plan say what is already budgeted and what it must still fund?*
2. *Which of your commitments rest on an agreed obligation, which on tested evidence and which on an assumption? Are they being compared as if they were the same kind of choice?*
3. *When the last plan was reviewed, was the whole combination reconsidered or only each project’s progress, and did the reserve go where the evidence pointed?*

{id: cannot-fund-everything--to-probe-further}
## To Probe Further

- **[2015 Letter to Shareholders](https://www.sec.gov/Archives/edgar/data/0001018724/000119312516530910/d168744dex991.htm)** — Jeff Bezos, Amazon.com, letter to the company’s owners, filed with the U.S. Securities and Exchange Commission (SEC) in April 2016.  
  *The short passage on Type 1 decisions, which are hard or impossible to reverse, and Type 2 decisions, which can be reversed and so can be made faster. Use it to ask how easily a proposed commitment could be undone. Staging is this chapter’s application of that question, not Bezos’s: a small first stage keeps more of the decision reversible.*
- **[Delusions of Success: How Optimism Undermines Executives' Decisions](https://hbr.org/2003/07/delusions-of-success-how-optimism-undermines-executives-decisions)** — Dan Lovallo and Daniel Kahneman, Harvard Business Review, July 2003.  
  *Explains why project forecasts are systematically optimistic and proposes checking a plan against comparable past projects, the evidence question in this chapter's sorting of the rows.*
- **[Investment Opportunities as Real Options: Getting Started on the Numbers](https://hbr.org/1998/07/investment-opportunities-as-real-options-getting-started-on-the-numbers)** — Timothy Luehrman, Harvard Business Review, July–August 1998.  
  *A manager's introduction to treating a staged investment as an option to continue, expand or stop. Keeping the option open has a cost; its value depends on the future choices it preserves and the cost of taking them, which is why this chapter asks whether the later stage can actually be funded.*
- **[The Principles of Product Development Flow: Second Generation Lean Product Development](https://archive.org/details/principlesofprod0000rein)** — Donald Reinertsen, Celeritas Publishing, 2009.  
  *A book about queues (work waiting for busy people) and the cost of delay (what is lost because work finishes later). Both ideas stand behind this chapter’s warning that 24 engineer-weeks spread across teams is not the same as one specialist available for twelve consecutive weeks.*
- **[The psychology of sunk cost](https://doi.org/10.1016/0749-5978%2885%2990049-4)** — Hal Arkes and Catherine Blumer, Organizational Behavior and Human Decision Processes, 1985.  
  *The experiments behind this chapter's rule that a review should weigh remaining costs and benefits, not what has already been spent.*
