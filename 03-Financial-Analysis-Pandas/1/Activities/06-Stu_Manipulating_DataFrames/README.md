# Manipulating DataFrames

In this activity, you will manipulate the structure of a Pandas DataFrame, namely its columns. Altering the structure of a Pandas DataFrame is often necessary to fit the needs of the user.

## Instructions

1. Import the Pandas, pathlib, and NumPy libraries.

2. Create a variable named `csvpath` that represents the path to `people.csv` by using the Path module from the pathlib library.

3. Read the CSV file into a Pandas DataFrame, using the Pandas `read_csv` function and the `csvpath` variable. View the first five rows of the DataFrame.

4. View the column names of the Pandas DataFrame.

5. View the column data types of the Pandas DataFrame.

6. Rename the columns of the Pandas DataFrame to "Person_ID", "First_Name", "Last_Name", "Email", "Gender", "University", "Occupation", and "Salary".

7. Alternatively, rename the columns of the Pandas DataFrame using a dictionary.

8. Re-order the columns of the Pandas DataFrame to "Person_ID", "Last_Name", "First_Name", "Gender", "University", "Occupation", "Salary", and "Email".

### Bonus

If you finish the activity with time to spare, try the following bonus activity. 

1. Create two additional columns: "Age" and "Age_Copy". 

2. Use the `randint` function from the NumPy library with the `low`, `high`, and `size` parameters set to `22`, `65`, and `1000`, respectively, to randomly generate an integer from 22 to 65 for 1000 rows. The following code generates the random values:

    ```python
    np.random.randint(low=22, high=65, size=1000)
    ```

3. Delete the newly created "Age_Copy" column.

4. Using the Pandas `to_csv` function, write the modified DataFrame to a new CSV. Put the file in the `Resources` folder.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
