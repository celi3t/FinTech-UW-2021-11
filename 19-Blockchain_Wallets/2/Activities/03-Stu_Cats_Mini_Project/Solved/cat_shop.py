# Cats Mini Project

# In this part of the activity you will import the functions from your wallet.py file and create an interface using streamlit

# In this portion of the activity we will create an interface and check our balance in ether to determine if we are able to purchase a cat.

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List




# From wallet.py import the functions w3, generate_account, get_balance

from crypto_wallet import w3, generate_account, get_balance

################################################################################
# Cat Information

# Database of cats including their name, digital address, rating and in Ether.
# A single Ether is currently valued at $3,900

cat_database = {
    "Jennifurr": ["Jennifurr", 22],
    "Cheddar": ["Cheddar", 151],
    "Meowise": ["Meowise", 31],
}

# Create a list of the the cats by first names
kitties = ["Jennifurr", "Cheddar", "Meowise"]

# Create a get_cats function to display the purchase information from the cats
def get_cats():
    """Display the database of cats to purchase information."""
    db_list = list(cat_database.values())

    for number in range(len(kitties)):
        st.write("Name: ", db_list[number][0])
        st.write("Price in Ether: ", db_list[number][1], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Create Streamlit application headings using `st.markdown` to explain this app is for buying kitties
st.markdown("# Kitties")
st.markdown("## Buy a Kitty!")
st.text(" \n")

#
#
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)
#  Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(w3, account.address)

# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")

# Create a select box to chose a Cat using `st.sidebar.selectbox`
cat = st.sidebar.selectbox('Select a cat', kitties)

#  Create a header using ` st.sidebar.markdown()` to display cat name and price.
st.sidebar.markdown("## Cat Name and Price")

# Identify the cat for purchase by name
cat = cat_database[cat][0]

# Create a variable called `cat_price` to retrive the cat price from the `cat_database` using block notation.
cat_price = cat_database[cat][1]

# Use a conditional statement using the `if` keyword to check if the selected cat can be purchased. This will be done by checking the user's account balance that wishes to make the purchase.
if cat_price <= ether:
  new_balance = float(ether) - float(cat_price)
# Write the cats name to the sidebar
  st.sidebar.write("If you buy", cat, "for", cat_price, "eth, your account balance will be", new_balance, ".")
  get_cats()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", cat, "for", cat_price, "eth." )
  get_cats()
