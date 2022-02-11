# Advanced Prophet Models - Modeling Holiday Events

In Part 1 of this activity, we've read in the data, built a forecasting model on Bitcoin, and made predictions out into the future.

In Part 2, we'll try out some advanced strategies in Prophet for making better forecasts. Specifically, this will include (1) detecting abrupt changes in the time-series trend, and (2) adjusting for holidays.

## Instructions

The starter file includes all of the solutions to Part 1. Using the starter file, run this solution code, and then complete the following steps:

### Modeling Holiday Effects

1. Create a new `Prophet` model.

2. Add the built-in US holidays to the model using `add_country_holidays`.

3. `fit` the model.

4. Check what holidays are included using `train_holiday_names`.

5. Create a dataframe to hold predictions as far as 1000 hours (approx 40 days), using `make_future_dataframe`.

6. `predict` the trend data using the `future_trends` DataFrame.

7. Plot the trend components using `plot_components`.

## Hint

Breathe easy! Take this activity one step at a time. Remember that this is a culminating activity of the unit, and covers some advanced strategies for building forecasting models.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
