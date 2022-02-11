# Advanced Prophet Models - Detecting Changes

In the previous activities, we've read in the data, built a forecasting model on Bitcoin, and made predictions out into the future.

In this section, we'll try out some advanced strategies in Prophet for making better forecasts. Specifically, this will include (1) detecting abrupt changes in the time-series trend, and (2) adjusting for holidays.

## Instructions

The starter file includes all of the code from Parts 1 and 2. Using the starter file, run this solution code, and then complete the following steps:

### Detecting Abrupt Changes in Trend

1. Using the `forecast_trends` DataFrame, reset the index of this forecast dataframe in order to use changepoints.

2. Import the `add_changepoints_to_plot` function in order to plot the changepoints.

3. Plot the `forecast_trends` dataframe to a figure, and then add the changepoints using `add_changepoints_to_plot`.

4. Use `display` on `model.changepoints` to view the exact dates and times of the major changepoints.

## Hint

Breathe easy! Take this activity one step at a time. Remember that this is a culminating activity of the unit, and covers some advanced strategies for building forecasting models.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
