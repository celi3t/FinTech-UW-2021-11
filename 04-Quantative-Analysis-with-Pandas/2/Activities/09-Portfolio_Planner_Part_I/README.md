# Portfolio Planner, Part 1

You have been tasked with a project involving the following 10 stocks:

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

Using the Pandas library, you need to sort these stocks by risk/volatility; filter out the top five stocks with the highest volatility; and assign the remaining stocks portfolio weights of 0.15, 0.05, 0.10, 0.2, and 0.50 (from least risk to most risk). You also need to show the returns over time for a hypothetical $10,000 investment in a portfolio consisting of these stocks. 

## Instructions

1. Import the required libraries and dependencies.

2. Read the following CSV files into Pandas DataFrames: 

    * `bk_data.csv`
    * `fang_data.csv`
    * `jnj_data.csv`
    * `luv_data.csv`
    * `mu_data.csv`
    * `nke_data.csv`
    * `sbux_data.csv`
    * `t_data.csv`
    * `wdc_data.csv`
    * `wrk_data.csv`

3. Combine the DataFrames so that the closing prices from each DataFrame are stacked column by column.

4. Use the `sort_index` function to sort the combined DataFrame by `DatetimeIndex` in ascending order (past to present).

5. Rename the columns to reflect the corresponding stock.

6. Use the `pct_change` function to calculate daily returns for each stock.

7. Use the `std` function and multiply by `sqrt(252)` to calculate annualized volatility. Use the `sort_values` function to sort by volatility values.

8. Drop the top five stocks with the highest volatility from the DataFrame of daily returns.

9. Set portfolio weights of 0.15, 0.05, 0.10, 0.2, and 0.50 to the remaining stocks (from least risk to most risk).

10. Using the `dot` function, multiply the weights by each column of daily returns in order to calculate the daily returns of the constructed portfolio.

11. Use the `cumprod` function to calculate the cumulative returns of the constructed portfolio.

12. Plot the returns of a hypothetical $10,000 investment in the constructed portfolio. **Hint:** To plot the returns of a $10,000 investment, multiply the initial investment by the portfolio's cumulative returns over time.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
