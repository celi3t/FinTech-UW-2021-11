# Streamlit Application

# Imports
import streamlit as st
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# @TODO
# Update the imports for the functions coming from ethereum.py
from ethereum import generate_account


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")

#######################################

# Generate the Ethereum account
account = generate_account(w3)

#######################################

# The Ethereum Account Address
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)

#######################################

# Display the Etheremum Account balance
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Balance:")

# @TODO
# Call the `get_balance` function and write the account balance to the screen


#######################################

# An Ethereum Transaction
st.text("\n")
st.text("\n")
st.markdown("## An Ethereum Transaction:")


# @TODO
# Create inputs for the receiver address and ether amount


# @TODO
# Create a button that calls the `send_transaction` function and returns the transaction hash
