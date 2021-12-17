# Calculating Stock Returns via Pandas DataFrames

In this activity, you will calculate daily stock returns and cumulative stock returns using the average daily price. The average daily price is defined as follows: 

average_daily_price = (open + close + high + low) / 4

## Instructions

1. Import the Pandas and pathlib libraries, and set the `%matplotlib inline` property.

2. Create a variable `csvpath` that represents the path to the [MSFT.csv](Resources/MSFT.csv).

3. Read the CSV into a Pandas DataFrame. Use the `index_col` parameter to set the index as the "date" column. Set `parse_dates` and `infer_datetime_format` to `True`.

4. Drop the "volume" column.

5. Calculate the daily average price. Use the `mean` function with `axis = 1` and save the average price into a new column in the DataFrame. **Hint:** DataFrames are a concatenation of Series.

6. Plot the average daily values of `MSFT`.

7. Use the `pct_change` function to calculate the daily returns of `MSFT`.

8. Plot the daily return values for `MSFT`.

9. Use the `cumprod` function to calculate the cumulative returns of `MSFT`

10. Plot cumulative return values for `MSFT`.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
