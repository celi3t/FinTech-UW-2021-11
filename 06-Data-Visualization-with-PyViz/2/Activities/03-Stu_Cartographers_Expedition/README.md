# A Cartographer's Expedition

You and your friends have decided to tackle NYC old school! No cell phones or GPS devices allowed. Although everyone is a bit nervous,  you realize that using an actual map might be pretty cool.

Instead of spending money on a map of NYC, become a true, modern cartographer and create your own map plots that can be used by you and your friends to get the lay of the city.

Using the CSV file provided, your goal is to generate a map that plots between five and six locations in the city.  Use **hvPlot** and **GeoViews** to plot the route (point A to point B to point C) for the expedition.

## Instructions

1. Read in the `nyc_excursion_plans.csv` file into a Pandas DataFrame. Drop any rows that contain missing data or NaN values.

2. Slice data for your arriving airport and the first location the group will visit. Plot the arriving airport and the first location.

> **Hint:** You can use the Pandas [`str.contains`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html) or [`isin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) functions in order to access the names of the locations that you intend to visit.

3. Create a plot that includes your second and third locations. Be sure to include your first stop so that you know how to get to the second stop.

4. Create a plot that includes your fourth and fifth locations. Be sure to include your third stop so that you know how to get to the fourth stop.

5. Plot all locations on one map. In what order should you visit the locations in order to get back to the airport most efficiently?

6. **Bonus:** Feel free to add any places in New York City that you would like to visit to the data file. To do this, you can look them up in a mapping service (such as Google Maps) to find the latitude and longitude, and then add them to the data file. Be careful not to corrupt the data file. If you do, re-download the data and start again.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
