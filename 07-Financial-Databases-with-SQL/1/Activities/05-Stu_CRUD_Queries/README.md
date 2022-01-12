# SQL CRUD

In this activity, you will apply `SQL` CRUD operations to a database of account payments. You will need to SELECT and filter data using SQL then INSERT, UPDATE, and DELETE records from the tables.

## Instructions

Complete the following steps:

1. Import the SQLAlchemy module.

2. Create a database connection string that imports the `bank_payments.db` from the Resources folder.

3. Create a [database engine object](https://docs.sqlalchemy.org/en/14/core/engines.html) that utilizes the database connection string.

4. Get a list of the tables included in the database.

5. Run a query that `SELECT`s all of the data from the `banks` table.

6. Using a SQL `SELECT` statement, find the bank routing number of the bank where the bank name equals 'TD Bank'. List the bank routing number to confirm.

7. Insert a new bank into the `banks` table. Once the query has been executed, confirm that the bank has been added to the list.
   * Use a '10' for the `bank_id`.
   * The bank name will be 'Royal Bank of Canada'.
   * The bank routing number will be '345826917'.

8. `WHERE` the bank id equals 10, `UPDATE` the bank name to 'RBC'. Confirm that the bank name has been updated.

9. `DELETE` the bank where the bank id equals to 3 from `banks` table. Confirm that the bank has been deleted.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
