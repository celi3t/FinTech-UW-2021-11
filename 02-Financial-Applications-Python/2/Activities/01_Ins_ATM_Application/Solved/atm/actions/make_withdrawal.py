"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Adjusts account balance for withdrawal.

        Script that verifies withdrawal amount is valid, confirms that withdrawal amount is less than account balance, and adjusts account balance.

        Arg:
            account(dict): contains pin and balance for account

        Return:
            account(dict): returns account with balance adjusted for withdrawal

    """
    # Use questionary to capture the withdrawal and set equal to amount variable
    amount = questionary.text("How much would you like to withdraw?").ask()
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
