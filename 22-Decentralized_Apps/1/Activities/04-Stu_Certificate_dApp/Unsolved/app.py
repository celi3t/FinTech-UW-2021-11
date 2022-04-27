import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load Art Gallery ABI
    # @TODO: YOUR CODE HERE!

    # Set the contract address (this is the address of the deployed contract)
    contract_address = # @TODO: YOUR CODE HERE!

    # Get the contract using web3
    contract = # @TODO: YOUR CODE HERE!

    return contract


# Load the contract
contract = load_contract()


################################################################################
# Award Certificate
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
# Select or enter a recipient address using a Streamlit component
student_account = # @TODO: YOUR CODE HERE!
# Enter a text string for the certificate or link to digital certificate location
certificate_details = # @TODO: YOUR CODE HERE!
if st.button("Award Certificate"):
    # Call the awardCertificate function with web3
    # @TODO: YOUR CODE HERE!
    transact({'from': account, 'gas': 1000000})

################################################################################
# Display Certificate
################################################################################
certificate_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1)
# @TODO: YOUR CODE HERE!
if st.button("Display Certificate"):
    # Get the certificate owner
    certificate_owner = # @TODO: YOUR CODE HERE!
    st.write(f"The certificate was awarded to {certificate_owner}")
    # Get the certificate's URI
    certificate_uri = # @TODO: YOUR CODE HERE!
    st.write(f"The certificate's tokenURI metadata is {certificate_uri}")
