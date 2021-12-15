# Generate a Market Analysis Report

In this activity, you will combine your developer skills and your knowledge of statistics to generate a report that anaylzes a basket of stocks and their performance relative to the S&P 500.

## Instructions

Using the starter code file and the provided CSV files, complete the following steps.

1. Import the required libraries and dependencies.

2. Set paths to the CSV files.

3. For each CSV file, read the data into a Pandas DataFrame.

4. Create a function named `calculate_mean` that returns the average value for a given list or Series. **Hint:** Choose a function name that will not conflict with any modules that may have been imported.

   - <img src="https://render.githubusercontent.com/render/math?math=\mu = \frac{\sum{x_{i}}}{n}">

5. Create a function named `calculate_variance`. **Hint:** Variance is the squared average change around the mean.

   - <img src="https://render.githubusercontent.com/render/math?math={S}^2 = \frac{\sum{ (x_{i} - \mu })^{2}}{ n - 1}">
   
6. Create a function named `calculate_standard_deviation`. **Hint:** The standard deviation is the square root of the variance.

   - <img src="https://render.githubusercontent.com/render/math?math=\sigma = \sqrt{S^{2}}">
   
7. Create a function named `check_value` that compares the most recent price of the asset to its mean price.

   - If the most recent price is greater than the mean price, the asset is overvalued.

   - If the most recent price is less than the mean price, the asset is undervalued.

   - If neither case is true, the most recent price must be at the mean price.
   
8. Create a function named `compare_volatility` that compares the standard deviation of an asset's price change percentage with that of the market. **Hint:** If the asset's standard deviation is greater than that of the marke, the stock is more volatile; otherwise, it's less volatile.
   
9. Calculate the daily percent change for the S&P 500.

10. Calculate the standard deviation for the S&P 500.

11. Create a dictionary of stocks to run the report on. **Hint:** Be sure to map each stock's name to the DataFrame. Do not include the S&P 500. For example: `stocks_to_check = {"stock_name" : stock_df}`.
    
12. Generate the report. Loop through the dictionary of stocks, and for each stock, do the following:

      * Calculate the daily percent change.
      * Get the most recent price.
      * Calculate the mean and standard deviation using the functions you created.
      * Print the stock's name.
      * Print the statistics that you calculated.
      * Use `check_value` to determine if the stock is over- or undervalued.
      * Use `compare_volatility` determine if the stock is more or less volatile than the S&P 500. 
      * Plot a box plot of the daily percent change. 
      
      **Hint**: Use the `items()` method for dictionaries. You can read more in the [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques).
      
---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
