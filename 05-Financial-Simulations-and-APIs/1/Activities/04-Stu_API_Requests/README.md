# Canadian Housing Data

In this activity, you will create a report to plot the median home prices and units available for Canadian provinces. Then, you will use your findings to recommend a province that you think has the best investment potential. 

### Instructions

1. Import the required libraries and dependencies. 

2. Store your Quandl API key in a variable named `QUANDL_API_KEY` in an `.env` file.

3. Set start and end dates for the housing data (November 2009 to November 2020).  

4. Using the provided list of provinces, loop over each province with the following URL builder: 

    ``` text
    https://www.quandl.com/api/v3/datasets/CMHC/HPPU50_{province}?start_date={start_date}&end_date={end_date}&api_key={quandl_api_key}
    ```

5. Create a scatter plot for each province using the `Date` and `Median` values for `x` and `y`. Use the `c` option in [`scatter`](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.scatter.html) to shade each point according to the number of units. Use `inferno` for the `cmap` parameter.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
