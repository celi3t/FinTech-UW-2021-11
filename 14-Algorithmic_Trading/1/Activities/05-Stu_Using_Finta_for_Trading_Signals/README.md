# Using Finta for Trading Signals

In this activity, you will be utilizing the [finta Python library](https://pypi.org/project/finta/) to generate the trading signals that power your trading algorithms.

## Instructions

In this activity, you will be utilizing the [finta Python library](https://pypi.org/project/finta/) to generate the trading signals that power your trading algorithms.

1. Open a new terminal window and install the [finta Python library](https://pypi.org/project/finta/).

  * Activate your conda `dev` virtual environment.
  * Type the following at the command prompt:

    ```shell
    pip install finta
    ```

2. Using the Jupyter notebook included in the unsolved folder, import the TA module from the finta library.

3. Read in the `ixn_ohlcv.csv`file from the Resources folder into a Pandas DataFrame. Both review the DataFrame and generate a plot of the "close" price using hvPlot.

### Part 1: Recreate the DMAC trading algorithm using technical indicators from the finta library.

Using the [finta library](https://pypi.org/project/finta/), reconstruct the simple moving average (`TA.SMA`) dual crossover trading algorithm.

1. Set a `short_window` variable at 15, and a `long_window` variable at 50.

2.  Using the [finta library](https://pypi.org/project/finta/) syntax, create two DataFrame columns. One column holds the "Short" simple moving average calculation, the other holds the "Long" simple moving average value calculation. Review the DataFrame to confirm the new columns were added.

3. Create a "Signal" column for the DataFrame and set the initial value to 0.

4. Create the trading algorithm using the `np.where` function. The value of the "Signal" column should updated to 1 where the short value SMA is greater than the long value SMA and 0 otherwise.

5. Create an "Entry/Exit" column in the DataFrame using the `diff` function. The column should reflect a 1 where the "Signal" column changes from 0 to 1, and a -1 where the "Signal" column changes from 1 to 0. Again, review the updated DataFrame.

6. Review the visualization that plots the entry points, exit point, short and long-window moving averages, all against the closing price.

7. Update the trading algorithm by incorporating at least one new moving average technical indicator (ie. SSM,  SSMA, EMA, DEMA, etc.) into your algorithm and evaluate the results.

### Part 2: Create a new trading algorithm using the Bollinger Bands technical indicator from the finta library.

Using the [finta library](https://pypi.org/project/finta/), construct a trading algorithm where an entry position is initiated when the closing price is less than the lower Bollinger band (an indicator that the stock is oversold and the price is likely to trend higher), and an exit position is initiated when the closing price is greater than the upper Bollinger band (an indicator that the stock is overbought and the price is likely to trend lower).

1. Create a copy of the original `ixn_df` DataFrame and save it as a DataFrame called `bb_signals_df`. Review the DataFrame.

2. Create a DataFrame called `bbands_df` by using the finta library's syntax to create the Bollinger Bands technical indicator. Review the DataFrame.

3. Using the [Pandas `concat` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html), concatenate the `bb_signals_df` and the `bbands_df` DataFrames. Save them as a new version of the `bb_signals_df`. Review the concatenated DataFrame.

4. Review the visualization of the `bb_signals_df` DataFrame including the Bollinger bands.

5. Create a trading algorithm that incorporates the Bollinger bands technical indicator.

    * Create a "Signal" column for the `bb_signals_df` DataFrame. Set the initial value to 0.
    * Create a trading algorithm using the Pandas `iterrows` function. For each row, if the "close" is less than "BB_LOWER", indicating an oversold position, update the "Signal" column to a 1 (trade entry). If the "close" value is greater than "BB_UPPER", indicating an overbought position, update the "Signal" column to -1 (trade exit).
    * Review the DataFrame.

6. Create a visualization that overlays the entry and exit positions as well as the close value and each of the 3 Bollinger bands. What do you notice about the entry and exit positions? Would this make a viable trading algorithm given its current status?

7. Update the trading algorithm so that only the first entry and first exit positions for each trade cycle are identified as trading signals. Review the plot to see if the variable was incorporated correctly.

    * **Hint:** Create a variable called `trading signal`, which is initially assigned a value of 0. This trading signal should be incorporated as a conditional in the trading algorithm's if-statement. The value should be adjusted to either 1 or 0 when the "Signal" column is updated. Review the plot to see if the variable was incorporated correctly.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.