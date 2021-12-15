# Compare the Risks of a Portfolio of Stocks

In this activity, you will compare a basket of stocks and determine if they are risky investments compared to the S&P 500.

## Instructions

Using the starter code file and the provided CSV files, complete the following steps.

1. Import the required libraries and dependencies. 

2. Set paths to the CSV files by creating a `path` object for each CSV file path. Each CSV file contains a stock's closing price and the date of the closing price.
    
3. Read the data from each CSV file into a Pandas DataFrame. Be sure to do the following: 

    - Set the index column to be the date.

    - Infer the Datetime format.

    - Parse all dates when the CSV is loaded.
    
4. Concatenate the Dataframes into one DataFrame. Use an inner join and set the axis as the columns. 
    
5. Calculate the daily percent changes. Be sure to drop all N/A values.

6. Calculate the Sharpe ratios. **Hint:** The Sharpe ratio is the ratio between the average annual return and the annualized standard deviation. Remember, there are 252 trading days in a year. To find the Sharpe ratio, first calculate the average annual return, and then calculate the annualized standard deviation: 

    - <img src="https://render.githubusercontent.com/render/math?math=\frac{R_{p}}{\sigma_{p}}">
      
7. Plot the Sharpe ratios in a bar plot.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
