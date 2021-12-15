# Concatenating Pandas DataFrames

In this activity, you will practice concatenating DataFrames and appending their data to a combined DataFrame.

## Instructions

1. Import the Pandas and Pathlib libraries.

2. Create two variables,`msft_csv_path` and `sp500_csv_path`, which represents the path to [MSFT.csv](Resources/MSFT.csv) and [SP500.csv](Resources/SP500.csv) using the Pathlib library.

3. Read the CSVs into two Pandas DataFrames named `MSFT` and `SP500`.

4. Preview the `MSFT` DataFrame.

5. Preview the `SP500` DataFrame.

6. Concatenate the `MSFT` and `SP500` DataFrames by columns using the `concat` function with the `axis` parameter set to `columns` and the `join` parameter set to `inner`.

7. Concatenate the `MSFT` and `SP500` DataFrames by rows using the `concat` function with the `axis` parameter set to `rows` and the `join` parameter set to `inner`.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
