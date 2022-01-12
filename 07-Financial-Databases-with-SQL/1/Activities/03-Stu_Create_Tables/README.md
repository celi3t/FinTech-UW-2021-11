# Create Tables

In this activity, you will work with Python's SQLAlchemy library to create and view table data in various ways.

## Instructions

Complete the following steps:

1. Import the SQLAlchemy module.

2. Create a database connection string that imports the `mortgage_payments.db` from the Resources folder.

3. Create a [database engine object](https://docs.sqlalchemy.org/en/14/core/engines.html) that utilizes the database connection string.

4. Get the list of table names from the database engine that was just created.

5. Create a new database connection string that creates a temporary, in-memory database.

6. Create a new database engine object using the updated connection string.

7. Read the `customers.csv` file from the Resources folder into a Pandas DataFrame called `customers_df`.

8. Using the `to_sql` function, write the `customers_df` dataframe into the SQL database table named `customers`.

9. Confirm that the the `customers` table was created.

10. Using the `pd.read_sql_table` function, read the `customers` table back into a Pandas Dataframe called `sql_customers_df`.

11. Create a new database connection string for an in-memory database and a new database engine.

    > **Hint** You can copy and paste the code from steps 5 and 6.

12. Write a SQL statement that creates a table called `customer_orders`. It should contain two columns of data: the `customer_id` and the `order_total`, both of which are defined by data type BIGINT.

13. Run the execution statement that creates the table and then confirm that it was created by calling the table name.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
