# Correlation

In this activity, you will analyze the following five semiconductor stocks: `INTC`, `AMD`, `MU`, `NVDA`, and `TSM`. Then you'll choose the stock with the least correlation to `JNJ` and `HD` in order to diversify a portfolio. 

To learn more about diversification and how correlation in a portfolio helps to minimize risk, review this [article on diversification](https://www.investopedia.com/terms/d/diversification.asp).

## Instructions

1. Import the Pandas, Seaborn, and pathlib libraries, and set the `%matplotlib inline` property.

2. Create a `path` object for each CSV file.

3. Read each CSV file into a DataFrame and set the "date" column as the index.

4. Use the `concat` function to combine the seven DataFrames into a single DataFrame. 

5. Use the `pct_change` function to calculate the daily returns. Drop `n/a` values. 

6. Use the `corr` function on the combined DataFrame to calculate and output a correlation table of each stock-to-stock pair.

7. Use the `heatmap` function from the Seaborn library to create a heatmap of correlation values. **Hint:** You can read more about the `heatmap` function in the [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap).

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
