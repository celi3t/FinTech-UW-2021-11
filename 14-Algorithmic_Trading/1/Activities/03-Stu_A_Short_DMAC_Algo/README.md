# A Short DMAC Algorithm Strategy

Using the CSV file provided, create a dual moving average crossover strategy for a trading algorithm that utilizes a short-position strategy.

A short-position strategy looks to capitalize on a downward trend in the stock price and initiates the trading position with a sell.

The strategy will be initially evaluated with a short window of 50 days and a long window of 100 days.

Complete the following steps to initiate your dual moving average crossover short-position algorithm.

## Instructions

1. Read the `blk_ohlcv.csv` file from the Resources folder into a Pandas DataFrame. Establish the "Date" column as the DateTimeIndex, then visualize the data using hvPlot.

2. Create a DataFrame called `signals_df`, which consists of only the Data index and the "Close" column from the original DataFrame.

3. Set the trading algorithm's `short_window` at 50 periods and the long_window at 100 periods.

4. Generate the short and long window moving averages. This is done by calling the `rolling` function and passing in a parameter called `windows` that are set to the short and long-windows, respectively. Chain the `mean` function to the rolling function in order to generate the average value of the rolling metrics.  Review the resulting DataFrame.

5. Add a "Signals" column to the signals_df DataFrame. Set the initial value of the signals column to 0.

6. Utilize the NumPy `where` function to create the code that evaluates the short-window moving average versus the long-window moving average. For this short-position strategy, a trade should be initiated (a value of 1) when the short-window SMA is less than (below) the long-window SMA. This is an indication that the overall trend in the stock price is heading lower. The value should be 0 otherwise.

7. Create the trade entry and exit trade signals. Call the `diff` function on the signals_df DataFrame "Signal" column. A value of 1 or -1 will be generated when the "Signal" column changes, indicating the occurrence of a crossover between the short and long-window SMAs.

8. Run the code that produces the visualization of the entry and exit points, as well as the short and long-window moving averages and the stock's closing price. Review the entry and exit points in relation to the short-position trading strategy. Do you think that this algorithm would have made money?

9. Alter the period assigned to the `short_window` from 50 to 30 days and rerun the code. Evaluating the resulting visualization, do you think this new algorithm would have performed better or worse than the version with a short_window of 50 periods.

10. Alter the period assigned to the `short_window` to 15 days and rerun the code. Evaluating the resulting visualization, do you think this new algorithm would have performed better or worse than the versions with short_windows of 50 and 30 periods.

11. Keeping the short_window at 15, adust the long_window from 100 to 200 periods, and rerun the code. What do you notice?

12. Finally, keeping the long window at 200, adjust the short_window back to the original value of 50. Would you utilize this version of the trading algorithm if your money was at risk?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.