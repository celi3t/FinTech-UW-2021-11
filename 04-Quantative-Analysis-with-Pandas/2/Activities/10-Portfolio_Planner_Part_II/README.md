# Portfolio Planner, Part 2

In this activity, you will revisit the 10 stocks that you researched in Part 1 of this activity:

* Bank of New York Mellon (BK)
* Diamondback Energy (FANG)
* Johnson & Johnson (JNJ)
* Southwest Airlines Co (LUV)
* Micron Technologies (MU)
* Nike (NKE)
* Starbucks (SBUX)
* AT&T (T)
* Western Digital (WDC)
* Westrock (WRK)

Now, you will create an optimized portfolio with the following characteristics:

* Equal-weighted allocations

* Least correlated stocks

* Positive return-to-risk ratio stocks (Sharpe ratios)

Then, you will visualize the returns of a hypothetical `$10,000` investment in this portfolio over time, as well as how this portfolio compares to $10,000 investments in less optimized portfolios.

**Hint:** Take this activity one step at a time. Remember that this is the culminating activity of the unit. Think about the bigger picture—what makes a particular stock portfolio a good investment?

## Instructions

1. Run the provided solved code cells from Part 1 down to the beginning of Part 2. The variables created in Part 1 are prerequisites for your code in Part 2. 

2. Reset the DataFrame for daily returns of the 10 stocks. Use the `pct_change` function to calculate and reassign a new DataFrame of daily returns.

3. Use the `corr` function and the `heatmap` function from the Seaborn library to calculate and visualize the stock return correlations for each stock pair.

4. Drop the two most consistently, highly correlated stocks and keep the remaining less correlated stocks from the DataFrame (two stocks should be dropped). (*Hint: you can do this by visually identifying high correlations, or by summing then comparing total correlation values per stock.*)

5. Use the `mean` and `std` functions to calculate the annualized Sharpe ratio and assess the reward-to-risk ratio of the 8 remaining, less-correlated stocks.

6. Drop the stocks with the three lowest Sharpe ratios from the DataFrame. (Three stocks should be dropped).

7. Assess the investment potential of a noncorrelated (diversified) and return-to-risk (Sharpe ratio) optimized portfolio:

    * Set an equal weight for each stock in the optimized portfolio (five stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the optimized portfolio's daily returns.

    * Calculate the optimized portfolio's cumulative returns, and then multiply the initial investment of $10,000 against the portfolio's series of cumulative returns. Plot the trend.

8. Assess the investment potential of a minimially correlated (diversified) portfolio:

    * Set an equal weight for each stock in a minimally correlated stock portfolio (eight stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the noncorrelated stock portfolio's daily returns.

    * Calculate the minimally correlated stock portfolio's cumulative returns, and then multiply the initial investment of $10,000 against the portfolio's series of cumulative returns. Plot the trend.

9. Assess the investment potential of the original unoptimized portfolio:

    * Set an equal weight for each stock in an unoptimized portfolio (all 10 stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the unoptimized portfolio's daily returns.

    * Calculate the unoptimized stock portfolio's cumulative returns, and then multiply the initial investment of $10,000 against the portfolio's series of cumulative returns. Plot the trend.

10. Overlay the investment trend of every portfolio on a single chart, including the portfolio constructed in Part 1.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
