"""Adjusts account balance after a withdrawal"""

import sys


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
