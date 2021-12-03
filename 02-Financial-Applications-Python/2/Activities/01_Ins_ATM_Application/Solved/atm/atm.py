"""This is a simple ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python atm.py
"""

import sys
import fire
import questionary

from utils import (
    load_accounts,
    validate_pin,
)

from actions.make_deposit import make_deposit

from actions.make_withdrawal import make_withdrawal


def login():
    """Login to the ATM using an account PIN."""

    # Initial CLI asking user to input PIN
    pin = questionary.text("Please enter your 6 digit PIN number:").ask()

    # Calls validate_pin() function to confirm length.
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


def main_menu():
    """Dialog for the ATM Main Menu."""

    # Determines action taken by application.
    action = questionary.select(
        "Would you like to check your balance, make a deposit or make a withdrawal?",
        choices=["check balance", "deposit", "withdrawal"],
    ).ask()
    return action


def run():
    """The main function for running the script."""

    # Initiates login process. If pin verified, returns validated account.
    account = login()

    # Initiates ATM action: check balance, deposit or withdrawal.
    action = main_menu()

    # Processes the chosen action
    if action == "check balance":
        sys.exit(f"Your current account balance is {account['balance']: .2f}")
    elif action == "deposit":
        account = make_deposit(account)
    else:
        account = make_withdrawal(account)

    # Prints the adjusted balance.
    print(
        f"Thank you for your {action}. Your adjusted balance is ${account['balance']: .2f}."
    )

    # @TODO: As a bonus, try writing the adjusted account balance back to the CSV file.


# Entry point for the application. Initiates the run() function.
if __name__ == "__main__":
    fire.Fire(run)
