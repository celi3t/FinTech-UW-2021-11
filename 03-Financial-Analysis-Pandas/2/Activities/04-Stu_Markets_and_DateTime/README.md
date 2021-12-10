# Markets and DateTime

In this activity, you will analyze a CSV file that contains pricing data from a single week in February 2020 for various stocks and indexes. You will use the `loc` function and the Pandas DateTime functionality in order to determine the percent change in the price for one day of the week and for the week as a whole.

## Instructions

1. Using the Pandas `read_csv` function and the Path module, read `market_data.csv` into a Pandas DataFrame. Review the first five rows of the Dataframe. Then use the `info` function to determine the columns and their respective data types.

2. Re-import `market_data.csv` using the `read_csv` function. This time, set the `index_col` to "Timestamp", and set the `parse_dates` and `infer_datetime_format` parameters. Display the first five rows of the Dataframe. Then use the `info` function to determine the columns and their respective data types.

3. Using the `plot` function, plot the pricing information for the ticker of your choosing from the DataFrame. This will display the data for the full week's worth of information for the chosen stock.

    **Hint:** You will notice that the data is very choppy. This is because the data contains information for times when the markets were not open and the stock or index was not trading.

4. Using the same stock from Step 3, choose the day with the biggest pricing change and plot just that single day. You will need to use the `loc` function and reference your chosen date in the format displayed in the TimeStamp index. You will not reference the time in this step.

5. For your chosen stock, plot the active trading period. To do this, use the `loc` function, reference the date used in Step 4, and add the time component. The trading day for these stocks will be from approximately 09:30 to 16:00.

Next, complete the following steps to calculate the percent change in the stock/index for your chosen day of the week.

6. Create a Pandas DataFrame that includes data for your chosen stocks trading day. To create the DataFrame, use the code from the previous step and remove the `plot` function. This should display the exact times that the stock/index started and finished trading. Confirm the creation of your DataFrame by displaying the first and last five rows.

7. Create a variable called `day_open` that holds the opening price for your stock or index. Set this variable equal to the opening price using the `loc` function, and reference the date and exact time that trading began. View the value of this variable.

8. Create a variable called `day_close` that holds the closing price for your stock or index. Set this variable equal to the closing price using the `loc` function, and reference the date and exact time that trading ended. View the value of this variable.

9.  Calculate and display the percent change (`day_percent_change`) variable using the following formula: (day_close- day_open) / day_open

Next, complete the following steps to calculate the percent change in the stock/index for the week.

10. Create a Pandas DataFrame that includes the week's worth of trading data for your chosen stock. Use the `loc` function and specify the time from 09:30:00 on 2020-02-24 through 16:00:00 on 2020-02-28. Confirm the creation of your DataFrame by displaying the first and last five rows.

11. Create a variable called `week_open` that holds the week's opening price for your stock or index. Set this variable equal to the opening price using the `loc` function, and reference the date and exact time that trading began on the first day of the week. Display this variable.

12. Create a variable called `week_close` that holds the week's closing price for your stock or index. Set this variable equal to the closing price using the `loc` function, and reference the date and exact time that trading closed on the last day of the week. Display this variable.

13.  Calculate and display the percent change (`week_percent_change`) variable using the following formula: (week_close - week_open) / week_open

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
