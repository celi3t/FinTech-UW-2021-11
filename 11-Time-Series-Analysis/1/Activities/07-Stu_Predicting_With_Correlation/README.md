# Predicting Data Using Time-Series Correlation

In this activity, you will get practice with the creating an hvPlot dual axis plot to juxtapose time-series data. You'll then use this and other data to analyze lead-lag relationships using time-series correlation.

### Instructions

Using the [starter code](Unsolved/predicting_with_correlation.ipynb) provided, complete the following steps.

1. Read in the S&P 500 stock volume and price data.

2. Plot S&P 500's performance over time using an hvPlot line plot.

3. Based on this plot, slice to just a few months to where the market seems to have suffered a big decline. (This is meant to be a little subjective; pick the time you think is most volatile/downward).

*For steps (4)-(10) that follow, just analyze this downward sub-period DataFrame.*

4. Using this downward sub-period, use hvPlot's ability to create two graphs, stacked one on top of each other. Specifically, plot the hourly `close` price and hourly `volume` of shares traded. Looking at this visual, does it apper there is any relationship between `volume` and `close`?

5. Create a column called `Lagged Volume`, which is the `volume` column, but shifted back in time by one hour.

6. Create another column called `Stock Volatility`, which is the rolling standard deviation of SPY's stock price returns. (Consider using a 4-hour moving average, or experiment with your own horizon to see if it impacts predictability).

7. Last (but not least!), construct a column called `Hourly Stock Return`, which is the percentage return on the S&P at each hour.

8. Using these three columns, construct a `correlation` table, and answer the following questions:

    * Does this hours trading volume predict the next hour's market volatility?

    * Does this hours trading volume predict the next hour's market return?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
