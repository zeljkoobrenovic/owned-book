{id: understand-valuation}
# 5. Understand Valuation: An Estimate, Not a Fact

![Understand Valuation: An Estimate, Not a Fact — logo](private-techuity/posts/02-understand-valuation/assets/images/02-understand-valuation/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn to read a business's sales, profit and cash, then interpret a valuation: what is being valued, how the estimate was built and which assumptions your plan is asked to support.

> **WHY INVESTORS CARE:** Investors who manage other people's money, such as investment funds, may have to report an estimated value for each company they hold and explain the assumptions behind it. They will ask management which of those assumptions the operating plan can support.

> **WHY YOU SHOULD CARE:** A valuation may shape your team's targets: how fast sales should grow, what **margin** (profit as a percentage of sales) the business should earn and which costs should fall. Before accepting them, find out what the valuation was for and how it was built.

> **KEY POINTS:**
>
> * **Sales, profit and cash** answer different questions. A business can record a sale or a profit before the customer pays.
> * A valuation is an **estimate for a date and a purpose**. Its assumptions can become growth, margin and cost targets, which leaders should examine before accepting.
> * The **value of the business and the value of its shares** differ. The gap is debt and any other claims paid ahead of shareholders.

> **[DYSFUNCTIONS THIS SECTION ADDRESSES](#where-investment-goes-wrong):**
>
> * **Spending the Press Release** — Distinguishes sales, profit and estimated value from cash available to fund work.
> * **The Nodding Room** — Makes a valuation's growth and cost assumptions explicit before teams accept its targets.

Product and engineering leaders rarely need to produce a **company valuation**, but they need to understand one. Valuations drive ambitions, and the goals derived from them decide which work gets funded and which gets questioned.

The previous chapter showed that a headline figure can be a purchase price, new funding or a valuation. This chapter takes the valuation. Suppose a buyer says Rotaline is **worth** €60 million. Reading that figure starts with two questions: **what is being valued**, the operating business or the shares its owners hold, and **how was the estimate made**? Answering either requires understanding the business’s numbers, so this chapter has two stages:

- **Read the business’s numbers** introduces revenue, profit and cash flow, and ends with a short checkpoint on the €60 million.
- **Interpret a valuation** separates the value of the business from the value of its shares, works through three common ways of estimating value, explains why a funding-round price answers a different question, and ends with one operating assumption a leader can challenge.

{id: understand-valuation--read-the-businesss-numbers}
## Read the Business’s Numbers

{id: understand-valuation--revenue-earnings-and-cash-are-three-different-things}
### Revenue, Earnings and Cash Are Three Different Things

**Revenue** is the income a business records from selling its products or services during a period. It isn’t necessarily cash received in that period: a customer might pay later, or pay in advance for a service delivered over time.

**Profit**, also called earnings, is revenue minus costs. Which costs are subtracted depends on the question being asked, so there are several **profit measures**. One subtracts only the costs of selling and delivering the product; another also subtracts interest on borrowing and income tax. A company’s **income statement** records revenue and expenses over a period; **net profit** is the bottom line, after every cost has been subtracted.

{id: understand-valuation--ebitda-and-why-people-use-it-to-compare-operating-earnings}
### EBITDA, And Why People Use It to Compare Operating Earnings

Revenue shows the scale of sales but leaves out their cost: two companies with identical revenue can have different operating economics. Net profit includes those costs but also reflects borrowing, income taxes and asset-accounting charges. Income-tax rates differ between countries, so higher net profit needn’t mean that a company serves customers more efficiently.

Consider two fictional companies with identical operations and €2 million of profit before tax. At assumed effective income-tax rates of 20% and 30%, their net profits are €1.6 million and €1.4 million. The difference comes entirely from tax.

**EBITDA** stands for **earnings before interest, taxes, depreciation and amortization**. Interest is the charge for borrowing money. Here, taxes means income taxes, rather than every tax a business pays. An **asset** is a resource expected to provide future benefit. **Depreciation** and **amortization** are accounting charges that spread the cost of certain assets over time: depreciation commonly concerns **tangible assets**, physical items such as equipment; amortization concerns **intangible assets**, nonphysical resources such as qualifying software development or acquired customer relationships.

EBITDA leaves those items out to help compare operating earnings across businesses with different financing, tax circumstances and asset histories. A more heavily borrowed company can pay more interest without operating less efficiently; an acquisition can introduce amortization charges without worsening the acquired product. Removing these effects helps examine the operating business before deciding how to finance or own it. Comparisons still need consistent accounting policies and context, a point the **International Private Equity and Venture Capital Valuation (IPEV) guidelines**, which investors use when reporting estimated values, also make. [S52: IPEV valuation guidelines, section 3.4](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

**EBITDA provides a complementary view to net profit and cash flow analyses.** The excluded costs still affect value: lower taxes can benefit shareholders, interest must be paid, and assets may need replacing. EBITDA can't establish how much cash the business can spend. The U.S. Securities and Exchange Commission (SEC), which regulates companies reporting to U.S. investors, calls EBITDA a **non-GAAP measure**—one that departs from generally accepted accounting principles (GAAP), the standard accounting rules. Under the SEC's reporting rules, a measure that makes adjustments beyond EBITDA needs a different label and a calculation showing those adjustments. [S06: SEC non-GAAP guidance](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)

{id: understand-valuation--putting-the-measures-together}
### Putting the Measures Together

Consider Rotaline's simplified, fictional annual income statement in this chapter's scenario. All figures are millions of euros. Operating expenses include salaries, hosting, selling costs and development work charged against earnings in the year rather than recorded as an asset; assume no other income or charges.

| Step | Calculation | Result |
| --- | --- | ---: |
| Revenue | Sales recognized during the year | 20.0 |
| EBITDA | Revenue 20.0 − operating expenses excluding depreciation and amortization 16.0 | 4.0 |
| Operating profit, or EBIT (earnings before interest and taxes) | EBITDA 4.0 − depreciation and amortization 1.0 | 3.0 |
| Profit before tax | Operating profit 3.0 − interest 1.0 | 2.0 |
| Net profit | Profit before tax 2.0 − tax expense 0.5 | 1.5 |

The **EBITDA margin** is EBITDA divided by revenue: €4 million / €20 million = 20%. It describes an earnings relationship, not a bank balance.

**Cash flow** is the money that actually moves into or out of the business during a period. It can differ sharply from profit, because profit follows accounting rules about *when* a cost counts, while cash follows the payments themselves. Customers may pay months after a sale, debt repayments use cash without being an expense, and some spending is recorded as an **asset** rather than an expense. Suppose the business buys €1 million of equipment expected to last five years. All €1 million leaves the bank account now, but the income statement spreads the cost as **depreciation**, perhaps €200,000 a year, so this year’s profit falls by only €200,000. Development work that meets the accounting conditions can be treated the same way: recording it as an asset spreads its cost over later years, yet the salaries were paid in cash today. The chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#understand-cash-flow) develops that distinction.

An **adjusted EBITDA** measure adds further specified exclusions to an earnings calculation. Some may improve comparability; others may remove costs the business will keep incurring. Ask for a **reconciliation**: a line-by-line calculation showing how one reported number becomes another. Ask what each excluded cost is and whether the business will incur it again. Two later company case studies show why the adjective “adjusted” matters: the chapter [Visma: The Manager Stayed, the Owners Changed](#visma) traces how one year’s EBITDA became a higher adjusted figure by adding back acquisition costs, and the chapter [TeamSystem: Four Owners, One Continuing Business](#teamsystem) shows a positive adjusted EBITDA reconciling to a reported loss.

![A sale and its costs can be recorded before the customer pays, while company payments follow their own dates.](private-techuity/posts/02-understand-valuation/assets/images/02-understand-valuation/sale-profit-cash-timing.jpeg)

**Figure 1:** *Revenue, earnings and cash describe different events; timing connects them.*

{id: understand-valuation--checkpoint-what-can-you-now-ask-about-the-60-million}
### Checkpoint: What Can You Now Ask About the €60 Million?

Return to the opening number with the fictional income statement in hand. The table gives three results for the same year: €20 million of revenue, €4 million of EBITDA and €1.5 million of net profit. Before moving on, you should be able to ask three questions:

- If the €60 million is quoted as a **multiple** of one of these measures, that is, as a stated number of times annual revenue or earnings (for example, three times revenue), which measure and which period does it use: last year’s **result**, this year’s **forecast** or an **adjusted** figure?
- If that measure is adjusted, what has been **excluded**, and will the business keep incurring it?
- How did the business’s **cash** differ from its **earnings** over the year, and why?

{id: understand-valuation--interpret-a-valuation}
## Interpret a Valuation

{id: understand-valuation--a-valuation-is-an-estimate-built-on-assumptions}
### A Valuation Is an Estimate Built on Assumptions

**Valuation** estimates what a business or an ownership interest is worth at a particular date, for a particular purpose. A negotiated acquisition price, an investor’s estimate for reporting and a buyer’s maximum affordable price answer related but different questions. A technology budget shouldn’t treat them as interchangeable facts.

**Enterprise value**, often abbreviated EV, is what the operating business is worth as a whole, regardless of how it is financed. Think of it as the value of a house, before asking how much of it the bank owns through the mortgage. **Equity value** is what is left for the shareholders: enterprise value minus the debt owed to lenders, plus any spare cash in the business. In the house metaphor, it is the owner’s equity: the house’s value minus the outstanding mortgage. Like a house’s value before it is sold, it is an estimate of what the shares are worth, not money anyone has received. In the book’s simplified bridge:

**Equity value = enterprise value − net debt.**

**Net debt** is what the business owes lenders minus the spare cash it holds. A business with €25 million of borrowings and €5 million of spare cash has €20 million of net debt; that is the amount subtracted from enterprise value to reach equity value. Not all cash counts as spare: money needed to pay wages and suppliers, or cash that cannot be freely used, must stay in the business and is not offset against the debt. In a sale, the debt may stay with the business, be repaid from the proceeds or be refinanced (replaced with a new loan); each choice changes how much reaches the shareholders.

So the opening €60 million could be either figure. If it is **enterprise value** and **net debt** is €20 million, **equity value** is €40 million, before other claims and deal-specific adjustments (such as an agreed correction for the working cash left in the business at completion). If €60 million is instead the equity value, adding back the €20 million of net debt gives €80 million of enterprise value, again before those adjustments. Neither figure is money the company has received; the chapter [Understand Funding and Control: An Investment Announcement Is Not a Budget](#understand-funding-control) follows where the cash in a transaction actually goes.

**Valuation methods** organize **evidence** and **assumptions**; they don’t eliminate **judgment**. The December 2025 IPEV guidelines distinguish the purpose of the valuation, the method and inputs such as EBITDA. They guide the reporting of estimated values for private investments, meaning stakes in companies whose shares are not traded on a stock exchange; they don’t prescribe a company’s strategy or determine its negotiated sale price. [S52: IPEV valuation guidelines, introduction and section 3](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

{id: understand-valuation--three-ways-to-estimate-value}
### Three Ways to Estimate Value

There are three common ways to estimate what a business is worth: compare it with similar businesses (**multiples**), estimate the cash it will generate in future (**discounted cash flow**), or add up what it owns minus what it owes (**net assets**). Valuers often combine them, choosing the methods that fit the company and the evidence available. The International Private Equity and Venture Capital (IPEV) valuation guidelines describe all three and stress choosing appropriate inputs and genuinely comparable businesses. [S52: IPEV valuation guidelines, sections 3.2–3.9](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf) This chapter aims for practical orientation, not mastery: **multiples** get the fullest treatment because leaders hear them quoted most often, while **discounted cash flow** gets a single-payment illustration rather than a working model.

| Approach | Plain-language question | Main limitation |
| --- | --- | --- |
| Market comparisons | What values do comparable businesses or transactions imply for this company? | The companies, dates, accounting and prospects may not be sufficiently comparable. |
| Discounted cash flow: translate expected future cash into today’s value | What is the business’s expected future cash generation worth today? | The answer depends on uncertain forecasts, risk assumptions and value beyond the forecast period. |
| Asset-based valuation | What are the underlying assets worth, after accounting for relevant obligations? | Assets considered separately can miss the value of a functioning organization and its customer relationships. |

The methods do not all estimate the same thing. A multiple of EBITDA or a cash-flow model estimates the worth of the operating business as a whole, an **enterprise value**; you still need to subtract net debt to reach equity value. A net-assets calculation already subtracts what the business owes, so its result is already close to an **equity value**. Before subtracting net debt, check whether the method has already done so; otherwise the same borrowing is deducted twice and the shares look less valuable than they are.

{id: understand-valuation--market-comparisons-revenue-and-earnings-multiples}
#### Market Comparisons: Revenue and Earnings Multiples

A **valuation multiple** divides a value by a financial measure: a figure from the company’s accounts that reflects its size or performance, such as annual revenue, EBITDA or profit. If an operating business is valued at €60 million and annual revenue is €20 million, EV / revenue is 3×. If annual EBITDA is €4 million, the same €60 million value corresponds to 15× EBITDA.

To value a business with a multiple, the analyst works in reverse: take a multiple observed for **similar businesses** and apply it to this company’s figure. If comparable companies are valued at around 3× revenue, Rotaline’s €20 million of revenue suggests €60 million of enterprise value. If comparable companies are valued at around 12× EBITDA, Rotaline’s €4 million of EBITDA suggests only €48 million. The two answers differ by €12 million for the same business. The right response is not to pick the larger number but to ask which comparison fits Rotaline better, and why investors expect what they do from those comparable companies.

A revenue multiple can be useful when current earnings are low or negative and investors are assessing what a growing business could become. But revenue doesn’t reveal the cost of delivering it. Two businesses with equal revenue can need different staffing, infrastructure, selling effort and ongoing investment.

An EBITDA multiple makes the earnings figure explicit. It still leaves questions about how **sustainable** those earnings are and what cash is needed to maintain them. Comparisons must also be like for like: applying a multiple based on another company’s past, unadjusted EBITDA to this company’s forecast, adjusted EBITDA produces a precise-looking but misleading valuation. This is why the IPEV guidelines insist that the figures being compared cover the same period and use the same accounting basis, including how development costs are treated. [S52: IPEV valuation guidelines, section 3.4](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

**Growth is a business characteristic, not a separate valuation method.** Growth **expectations** can influence a revenue **multiple**, an EBITDA multiple or a cash-flow forecast. A mature business can also have valuable growth opportunities. A rapidly growing business still needs a credible relationship between future revenue, costs and investment.

{id: understand-valuation--discounted-cash-flow-make-time-and-investment-explicit}
#### Discounted Cash Flow: Make Time and Investment Explicit

Discounted cash flow, or **DCF**, estimates the cash a business is expected to produce in future years and translates each amount into its **present value**, what it is worth today. Money expected later is worth less today than the same amount in hand, for two reasons: money in hand could be invested in the meantime, and the future payment is uncertain. The **discount rate** is the annual percentage used to make that reduction. It reflects the return investors could earn elsewhere plus compensation for the risk that the cash arrives late, smaller or not at all. A DCF must also be clear about whose cash it counts. A model of all the cash the business generates, before paying lenders, gives an enterprise value; a model of only the cash left for shareholders after paying lenders gives an equity value. Each needs its own matching discount rate.

A small fictional example shows how discounting works. At an assumed 10% annual rate, €1 million today would grow to €1.1 million in a year: €1 million × 1.10. Discounting reverses that calculation: €1.1 million received in one year is worth €1 million today, that is €1.1 million / 1.10. A real valuation repeats this step for every year of a multi-year forecast, so a three-year transformation plan needs an estimate of the cash in each year.

A company does not stop existing when the forecast ends. A DCF therefore has two parts: the cash flows forecast year by year, typically for five years, and a **terminal value**, a single estimate of everything the business is worth after that, usually assuming it keeps growing at a steady rate. The terminal value often makes up a large share of the total, so small changes in its assumptions can move the valuation a lot. It should also be realistic: a spreadsheet that stops at year five does not mean the product stops needing development and maintenance in year six, and the terminal value should allow for that cost.

For technology leaders, DCF is the method closest to how their own plans work, because it follows cash year by year. A **platform migration**, for example, spends money now on building the replacement, pays to run old and new systems side by side during the transition, delivers savings later and still costs money to maintain afterwards. A DCF makes that sequence visible. Its weakness is that plausible-looking assumptions can hide an **unachievable plan**, so architecture and operating teams must help test whether the forecast’s timing and savings are realistic.

Aswath Damodaran, a finance professor at NYU Stern and a widely cited authority on valuation, connects a growth company’s value to three drivers: **revenue growth**, sustainable **margins** and **reinvestment**. Growth is not free: a larger business may need more funding before it produces more cash. [S53: Growth companies—value drivers](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/growthvaluedrivers.htm) For each growth assumption, ask how much product, engineering, selling and implementation effort it requires, and when the benefit can arrive.

{id: understand-valuation--asset-based-valuation-what-a-company-owns-minus-what-it-owes}
#### Asset-Based Valuation: What a Company Owns Minus What It Owes

An asset-based approach examines the value of assets and relevant **liabilities**, financial obligations such as debts and unpaid bills. It can be particularly informative when identifiable assets drive value or when continuing the business in its present form is doubtful.

For a software company, adding up historical development expenditure isn’t a sufficient valuation. Code written at great cost may have little use; a relatively inexpensive product may support valuable customer relationships. The cost of building an asset and what someone would pay for it answer different questions.

Who legally owns the product: its code, brand and the licences it depends on? Can the service operate without its parent, the larger company that owns it? Which shared systems, people and contracts would need replacing? These questions become especially concrete in a carve-out, where a business is separated from a larger organization. The chapter [Plan Acquisitions and Separations: Account for the Work, Not Just the Value](#plan-acquisitions-separations) examines that work.

![Comparable businesses, expected future cash and assets less liabilities offer different lenses on an estimated value.](private-techuity/posts/02-understand-valuation/assets/images/02-understand-valuation/valuation-lenses-and-assumptions.jpeg)

**Figure 2:** *A valuation depends on its purpose and assumptions; no single lens supplies an automatic price.*

{id: understand-valuation--a-funding-round-valuation-sets-ownership-not-the-companys-worth}
### A Funding-Round Valuation Sets Ownership, Not the Company’s Worth

In a separate scenario, a smaller Rotaline raises its first outside money: the founders agree an **equity valuation before new funding**, or **pre-money valuation**, of €8m. An investor pays the company €2m for newly issued shares. Ignoring fees, any other instruments that could later convert into shares, and differences in share rights, the **post-money valuation**, the equity value immediately after that funding, is €10m. The new investor owns €2m / €10m = 20%.

The company receives €2m, not the €10m headline valuation. If the same investor instead pays a founder €2m for existing shares, the company receives no new money. Nor should this equity valuation be compared directly with an enterprise value that treats borrowing differently.

A financing round sets a negotiated price for particular shares under particular terms. It doesn’t establish what every shareholder could receive in a sale, especially when payment rights differ. The product leader’s useful question is which assumptions about customer demand, growth and future funding justify the price, and which of them the team can test.

An early business with losses can’t sensibly use a positive EBITDA multiple as though current earnings established its value. A forecast or comparison still needs **assumptions about future sales, costs, reinvestment and uncertainty**. A corporate buyer may also expect benefits in its own operations. Those expected benefits belong in a separate explanation of what must change, who pays and how success would be observed.

{id: understand-valuation--challenge-the-assumption-that-each-customer-gets-cheaper-to-serve}
### Challenge the Assumption That Each Customer Gets Cheaper to Serve

Take the €60 million one last time, now as a model rather than a headline. Suppose the buyer’s model reaches that figure by expecting revenue to double over four years while the cost of **onboarding** each new customer, setting the customer up to use the product, falls by a third, on the reasoning that the work will spread across more customers. That is an **operating assumption**, and it lands on product and engineering. In the Rotaline onboarding example that the chapter [Test Revenue Assumptions: The Investor Judges the End of the Chain](#test-revenue-assumptions) costs out, each **implementation**, the configuration work that makes the product usable for one new customer, takes about 80 hours, much of it one specialist’s manual configuration. Selling to more customers does not shorten those 80 hours; it only multiplies them. The cost per customer falls only if someone changes how onboarding is done, for example by automating the configuration, and that change has to be planned, funded and built.

- **Which change produces the reduction?** A reusable setup step, a data import that customers can run themselves, or a narrower first-year target of customers whose data is already standard. Name it.
- **When does it become usable?** If the setup step needs two quarters (six months) to build and a first group of customers to prove it works, the model cannot assume a full year of savings; phase the benefit from the expected validation date and check what that does to the early margins.
- **Who funds the transition?** Building the change consumes cash and weeks of engineers’ time before it saves a single hour. That spending must sit in an approved plan, not be assumed by the valuation.

If the answers are “nothing specific,” “not yet” and “nobody,” the assumption is a **hope**, and the target derived from it needs revising. The chapter [Plan for Growth: Flexibility Needs a Customer and a Date](#plan-for-growth) works through choosing the system change that makes such an assumption true, and the chapter [Test Revenue Assumptions: The Investor Judges the End of the Chain](#test-revenue-assumptions) shows how to measure whether it did.

{id: understand-valuation--what-to-carry-forward}
## What to Carry Forward

You can now ask which value is being quoted and which assumptions need testing. The next question is what the investor gets back, and why the same company performance can return very different amounts: the chapter [Understand Investor Returns: Same Performance, Different Outcomes](#understand-investor-returns).

{id: understand-valuation--questions-to-consider}
## Questions to Consider

1. *The last time you heard a valuation for your company, was it enterprise value or equity value, at what date and for what purpose?*
2. *Which valuation assumptions is your technology plan being asked to support: growth in which customers, margins at what cost to serve, earnings sustained by what investment? Which change would make each one true, and is it funded?*
3. *Which adjusted measures does your company report, and do you know what each excluded cost is and whether it recurs?*
4. *After the last funding round, how much money actually reached the company compared with the headline valuation?*

{id: understand-valuation--to-probe-further}
## To Probe Further

- **[Beginners’ Guide to Financial Statements](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements)** — U.S. Securities and Exchange Commission, 2014, updated 2017.  
  *Start here if Stage 1 was new to you: a plain-language walk through the three main financial reports, the balance sheet (what a company owns and owes at a date), the income statement and the cash flow statement, behind this chapter’s revenue, earnings and cash section.*
- **[IFRS 13 Fair Value Measurement](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-13-fair-value-measurement/)** — International Accounting Standards Board, issued 2011.  
  *The formal version of “a valuation is for a date and a purpose”: the international accounting standard (IFRS stands for International Financial Reporting Standards) that defines **fair value**, the estimated price in an orderly sale at the measurement date, which your investor’s independently audited accounts are likely to use.*
- **[Valuation Approaches and Metrics: A Survey of the Theory and Evidence](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/valuesurvey.pdf)** — Aswath Damodaran, Stern School of Business, 2006 (published in Foundations and Trends in Finance, 2007).  
  *Optional depth: a free survey of cash-flow models, multiples and asset-based valuation, the three lenses this chapter only introduces.*
- **[Valuation: Measuring and Managing the Value of Companies](https://www.wiley.com/en-us/Valuation:+Measuring+and+Managing+the+Value+of+Companies,+8th+Edition-p-9781394279418)** — Tim Koller, Marc Goedhart and David Wessels, McKinsey & Company, Wiley, 8th edition, 2025.  
  *Optional depth: the practitioner reference behind many investor models, showing how a cash-flow forecast becomes an enterprise value and then an equity value.*
- **[Squaring Venture Capital Valuations with Reality](https://www.nber.org/papers/w23895)** — Will Gornall and Ilya Strebulaev, National Bureau of Economic Research working paper, 2017 (Journal of Financial Economics, vol. 135, no. 1, 2020, pp. 120–143).  
  *In 135 US unicorns (privately held companies reported to be worth more than US$1 billion), reported post-money valuations averaged about 50% above the authors’ modeled fair values. Shares in the same company can be worth different amounts: the model valued each share class (a group of shares carrying the same rights) from its contractual terms, and the latest preferred shares carry extra protections, such as being paid before ordinary shares in a sale. Pricing every share at what those preferred shares fetched can overstate the estimated value of the whole company, which is why this chapter treats a funding-round headline as answering a different question.*
