## Visualizing Time-Series with hvPlot

In this activity you we gain some additional practice working with the hvPlot grouped plots.

### Instructions

Using the [Starter code](Unsolved/visualizing_time_patterns.ipynb) provided, complete the following:

1. Read the S&P 500 volume into a DataFrame. (Make sure to declare the datetime index).

2. Slice the dataframe so that it just includes the volume data.

3. Using hvPlot, plot the volume data according to the day of the week to answer the following question: In what day does trading in the S&P500 tend to be the most active?

4. Next, use hvPlot to visualize hourly trends for each day of the week in the form of a heatmap. Based on this, does any day-of-week pattern concentrate in just a few hours of a particular day?

5. Lastly, create a plot with hvPlot that shows the data grouped by the calendar week in the year (week of year). Does share trading intensity tend to increase at any particular time of the calendar year?