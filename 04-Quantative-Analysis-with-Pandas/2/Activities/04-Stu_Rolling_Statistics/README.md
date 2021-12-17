# Visualizing Rolling Statistics with Pandas DataFrames

In this activity, you will calculate and visualize rolling statistics for a specified time window. You will calculate a volume weighted average price for each window. The volume weighted average price is defined as follows:

average_daily_price = (open + close + high + low) / 4

The `average_volume` will be calculated for each window, and the `average_price` will be calculated for each day.

## Instructions

1. Import the Pandas and pathlib libraries, and set the `%matplotlib inline` property.

2. Create a variable `aapl_csvpath` that represents the path to the [AAPL.csv](Resources/AAPL.csv).

3. Read the CSV into a DataFrame. Set the "date" column as the index.

4. Calculate the average daily price.

5. Define a function to calculate the volume weighted average price. Note the following:

    - The calculation is as follows: average_price * volume / average_volume_for_window

    - The average price is for each day.

    - The average volume is for each window.

6. Calculate the average volume for each window using the `rolling` function with a window size of `10`.

7. Apply the volume weighted average price function by doing the following:

    - Use the function defined previously to calculate the weighted price.

    - Use a `lambda` function to pass in parameters from the other row values in the DataFrame. **Hint:** You can read more about the `lambda` function in the [Python documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).

    - Use `axis = 1` so that the `apply` function applies the function to each row. **Hint:** You can read more about the `apply` method in the [Python documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html).

8. Plot the volume weighted average price and the average price. **Hint:** Plot the volume weighted average price first, and then add the average price as the second figure.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
