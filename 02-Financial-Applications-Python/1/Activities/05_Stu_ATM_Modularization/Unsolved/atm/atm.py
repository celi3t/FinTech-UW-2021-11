"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""

import csv
import sys
from pathlib import Path


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 6 digits long."""

    # Verifies length of pin is 6 digits prints validations message and return True. Else returns False.
    if len(pin) == 6:
        print(f"Your PIN is valid")
        return True
    else:
        return False


def main_menu():
    """Dialog for the ATM Main Menu."""

    # Determines action taken by application.
    action = input("Would you like to check your balance (b), make a deposit (d) or make a withdrawal (w)? Enter b, d, or w. \n")
    return action


def login():
    # Calls validate_pin() function to confirm length.

    pin = input("Please enter your pin:\n")
    if not validate_pin(pin):
        sys.exit("Sorry, your account PIN is not valid. It must be 6 digits in length.")

    # If pin validates, calls load_accounts() and then verifies pin against accounts list. Returns account that matches pin.
    accounts = load_accounts()

    for account in accounts:
        if int(pin) == account["pin"]:
            return account
        # If no account was returned above, exit with an error

    sys.exit(
        "Sorry, your login was not successful. Your PIN does not link to an account. Please check your PIN and try again."
    )


def make_deposit(account):

    # Use input to determine the amount of the deposit
    # Re-type amount from a string to a floating point number.
    amount = input("How much would you like to deposit?\n")
    amount = float(amount)

  # Validates amount of deposit. If true processes deposit, else returns error.
    if amount > 0.0:
        account["balance"] = account["balance"] + amount
        print(f"Your deposit was successful.")
        return account
    else:
        sys.exit(f"This is not a valid deposit amount. Please try again.")


def make_withdrawal(account):

    # Use input to determine the amount of the withdrawal
    # Re-type amount from a string to a floating point number.
    amount = input("How much would you like to withdraw?\n")
    amount = float(amount)

    # Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit("This is not a valid withdrawal amount. Please try again.")

    # Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Your withdrawal was successful!")
        return account
    else:
        sys.exit(
            "You do not have enough money in your account to make this withdrawal. Please try again."
        )


def run():

    # Initiates login process. If pin verified, returns validated account.
    account = login()

    # Initiates ATM action: check balance, deposit or withdrawal.
    action = main_menu()

    # Processes the chosen action
    if action == "b":
        sys.exit(f"Your current account balance is {account['balance']}")
    elif action == "d":
        account = make_deposit(account)
    elif action == "w":
        account = make_withdrawal(account)

    # Prints the adjusted balance.
    print(
        f"Thank you for using this atm. Your adjusted balance is ${account['balance']: .2f}."
    )


if __name__ == "__main__":
    run()
