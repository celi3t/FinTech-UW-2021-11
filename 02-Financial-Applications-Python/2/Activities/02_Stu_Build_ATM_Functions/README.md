# Build ATM Functions

In this activity, you will complete the two missing functions in the ATM application: `validate_pin` and `make_withdrawal`.

## Files

Use the following files to complete this activity.

[ATM Application Folder](Unsolved/atm)

[requirements.txt](Unsolved/atm/requirements.txt)

## Background

Equipped with the user stories and the provided code, your task is to write the code for the `validate_pin` and `make_withdrawal` functions. You'll also need to complete the multiline docstring for the `make_withdrawal` function.

Additionally, this activity will include setting up a new `atmdev` environment and installing the libraries from the `requirements.txt` file.

When you've coded the functions, run your ATM application to determine if it works. If not, use this as an opportunity to practice your debugging skills.

### ATM Application User Stories

* As a user of an ATM, I input my PIN for identification.

* As a user of an ATM, I identify if I am going to make a deposit or withdrawal.

* As a user of an ATM, I input the amount of my deposit or withdrawal.

* As a user of an ATM, I want to receive my adjusted account balance.

### ATM Application System Requirements

* Verify that the PIN is valid.

* Validate that the deposit or withdrawal amount is a positive number.

* Verify that there are enough funds in the account to cover the withdrawal.


## Instructions

1. Create a new development environment called `atmdev` and install the libraries contained in the `requirements.txt` file.

  * From your terminal instance, create a new virtual environment called `atmdev`, using the following code:

    ```code
    conda create -n atmdev python=3.7 anaconda
    ```

  * Activate the new `atmdev` environment as follows:

    ```code
    conda activate atmdev
    ```

  * Navigate to the root of this activity folder and install the provided `requirements.txt` using the following code:

    ```code
    pip install -r requirements.txt
    ```

2. Open [`atm.py`](Unsolved/atm/atm.py) and review the Python script. Then open [`utils.py`](atm/utils.py) and [`make_withdrawal.py`](Unsolved/atm/actions/make_withdrawal.py). You'll be completing the following functions:

  * `verify_pin(pin)`, located in the utils module

    * Verify that the length of the pin is six characters.

      * If true, print a validation message and return `True`.

      * If false, then return `False`.

  * `make_withdrawal(account)`, located in the actions folder

    * Use `make_deposit(account)` as a guide.

    * Complete the docstring using the docstring from `make_deposit(account)` as a guide.

    * Use the Questionary library to ask the user how much they want to deposit. Set the return equal to the variable `amount`. Make sure that `amount` is a floating point value.

    * If `amount` is less than or equal to 0.0, exit the system with an error message indicating that it’s not a valid withdrawal amount.

    * Validate that `amount` is less than or equal to `account["balance"]`.

      * If the amount is valid, adjust the `account["balance"]` for the withdrawal, and print a confirmation message and return the adjusted account.

      * If the amount isn't valid, exit the system with an error message that tells the user that they don't have enough money in the account to cover the withdrawal.

3. Run your application!

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
