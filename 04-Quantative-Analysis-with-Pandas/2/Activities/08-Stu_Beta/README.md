# Beta Comparisons

In this activity, you will calculate and plot the 30-day rolling betas for social media stocks, and determine the social media stock with the lowest beta value.

## Instructions

1. Import the Pandas and pathlib libraries, and set the `%matplotlib inline` property.

2. Create a `path` object for each CSV file. 

3. Read each CSV file into a Pandas DataFrame. Use the `index_col` parameter to set the index as the "date" column. Set `parse_dates` and `infer_datetime_format` to `True`.

4. Combine the DataFrames using the columns for the `axis`. Then sort the DataFrame by `date` and rename the columns to each stock symbol. 

5. Use the `pct_change` function to calculate daily returns for each stock.

6. Calculate the overall covariance of each stock's daily returns to that of the S&P 500. Calculate the overall variance of S&P 500 daily returns.

7. Calculate the variance of S&P 500 returns.

8. Calculate the beta of each social media stock. The beta is the ratio between covariance and variance: 

    - <img src="https://render.githubusercontent.com/render/math?math=\beta = \frac{cov(R_{e},R_{m})}{var(R_{m})}">

9. Calculate the 30-day rolling beta of each stock's returns vs. S&P 500 returns by doing the following: 

    - Use the `rolling` function to calculate covariance for each stock.
    
    - Calculate the rolling variance of the S&P 500.
    
    - Calculate the rolling beta for each stock. 

10. Plot the rolling 30-day betas of the social media stocks. **Hint:** Set the `ax` parameter when plotting multiple datasets on a single chart.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
