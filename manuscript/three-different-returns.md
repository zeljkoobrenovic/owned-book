{id: three-different-returns}
# 5. Understand Investor Returns: Same Performance, Different Outcomes

![Understand Investor Returns: Same Performance, Different Outcomes — logo](private-techuity/posts/03-three-different-returns/assets/images/03-three-different-returns/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** See how the same company performance produces three different investor returns, and learn what engineering can and cannot claim credit for in a sale gain.

> **WHY INVESTORS CARE:** An investment **fund** pools its investors’ money; the fund’s **manager** chooses what to buy and reports the results to those investors. A reported return combines the company’s performance with the purchase price, the borrowing and the sale. So the manager works on all three, and needs any claim about engineering to be one it can defend in that report.

> **WHY YOU SHOULD CARE:** Investor returns are often treated as a scorecard for product and engineering, yet price, borrowing and timing can change the result without any change in the work; that misreading shapes what you are asked to do.

> **KEY POINTS:**
>
> * Improving the business is **only part of an investment result**. Purchase price, borrowing, sale price, timing and changes in the investor’s ownership percentage also decide what the investor gets back.
> * **Hold the company’s performance fixed** and the money the fund receives at the sale, and its multiple of the money it invested, can still more than double, because only the price a buyer pays changed.
> * Explain the **technology contribution step by step**. Evidence about customers, costs and cash is needed before assigning part of a sale gain to engineering.

A company grows its earnings, yet its investor earns less than expected. Another company becomes more fragile while an investor receives a profit. To understand either result, we need to follow the investment as well as the business.

An **investment return** compares what an investor gets back — in cash received or in the value of what it still holds — with what it put in. There is no single way to measure it: some measures ask only how much came back, others also ask how long it took. And until an investment is sold, the value of what is still held is an estimate, so part of any reported return rests on a judgement rather than on cash in hand.

Leaders inside the company judge progress by customers served, products shipped and earnings. An investor judges the same company by the return on its holding, which also depends on the price it paid, the money it borrowed and when it sells. That is why an investor can press for a change that a product or engineering leader can’t justify from the business alone: the request often follows from the mechanics of the investment rather than from the product. Understanding those mechanics makes such requests easier to anticipate and to question.

{id: three-different-returns--one-operating-result-three-investor-outcomes}
## One Operating Result, Three Investor Outcomes

Here is the whole argument in one table. In a fictional **buyout**, a purchase of a controlling share of a company, a fund buys a company for €100 million, using €60 million of borrowed money and €40 million of its own. Investors call the purchase the **entry** and the eventual sale the **exit**.

Over five years the company raises its annual **EBITDA** from €10 million to €15 million. EBITDA, earnings before interest, taxes, depreciation and amortization, is explained fully in the next section. For now, read it as the company’s operating earnings before borrowing costs, income taxes and certain accounting charges. It is not cash in the bank. The company also repays €20 million of the debt, which is a separate assumption about the cash left over after its necessary spending.

Everything about the company’s performance is now fixed. The only thing that varies is the price a buyer pays at the exit, expressed as a **multiple** of EBITDA: how many euros of price per euro of annual EBITDA. Amounts are in millions of euros, written €m.

| Exit multiple | Fund receives | Multiple of its €40m |
| --- | ---: | ---: |
| 7× | €65m | 1.6× |
| 10× | €110m | 2.75× |
| 12× | €140m | 3.5× |

Same engineering team, same customers, same earnings growth, and a result that ranges from a modest gain to more than triple the money. The rest of the chapter teaches the arithmetic behind those three rows, then uses it to show what a product or engineering leader can and can’t claim credit for. The chapter [Understand Valuation: An Estimate, Not a Fact](#valuation-is-an-estimate) introduced the measures; this chapter follows the investment from purchase to sale.

In the calculations, “earnings growth” means an increase in the specified earnings measure. It doesn’t by itself establish better products or customer service. Postponing maintenance, for example, can raise current earnings while creating problems later.

{id: three-different-returns--the-base-buyout-measures-and-arithmetic}
## The Base Buyout: Measures and Arithmetic

Three definitions from the chapter [Understand Valuation: An Estimate, Not a Fact](#valuation-is-an-estimate) carry the calculation. **EBITDA** is earnings before interest, taxes, depreciation and amortization. Interest is the cost of borrowing, and taxes here means income taxes. Depreciation and amortization are accounting charges that spread the cost of a long-lived asset over the years it is used: depreciation for physical items such as equipment or vehicles, amortization for intangible ones such as acquired software or customer contracts. EBITDA leaves all four out so that the operating business can be compared before differences in financing, tax and asset history.

EBITDA is an earnings subtotal, not money in the bank. A company with €15 million of EBITDA still has to pay its interest and taxes, replace equipment and fund growth before any cash is left to repay debt. The €20 million repayment in this example is therefore a separate assumption about the cash left after that spending, not a consequence of the EBITDA figure.

An **EBITDA multiple** is the price a buyer pays per euro of those annual earnings: a business earning €3 million that sells for €30 million sold at 10× EBITDA. The multiple packs a buyer’s expectations about growth and risk into a single number; it states a price, it doesn’t promise ten years of cash. And what the *business* is worth and what the *shareholders* get are different amounts, because lenders must be repaid before the owners receive anything:

**Equity value = enterprise value − net debt.**

Enterprise value is the value of the operating business, and net debt is borrowings less the cash included in the calculation. Equity value is what is left for the owners. We leave out other rights to payment that a buyer would deduct, and the price adjustments negotiated in a sale contract, for this example.

Now the base case in full. The fictional company has annual EBITDA of **€10 million**. A fund agrees to buy it at **10× EBITDA**, giving an **enterprise value of €100 million**. The purchase uses **€60 million of acquisition debt and €40 million of fund equity**. The debt is borrowed by the companies set up to make the purchase, and the business’s own cash is expected to pay the interest and the repayments. Using borrowing this way is called **leverage**; this example is a leveraged buyout. A buyout doesn’t have to use this level of borrowing.

Five years pass. EBITDA reaches €15 million: earnings improved by half, and for now we take no view on whether the company itself got better. It also repays €20 million of debt from the cash left after its own spending, as assumed above. The fund sells at the same 10× multiple.

Assume no cash is available to offset debt at entry or exit. Ignore fees, taxes on the sale, changes in the fund’s ownership percentage and payments to owners before the sale; the chapter [Understand Cash Flow: Confirm the Cash Before You Commit](#obligations-before-budget) follows the cash step by step from operating earnings to what is left for lenders and owners.

| Item | Entry | Calculation | Exit | Calculation |
| --- | ---: | --- | ---: | --- |
| Annual EBITDA | 10 | The earnings measure defined above | 15 | After five years of earnings growth |
| EBITDA multiple | 10× | Price agreed per €1 of EBITDA | 10× | Assumed unchanged |
| Enterprise value | 100 | 10 × 10 | 150 | 15 × 10 |
| Net debt | 60 | Borrowed to fund the purchase | 40 | 60 − 20 repaid from cash |
| Equity value | 40 | 100 − 60 | 110 | 150 − 40 |

**Annual EBITDA and enterprise value each grew by 50%. The fund’s €40 million investment produced a €70 million gain, or 175%.** It put in €40 million and took out €110 million.

The €70 million equity gain separates into two parts, reflecting both earnings and financing:

- **€50 million** because the business earns more (€5m more EBITDA, at 10×)
- **€20 million** because the debt shrank, so less of the sale price goes to lenders

Two common measures describe this result. **MOIC**, the multiple on invested capital, is how many times the investor got its money back. It compares what the investor received, or still holds, with what it invested. In this example the holding has been sold in full, so MOIC is proceeds divided by total capital invested: €110m / €40m = **2.75×**.

**IRR**, the internal rate of return, expresses the result as an annual rate that accounts for when each payment happened. With one investment and one receipt five years later, it is (110 / 40) raised to the power of 1/5, minus 1: about **22.4%**. If money is invested or received at several dates, the calculation must include each dated payment. MOIC tells you how much; IRR tells you how fast, given those payment dates. Neither tells you whether the company is better.

One caution on the €20 million of debt repayment: it had to come from somewhere. **Paying it from operating cash** is a real achievement. An asset sale or additional investor funding can also reduce debt, but each has different consequences. Selling an asset gives up its future benefits; adding equity increases the money invested. Leaving that additional equity out of the return calculation overstates the result.

{id: three-different-returns--vary-the-multiple-the-timing-and-the-direction}
## Vary the Multiple, the Timing and the Direction

Return to the preview table, now with the annual return added. The operating assumptions are unchanged: EBITDA still reaches €15 million, debt still falls to €40 million. Varying only the exit multiple produces markedly different investment results.

| Exit multiple | Business worth | Fund receives | MOIC on its €40m | Annual return |
| --- | ---: | ---: | ---: | ---: |
| 7× | €105m | €65m | 1.6× | 10.2% |
| 10× | €150m | €110m | 2.75× | 22.4% |
| 12× | €180m | €140m | 3.5× | 28.5% |

The same engineering team, the same customers, the same year-on-year earnings growth. **Between the first row and the third, the fund’s proceeds and its MOIC more than double, from €65m and 1.6× to €140m and 3.5×.** The annual rate rises from about 10% to about 28%. Calling the 7× outcome a failed transformation would confuse the company’s work with its entry price and the price available at exit. Calling the 12× outcome proof of exceptional engineering makes the identical mistake in reverse.

This exercise varies the multiple without saying why it moved. In practice a multiple can reflect the company’s prospects and a particular buyer’s expectations as well as general market conditions, which is exactly why the transaction alone can’t separate those explanations.

Timing has the same effect. The time between purchase and sale is the **holding period**. Turning €40 million into €80 million is 2× either way, but do it in three years and that is about 26% a year; take seven years and it is about 10%. IRR exposes the speed, given the dates of the payments. It can’t tell you how much money was made, how much risk remains, or whether the business is any good.

Leverage magnifies the change in value relative to the fund’s smaller initial equity contribution, and it magnifies losses too. For a **separate downside scenario**, assume enterprise value falls to €80 million and no debt is repaid, leaving €60 million owed. Equity value is then €20 million, against the fund’s original €40 million investment. **The business lost a fifth of its value; the fund lost half of its money.**

{id: three-different-returns--why-the-bridge-cant-say-engineering-created-30-million}
## Why the Bridge Can’t Say “Engineering Created €30 Million”

Now suppose earnings and price move together: EBITDA grows from €10m to €15m *and* the buyer pays 12× instead of 10×. Enterprise value goes from €100m to €180m. Where did that €80 million come from? Investors answer with a **bridge**: a step-by-step breakdown that walks from one amount to another, here from €100m to €180m, assigning each step to a cause.

| Source | Amount | |
| --- | ---: | --- |
| The business earns more | €50m | €5m extra EBITDA, at the old 10× |
| Buyers pay more per euro | €20m | the extra 2×, on the original €10m |
| Both at once | €10m | the extra 2× on the extra €5m |
| **Total** | **€80m** | |

That third row is the awkward one. It exists only because both things changed together, and no rule says whether it belongs to the operating team or to the price. Assigning €60m to operations and €20m to the multiple is a **convention, not a measurement**, and a report that quietly folds the interaction into the operations column makes the same work look better.

This is where a claim such as “our platform work created €30 million of company value” runs into trouble. **Platform work** means improving the shared software foundations on which the company’s products are built, such as the systems that store data or handle logins; customers rarely see it directly. Ask how the claim would be justified. At the entry multiple, the bridge attributes €50 million to higher earnings. Allocating the €10 million interaction row differently changes that accounting attribution; none of those conventions identifies engineering’s causal share. The bridge then stops. It separates earnings from price; it doesn’t separate the platform work from the pricing changes, sales hiring, cost reductions or postponed maintenance that also moved EBITDA over five years. A transaction bridge answers “how much of the gain came from earnings rather than from the multiple.” It can’t answer “how much of the earnings came from engineering.” That causal question needs evidence gathered on the way, not read off the sale.

The shortcut behind all this, enterprise value = EBITDA × multiple, is a negotiating and comparison device, not a law of nature. What a buyer will actually pay depends on expected future cash, growth, risk, market conditions and its alternatives. Keep three kinds of change distinct when reading any result:

**Operational improvement** changes the company’s ability to serve customers and generate cash, the area most directly connected to product and engineering work. Making the product easier for new customers to set up might reduce installation and training work and allow additional sales. Fewer outages might reduce customer losses. Neither automatically creates the value assumed in a spreadsheet, and neither shows up in EBITDA on any fixed schedule.

**Financial structuring** changes who has a right to be paid from the business, when, and with how much risk. Borrowing can reduce the equity needed at entry. **Refinancing**, replacing an existing loan with a new one, can change interest costs or the **maturity date**, the deadline by which a loan must be repaid. A **debt-funded dividend**, borrowing in order to pay the owners now, distributes cash earlier while leaving a larger debt burden. Such changes can be rational; their benefits and risks must be measured separately from product improvement.

**Multiple changes** alter the price assigned to a unit of earnings. A stronger business might deserve a higher multiple. A rising market might also raise it. The transaction alone can’t separate those explanations. The broader literature describes borrowing, oversight of the company’s decisions and changes to its operations as interacting parts of buyout ownership. [S03: Kaplan and Strömberg](https://www.nber.org/system/files/working_papers/w14207/w14207.pdf)

![Earnings, the price multiple and debt reduction can each affect the equity proceeds from a sale.](private-techuity/posts/03-three-different-returns/assets/images/03-three-different-returns/sources-of-investor-return.jpeg)

**Figure 1:** *Explain operating, valuation and financing effects separately before attributing an investment gain to product and technology.*

{id: three-different-returns--two-extensions-dilution-and-a-corporate-owner}
## Two Extensions: Dilution and a Corporate Owner

{id: three-different-returns--a-minority-investors-return-can-change-with-further-funding}
### A Minority Investor’s Return Can Change With Further Funding

The buyout used borrowing. A **minority investment**, one that buys less than half of a company’s shares, shows a different mechanism without any borrowing. In a separate fictional example, Larkspur has 800 identical shares; a **share** is one unit of ownership, and here every share carries the same rights. A new investor pays €2m for 200 new shares, giving it 20% of the resulting 1,000 shares. This corresponds to an equity value of €8m before the new investment, the **pre-money valuation**, and €10m after it, the **post-money valuation**, as explained in the previous chapter.

Later, the company creates and sells 250 new shares to another investor, a **share issue**. The first investor buys none. It still owns 200 shares, but the total is now 1,250, so its holding falls to 16%. This reduction in ownership percentage is **dilution**. The company receives additional capital in that round; the first investor hasn’t received a payment.

Suppose the company is eventually sold for €20m of equity proceeds available to these shareholders. Assume identical payment rights, no further shares, no payments to shareholders before the sale, and no fees or taxes. The first investor receives 16% × €20m = €3.2m on its €2m investment: **1.6 times the money invested**. Had it bought additional shares, those payments would also belong in the return calculation.

An increase in company value therefore doesn’t translate mechanically into the same increase for an early shareholder. Further funding, ownership changes and payment priorities matter. **Preferences** are rights affecting which shares receive proceeds first or on different terms. With different rights, a simple percentage calculation may be wrong. For a company leader, another funding round has two consequences to discuss: the work its cash makes possible and the changes to ownership or expectations it brings.

![Issuing new shares can reduce an existing investor’s ownership percentage while adding cash to the company.](private-techuity/posts/03-three-different-returns/assets/images/03-three-different-returns/dilution-and-fresh-funding.jpeg)

**Figure 2:** *A lower ownership percentage does not, by itself, show whether the investor’s holding has gained or lost value.*

{id: three-different-returns--a-corporate-owner-may-expect-benefits-elsewhere}
### A Corporate Owner May Expect Benefits Elsewhere

In a fictional strategic acquisition, the buyer wants Larkspur’s scheduling product to help retain customers of its maintenance equipment. The buyer may value that effect even if Larkspur’s separate profit changes little. Alex, Larkspur’s technology leader, and Priya, its product leader, still need to establish the chain from action to benefit: which customers will use the combined offering, what must be connected between the two products, and who funds support and development.

A group-wide benefit isn’t automatically a local product budget. Ask the corporate owner to name the business unit accountable for the expected benefit and to fund the work and continuing obligations. Keep direct shareholder returns, expected group benefits and the company’s own operating results visible separately. The proposed mechanism must be tested; a strategic rationale doesn’t prove it works. A corporate parent’s internal investment review can also use different measures from a fund, and it need not involve any payment to outside investors or a planned sale.

{id: three-different-returns--what-product-and-technology-can-and-cannot-claim-credit-for}
## What Product and Technology Can and Cannot Claim Credit For

Start with the observable change, not the sale price. Which customer task improved? What costs changed? What investment was required? A **chief financial officer**, or **CFO**, leads the financial work and can help connect those observations to company earnings and cash. The investment team can then examine their possible valuation implications. The chapter [Test Revenue Assumptions: Do Customers Respond as Expected?](#roadmap-to-revenue) develops that chain in Part III.

One distinction from the investor’s side helps in reading the pressure you receive. Where the owner is a fund, its manager reports to the fund’s investors, often called limited partners. The report shows both the cash it has already returned to them and its estimate of the value of holdings it hasn’t yet sold. The estimate can still move, and pressure on a company often comes from the gap between the two. A corporate owner or an individual shareholder has no such report, though each has its own reasons to watch the same gap.

For optional depth, [Fund Economics: Fees, Distributions and Performance Reports](#fund-economics) explains the manager’s fee, the manager’s share of profits and the rules for paying money out to those investors, which together decide how much of a return reaches them. It also explains the ratios and borrowing arrangements behind the report.

The worked example gives a useful test for a proposed improvement: does its business case still hold if the sale price is lower or the owner holds the company longer? The answer separates a sustainable operating benefit from a result that depends heavily on the exit price.

If the return depends this much on price, borrowing and timing, the next question is how much borrowing, and which kind of investor, a company should take on for the work it actually has to do. That is the subject of the chapter [Understand Funding Choices: Match the Money to the Work](#raise-what-you-need).

{id: three-different-returns--questions-to-consider}
## Questions to Consider

1. *If your company’s earnings grew by half over five years, how would the investor’s return change under a lower exit multiple, a longer holding period or an additional funding round? Which of these can your team influence?*
2. *Which of your current initiatives would still justify itself if the sale price were lower or the owner held the company longer than planned?*
3. *The last time technology was credited with creating company value, how much of the gain was operating improvement, how much financing effect and how much a change in what buyers were paying? What evidence gathered along the way supports the engineering share?*
4. *If your owner is a corporate group, which business unit is accountable for the group-wide benefit attributed to your product, and who funds the work needed to deliver it?*

{id: three-different-returns--to-probe-further}
## To Probe Further

- **[Venture Deals: Be Smarter Than Your Lawyer and Venture Capitalist](https://www.venturedeals.com/)** — Brad Feld and Jason Mendelson, Wiley, 4th edition, 2019.  
  *Venture investors finance young companies with growth potential; this is two such investors’ explanation of liquidation preferences, dilution and the other payment rights this chapter mentions only in a sentence.*
- **[Do Buyouts (Still) Create Value?](https://www.nber.org/papers/w14187)** — Shourun Guo, Edith Hotchkiss and Weihong Song, National Bureau of Economic Research working paper, 2008 (Journal of Finance, 2011).  
  *The empirical version of this chapter’s value bridge, separating the returns on buyouts, purchases of controlling stakes, into operating gains, multiple changes and tax effects.*
- **[Private Equity Performance: A Survey](https://www.annualreviews.org/content/journals/10.1146/annurev-financial-111914-041858)** — Steven Kaplan and Berk Sensoy, Annual Review of Financial Economics, 2015.  
  *Optional depth: a summary of how fund returns are measured and how interim valuations compare with realized results, background for the received-cash versus unsold-estimate distinction that [Fund Economics: Fees, Distributions and Performance Reports](#fund-economics) develops.*
- **[Distortion or Cash Flow Management? Understanding Credit Facilities in Private Equity Funds](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3434112)** — Pierre Schillinger, Reiner Braun and Jeroen Cornel, Social Science Research Network (SSRN) working paper, 2019.  
  *Optional depth: simulations showing that a fund’s borrowing can lift its measured IRR substantially without changing company value, the same timing point this chapter makes with the three-year and seven-year comparison.*
