# Mapping Adventures

It's time to take a break from your day job and to plan an adventure!

Your friends have decided to plan a trip to New York City, and you're all looking forward to the time away from the office. In order to plan for the event, you started doing some research regarding points of interest. You've found one dataset that lists a bunch of cool places to see.

Use **hvPlot** and **GeoViews** to create a series of geographical plots that will visualize each area of interest within the city.

### Instructions

1. Read in the `nyc_places_interest.csv` file from the `Resources` folder into a Pandas DataFrame. Drop any rows that contain missing data or NaN values.

2. Plot all places of interest by using the hvPlot `points` function with GeoViews enabled. Set the parameters as follows:

    * Set the `color` parameter to Name
    * Set `alpha` to 0.8
    * Set `tiles` to 'OSM'
    * Set `frame_width` to 700

3. Plot places of interest by `PlaceType` by using the `points` function.  Set the `color` parameter to 'PlaceType' and keep all other parameters the same as the previous plot.

4. Plot places of interest by `Borough`. Set the `color` parameter to 'Borough' and keep all other parameters the same as the previous plot.

5. Plot parks that are of interest.

6. Plot gardens that are of interest.

7. Plot squares that are of interest.

8. **Bonus:** Select just two locations from the `places_of_interest` DataFrame and plot them on a scatter plot map. Use the Pandas [`isin` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) to reference a list containing the names of the two locations, as specified in the "Name" column, that you would like to visit.

> **Hint** Creating too many map plots in one notebook might create a memory issue. If it does, consider creating a separate notebook for the Bonus section. This will require you to read the CSV data in both notebooks.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
