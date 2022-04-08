# Streamlit Application

# Imports
import streamlit as st

# Import the functions from ethereum.py
from ethereum import w3, generate_account, get_balance, send_transaction
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

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

# Call the get_balance function and write the account balance to the screen
ether_balance = get_balance(w3, account.address)
st.write(ether_balance)

#######################################

# An Ethereum Transaction
st.text("\n")
st.text("\n")
st.markdown("## An Ethereum Transaction")

# Create inputs for the receiver address and ether amount
receiver = st.text_input("Input the receiver address")
ether = st.number_input("Input the amount of ether")

# Create a button that calls the `send_transaction` function and returns the transaction hash
if st.button("Send Transaction"):

    transaction_hash = send_transaction(w3, account, receiver, ether)

    # Display the Etheremum Transaction Hash
    st.text("\n")
    st.text("\n")
    st.markdown("## Ethereum Transaction Hash:")

    st.write(transaction_hash)
