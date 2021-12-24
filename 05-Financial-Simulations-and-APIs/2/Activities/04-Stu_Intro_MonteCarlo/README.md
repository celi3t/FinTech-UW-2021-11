# Forecasting with MCForecast

In this activity, you will use the provided `MCForecastTools.py` module to forecast a portfolio's returns for one year's worth of stock data for both Home Depot and Disney. 

Specifically, you will retrieve the data using the Quandl API and then concatenate the DataFrames by using `MCSimulation`. Then, you will use `calc_cumulative_return`to get the cumulative returns for the year. Finally, you'll plot the simulations, examine the distribution, and review the summary statistics for the simulation. 

>**Hint:** The most authoritative documentation is the source code itself. Make sure to review the `MCForecastTools.py` file to get an idea of how the module works.

**Instructions**

1. Import the required libraries and dependencies. 

2. Load the environment variables. 

3. Retrieve the data from Quandl.

4. Using the response JSON objects, get a list of the column names and create DataFrames for each ticker. Convert each DataFrame's `Date` field to a `datetime` object and set `Date` as the index.

5. Using `to_datetime`, convert a string into a `datetime` object. Use the `infer_datetime_format` parameter.

6. Filter each DataFrame to only keep the `"Open", "High", "Low", "Close", "Volume"` columns. In order to work with `MCForecastTools`, the columns will then need to be renamed using all lowercase letters. 

7. Create a dictionary to hold the Home Depot and Disney DataFrames similar to the following:

      ```
      { "ticker_name": ticker_df , .... }
      ```
      
    **Hint:** `MCForecastTools` requires that the DataFrame be multi-indexed.
    
8. Use the dictionary and the Pandas `concat` function to concatenate the DataFrames and return a multi-indexed DataFrame. Be sure to do the following: 

    - Use the dictionary's `.value()` function for the data parameter into `concat`.
    
    - Set `axis = 1`.
    
    - Use the dictionary's `.keys()` function for the `keys` parameter in `concat`.

9. Create an instance of `MCSimulation` with the following parameter values:

    - `weights == [0.25,0.75]`
      
    - `num_simulations == 500`
      
    - `num_trading_days == 252`
      
10. Call the following functions: 

    - `calc_cumulative_return` to run the number of simulations
      
    - `plot_simulation` to plot the simulated returns
    
    - `plot_distribution` to plot a histogram of the underlying distribution
    
    - `summarize_cumulative_return` to display summary statistics for the simulated distribution
    
---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
