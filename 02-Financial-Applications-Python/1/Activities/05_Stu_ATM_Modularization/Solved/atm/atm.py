"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""
import sys

from utils import (
    load_accounts,
    validate_pin,
)

from actions.make_deposit import make_deposit

from actions.make_withdrawal import make_withdrawal


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
