# Indexing Loans

In this activity, you will access data from a Pandas DataFrame in order to analyze customers who are seeking three-year loans. Review the compilation of loan data, and then filter out the necessary data to generate insights about customers who have been granted three-year loans.

## Instructions

1. Using the Pandas `read_csv` function and the Path module, read in the `loans.csv` file from the `Resources` folder and create the Pandas DataFrame. Review the first five rows of the resulting DataFrame.

2. Using `iloc`, show the first 10 records of the data.

3. Generate the summary statistics for all of the `loans.csv` data.

4. Using `iloc`, create a subset DataFrame, `filtered_df`, by selecting only the following columns:

    * `loan_amnt`
    * `term`
    * `int_rate`
    * `emp_title`
    * `annual_inc`
    * `purpose`

5. Using `loc`, filter `filtered_df` by row values where `term` is equal to `36 months` in order to focus on only three-year loan records.

6. Modify rows with `term` values equal to `36 months` to be `3 years`.

7. Use the `isnull` and `sum` functions to evaluate the number of missing values in the `term_df` DataFrame. Use the `fillna` function to replace the NaN values with 'Unknown'. Review the first five rows of the new DataFrame.

8. Generate the summary statistics for `term_df` after all modifications.

9. Use the `value_counts` function on the `emp_title` column of the `term_df` DataFrame to view the unique value counts for employee titles of three-year loan customers.

10. Use the `value_counts` function on the `purpose` column of the `term_df` DataFrame to view the unique value counts for loan purposes of three-year loan customers.

11. Filter `term_df` by rows with `annual_inc` greater than `80000`. Use the `describe` function to view the mean `int_rate` of three-year loan customers with annual incomes greater than $80,000.

12. Filter `term_df` by rows with `annual_inc` less than `80000`. Use the `describe` function to view the average `int_rate` of three-year loan customers with annual incomes less than $80,000.

13. Answer the following questions about individuals taking out three-year loans:

    * What kind of customers (employee title) seem to ask for three-year loans most frequently?

    * What are three-year loans generally used for?

    * What is the difference between counts of three-year loan customers with annual incomes greater than 80,000, compared to those with annual incomes less than 80,000?

    * What is the difference between interest rates for customers with annual incomes greater than 80,000 compared to those with annual incomes less than 80,000?
    
## Hint

Refer to the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) for additional explanations about using specific functions.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
