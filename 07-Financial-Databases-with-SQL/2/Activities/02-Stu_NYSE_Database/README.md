# NYSE DataFrames and Databases

In this activity, you will read, clean and load data to a database table.

## Instructions

### Create the Pandas DataFrame

1. Import the modules for Pandas, the Path, and SQLAlchemy.

2. Read the `nyse_companylist.csv` file from the Resources folder into a Pandas DataFrame called `nyse_df`. Review the DataFrame.

3. Check the data types (`dtypes`) of each column in the DataFrame.

### Clean the Pandas DataFrame

1. Apply the provided `clean_currency` function to the 'MarketCap' column of the `nyse_df` DataFrame.

* The `clean_currency` function performs the following actions:
  -Removes non-numeric characters (ie '$', 'M', and 'B') from the data entry
  -Converts the value to a float
  -Scales the data according to the suffixes 'M' and 'B'
  -Returns the cleaned and scaled data entry

2. Review the contents of the 'MarketCap' column to confirm that data has been cleaned as expected.

### Load the DataFrame into a SQLite Database

1. Create a database connection string that loads the SQLite database called `nyse.db` into the Resources folder.

2. Create a [database engine](https://docs.sqlalchemy.org/en/14/core/engines.html) called `nyse_engine`. Be sure to include the `echo=True` parameter.

3. Using the Pandas [`to_sql`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html) function, write the `nyse_df` DataFrame to a table called `NYSE` in the `nyse.db`. Be sure to include the parameters for `index` and `if_exists`.

4. Get the table name from the database to confirm it was created.

### Query the SQL Database

1. Write a SQL query to select all companies in the Technology sector AND in the Software industry AND that have a market cap greater than 30 billion USD.

2. Using the Pandas [`read_sql_query`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html) execute the SQL query and assign the results to a new Pandas DataFrame called `nyse_tech_companies_df`.

3. Review the DataFrame.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
