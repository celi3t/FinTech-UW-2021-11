# A Friends DataFrame

In this group activity, you will share your name, location, years of software experience, and technologies you have used. You will then create a DataFrame to store the data and calculate the average age of your group using the `mean` method.

## Background

To learn more about the `mean` method, refer to the ["Methods" section in the Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

## Instructions

### Part 1: Initial Setup

1. Ask each classmate in the breakout room the following:
    * Their name.
    * Their location.
    * How many years of software experience they have.
    * One technology they have experience with.

2. Import the required libraries and dependencies into your Jupyter Notebook.

### Part 2: `Series` to `DataFrame`

1. Create three dictionaries for the data collected.

    * The keys for each dictionary are the names.
    * The values for the first dictionary are the locations.
    * The values for the second dictionary are the years of experience.
    * The values for the third dictionary are the technology used.

2. Convert each dictionary into a Pandas `Series`, storing each in its own variable.

3. Create a Pandas `DataFrame` using the three `Series` as data. **Hint:** Pass them as a list to the data parameter.

4. Transpose the resulting `DataFrame`.

### Part 3: `Dictionary` to `DataFrame`

1. Create a single `dictionary` where the keys are your classmates' names and the other values are stored in a list.

    For example:

    ```python
    my_classmates = {
      "Anna": ["London",1,"Java"],
      "Mohammad" : ["Chicago",0,"Microsoft Office"],
    }
    ```

2. Create a Pandas DataFrame, using the my_classmates dictionary as the data. **Hint:** Use the `index` parameter and label the column names with ["City", "Software Experience", "Technologies Used"].

3. Transpose the DataFrame.
### Part 4: Manipulate the `DataFrame`

1. View the data in the `DataFrame`'s City column.

2. Using the `mean` method, calculate the average years of software experience of the group.

3. For one of your classmates, increase their years of software experience by 1 year.

Be prepared to share some of your solutions with the class when you return from the breakout room.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
