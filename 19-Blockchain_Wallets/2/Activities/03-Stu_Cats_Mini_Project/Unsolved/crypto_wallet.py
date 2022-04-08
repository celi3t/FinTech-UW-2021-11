# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Wallet functionality

#@TODO create a function called generate account do not forget to add each of the following steps

def generate_account(w3):
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.


    # Create Wallet Object

    # Derive Ethereum Private Key


    # Convert private key into an Ethereum account



    return account

#@TODO create a function called generate account do not forget to add each of the following steps
def get_balance(address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei


    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in ether
    return ether
