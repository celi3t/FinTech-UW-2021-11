# JSON Practice

In this activity, you'll practice converting JSON files to Pandas DataFrames. You will read a JSON file containing housing data from Alberta, Canada, and then convert that JSON object to a DataFrame.

### Instructions

1. Import the required libraries and dependencies. 

2. Set paths to the JSON files. The files contain a JSON object that was returned from a request to the financial API Quandl.

3. Create an empty dictionary in which to read the JSON object. 

4. Using `json.load`, read the JSON object into the `response` dictionary.

   **Hint:** You can use [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) to create a file handle to pass to `json.load`.
   
5. Closely examine the structure of the `response` dictionary. There is a list named `column_names` that contains the names for the data columns held in the JSON object. Retrieve this list and store it in a variable named `column_names`. 

6. Create a `DataFrame` from `response` by doing the following: 
  
    - Create an empty list named `list_series`.
    
    - Create a `for` loop that iterates over each row in `data`.
    
    - Append a new Series for each row into `list_series`.
    
    - Create a new DataFrame for the list of Series after the list is fully populated.
    
    **Note:** `pandas.DataFrame.from_dict` will not return a DataFrame with only the data values and column names.
    
7. Using the column names found previously, set the DataFrame column names using the `column` attribute.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
