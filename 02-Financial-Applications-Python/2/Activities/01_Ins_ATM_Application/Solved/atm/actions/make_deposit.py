"""Deposit Dialog."""

import sys
import questionary


def make_deposit(account):
    """Adjusts account balance for deposit.

        Script that verifies deposit amount is valid and adjusts account balance.

        Arg:
            account(dict): contains pin and balance for account

        Return:
            account(dict): returns account with balance adjusted for deposit

    """
    # Use questionary to capture the deposit amount.
    amount = questionary.text("How much would you like to deposit?").ask()
    amount = float(amount)

   # Validates amount of deposit. If true processes deposit, else returns error.
    if amount > 0.0:
        account["balance"] = account["balance"] + amount
        print(f"Your deposit was successful.")
        return account
    else:
        sys.exit(f"This is not a valid deposit amount. Please try again.")
