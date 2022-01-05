# Plotting Relocation

Your parents are considering relocating to another state because of the rising hospital costs in New Jersey for diabetes care. One of their main considerations is moving to a location where there are low cost offerings for diabetes services.

Using hvPlot, analyze and plot the provided hospital claims data. Use the widgets to explore the data and get specific detail about each state and provider. Make sure to perform all analysis using the visualization and supporting widgets.

## Instructions

1. Open the [starter file](Unsolved/hvplot_widgets.ipynb), and run the starter code. Examine the information provided in the DataFrames.

2. Group the filtered hospital data by **Average Total Payments** and **Provider State**. Then, sum by **Average Total Payments**.

    > Hint: Use Pandas `groupby` function.

3. Plot the aggregated data using `hvplot.bar` function. Explore the unsorted data using the **pan** and **zoom** widgets to find the costs for the state of **New Jersey**. Zoom in and out of the data to get a better understanding of costs for different states.  How does the total cost of diabetes payments in New Jersey compare to that of surrounding states like NY, CT, DE, and PA?

4. Sort the underlying visualization data from lowest to highest total payments, then plot a bar chart. List the 10 states with the lowest total payments for diabetes care.

5. Use the **box zoom** widget to zoom in on **all states** with total average payments **less than `$200,000`**. How many states have total payments of less than `$200,000`?

6. Reset the visualization and use the **pan** widget to see the highest point of the visualization. Then, use the **box zoom** or **wheel zoom** widgets to zoom in on the data.

7. Identify the 10 states with the **highest total average payments** for diabetes diagnostic services. What is the approximate difference in the total payments for diabetes services between the state with the 10th highest payments and the state with the highest payments?

8. Use the **Save** widget to save your visualization of the 10 states with the highest total payments.


- - -

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
