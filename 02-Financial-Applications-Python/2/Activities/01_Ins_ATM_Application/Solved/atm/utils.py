"""Helper functions for loading accounts and validating PIN number."""

import csv
from pathlib import Path
import sys


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
        print(f"The length of your PIN is valid")
        return True
    else:
        return False

# input accounts: list of dictionaries  [{acc1}, {acc2}, {acc3}]
def update_accounts(account, accounts):
    updated_accounts = []
    for acc in accounts:
        if acc['pin'] == account['pin']:
            acc['balance'] = account['balance']
        updated_accounts.append(acc)
    csvpath = Path('data/updated_accounts.csv')
    with open(csvpath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        csvwriter.writerow( ["pin", "balance"] )
        for acc in updated_accounts:
            csvwriter.writerow( [acc['pin'], acc['balance']] )
