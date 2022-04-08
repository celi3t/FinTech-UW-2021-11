# Streamlit Application

# Imports
import streamlit as st
from ethereum import generate_account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
################################################################################

# Import the functions from ethereum.py
account = generate_account(w3)


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)
