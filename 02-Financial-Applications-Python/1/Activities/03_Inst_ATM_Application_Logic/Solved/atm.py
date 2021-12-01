"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python app.py
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3258.42}
]

# Create the `login` function for the ATM application.

def login(pin):
    for account in accounts:
        if int(pin) == account["pin"]:
            print(f"The account balance for PIN {account['pin']} is {account['balance']}.")
        return account["balance"]


account_balance = login(123456)
print(f"{account_balance}")
