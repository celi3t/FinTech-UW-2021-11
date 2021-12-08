# From CSV to DataFrame

In this activity, you will import a CSV file and create a DataFrame with a `DatetimeIndex`.

## Instructions

1. Import the required libraries and dependencies.

2. Using the Pandas `read_csv` function, import the `prices.csv` file from the `Resources` folder into a Pandas DataFrame. The `read_csv` function will take in four parameters: 

    * Using the Path module, specify the relative path to the `prices.csv` file.
    
    * Set the `index_col` parameter to specify the Date column as the index for the DataFrame.
    
    * Set the `parse_dates` parameter to `True`.
    
    * Set the `infer_datetime_format` parameter to `True`.

3. Review the first five rows of the DataFrame using the Pandas `head` function.

4. Review the last five rows of the DataFrame using the Pandas `tail` function.

5. Review both the first and last seven rows of the DataFrame from one cell by calling the Pandas `display` function in conjunction with the `head` and `tail` functions.

6. Review the basic information of the DataFrame by calling the Pandas `info` function.

7. Generate the summary statistics for the DataFrame by calling the Pandas `describe` function.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
