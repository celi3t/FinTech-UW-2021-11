# Variables

# This is a comment - any code commented out is not run -
# meaning that any code or text commented out is ignored.

"""
This is a multi-line comment.
You can comment out many lines at once.
For the most part you will see single line comments
As in single line comments, any code contained within multi-line comments is not run -
meaning that any code commented out is ignored.
"""

# Topic: Strings

# Create a variable named `subject` with no value (None).
subject = None

# Assign a value of "Programmers to the variable `subject`.
subject = "Programmers"

# Create a variable, `first_name`, and assign it a value of an empty string.
first_name = ""

# Assign a value of "Ada" to the variable `first_name`.
first_name = "Ada"

# Create a variable, `last_name`, and assign it a value of a string, "Lovelace".
last_name = "Lovelace"



# Topic: Integers

# Create a variable, `birth_year`, and assign it with an integer of 1815.
birth_year = 1815

# Create a variable, death_year, and assign it with an integer of 1852.
death_year = 1852

# Create a variable, age_at_passing, and assign it a value of death_year minus birth_year.
age_at_passing = death_year - birth_year


#Topic: Print

# Print: "First Name: " and `first_name`.
print(f"First Name: {first_name}")

# Print: "Last Name: " and `last_name`.
print(f"Last Name: {last_name}")


#Topic: Concat Values

# Create and print a variable, `statement_one`, by assigning it a value of a string:
# "Programmers: Ada Lovelace was born in 1815, and she lived to be  37 years old."
statement_one = f"{subject}: {first_name} {last_name} was born in {birth_year}, and she lived to be {age_at_passing} years old."
print(statement_one)
