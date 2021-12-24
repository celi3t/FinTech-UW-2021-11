# Financial Forecasting

In this activity, you will review one year's worth of TSLA stock prices and plot a potential stock trajectory for TSLA stock over the next three years. You'll also need to show how a $10,000 investment would perform, given the simulated results. Therefore, you'll create a Monte Carlo simulation that simulates the next `252 * 3` trading days by using three years' worth of TSLA stock data. Plot the simulated results of TSLA daily returns over the next three years as well as the corresponding simulated outcomes.

## Instructions

1. Import the required libraries and dependencies. 

2. Use the `get_barset()` function to retrieve three years' worth of daily prices for TSLA stock and read the data into a Pandas DataFrame. 

3. Build a Monte Carlo simulation that runs 1,000 times through `252 * 3` trading days, and then save the results. 

4. Plot the simulated daily returns of TSLA stock over the next three years.

5. Plot the simulated profits and losses for a $10,000 investment in TSLA, given the simulated cumulative returns.

6. Calculate the range of the possible outcomes of your $10,000 investment in TSLA stock with a 95% confidence interval. 

  **Hint:** Remember, a normal probability distribution illustrates the probability of potential outcomes as outcomes deviate closer to or away from the expected average.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
