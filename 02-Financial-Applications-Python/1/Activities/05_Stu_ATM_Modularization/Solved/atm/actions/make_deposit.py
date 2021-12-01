"""Adjusts account balance after a deposit."""

import sys


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
