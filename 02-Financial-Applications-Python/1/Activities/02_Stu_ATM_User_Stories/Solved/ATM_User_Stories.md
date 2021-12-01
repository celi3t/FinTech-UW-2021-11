# ATM User Stories

Here are some examples of pseudocode for the ATM user stories:

  * As a user of an ATM, I: **input my PIN for identification.**
  ```
  # Import data that has usernames and corresponding pins
  # Store it in a Python dictionary
  # Ask the user for their username and store it in a variable
  # Then create a PIN variable and ask the user to input their PIN
  # Look up the PIN associated with the provided username
  # Check to see the true PIN is the same as the entered PIN
  # If it is, proceed to the next part of the program
  # If it isn't, display an error message and prompt the user to try entering the PIN again
  # Give the user a set number of attempts (such as 4) to enter the correct PIN
  # Display the attempt number each time and explain when they will be locked out of their account
  ```

  * As a user of an ATM, I: **identify whether I’m going to make a deposit or withdrawal.**
```
  # Display "deposit or withdrawal" to the user
  # Allow the user to input a selection
  # Make sure the selection is either deposit or withdrawal
  # If the selection is not deposit or withdrawal, display an error message
  # Allow the user to make a correct selection
```
  * As a user of an ATM, I: **input the amount of my deposit or withdrawal.**
```
  # Display text to the user telling them to input an amount, in dollars
  # If the amount is not positive, display an error message
  # Allow the user to try again until there is no error
```
  * As a user of an ATM, I: **receive cash.**
```
  # Confirm that there is enough money in the account to allow withdrawal
  # Subtract the withdrawal amount from the account balance
  # Display a message to the user telling them that they have received cash
```
  * As a user of an ATM, I: **deposit cash and checks.**
```
  # Ask the user if they are depositing cash or checks
  # Ask the user how many checks they are depositing
  # Ask the user which account they would like to deposit the check into
  # Update the balance of the selected account 
  # Display a message to the user that confirms the deposit
```
  * As a user of an ATM, I: **want to receive my adjusted account balance.** 
```
  # Ask the user which account they would like to see
  # Display the account balance
```

## ATM Software Requirements:

Software developers must also be aware of software and compliance requirements ahead of the development process. Some of these were included in the answers above.

Specify any compliance or validation requirements that should be associated with basic ATM functionality:

* Verify that the PIN is valid.

* Validate that the deposit or withdrawal amount is a positive number.

* Verify that there are enough funds in the account to cover the withdrawal.

With these user stories and system requirements in mind, we can start to convert the specifications into code.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
