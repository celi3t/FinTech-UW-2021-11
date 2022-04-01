# Import required libraries
import streamlit as st
from datetime import datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import hashlib

# Import required libraries
@dataclass
class RecordTrade:
    buyer_id: str
    seller_id: str
    shares: float

# Our Block class
@dataclass
class Block:
    record: RecordTrade
    trade_time: str = datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = "0"

    def hash_block(self):
        # Declare a hashing algorithm
        sha = hashlib.sha256()

        # Encode the time of trade
        trade_time_encoded = self.trade_time.encode()
        # Add the encoded trade time into the hash
        sha.update(trade_time_encoded)

        # Encode the Record class
        record = str(self.record).encode()
        # Then hash it
        sha.update(record)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        # Return the hash to the rest of the Block class
        return sha.hexdigest()

# Our StockChain class
from typing import List
@dataclass
class StockChain:
    # The class `StockChain` holds a list of blocks
    chain: List[Block]
    # The function `add_block` adds any new `block` to the `chain` list
    def add_block(self, block):
        self.chain += [block]

# Add text titles to the web page
st.markdown("# Our Stock Exchange Blockchain")
st.markdown("## Enter Your Transaction Below:")

# Add an input area for the buyer
buyer = st.text_input("Buyer ID")

# Add an input area for the seller
seller = st.text_input("Seller ID")

# Add an input area for the number of shares
shares = st.text_input("Shares Transacted")

# Set up the web app for deployment (including running the StockChain class)
@st.cache(allow_output_mutation=True)
def setup():
    genesis_block = Block(
        record=RecordTrade(shares=100, buyer_id=1, seller_id=2)
    )
    return StockChain([genesis_block])

# Serve the web app
stockchain_live = setup()

# Add a button using Streamlit to add a new block to the chain
if st.button("Add Block"):
    # Pull the original block to start on
    prev_block = stockchain_live.chain[-1]

    # Hash the original block (to put into the next block)
    prev_block_hash = prev_block.hash_block()

    # Create a `new_block` so that shares, buyer_id, and seller_id from the user input are recorded as a new block
    new_block = Block(
        # data=input_data,
        record=RecordTrade(buyer, seller, shares),
        prev_hash=prev_block_hash
    )

    # Add the new_block to the existing chain
    stockchain_live.add_block(new_block)

    # Just for fun, we add a little pizzazz
    st.balloons()

# Add a title for the chain display section
st.markdown("## The Stockchain Ledger")

# Save the data from the blockchain as a DataFrame
stockchain_df = pd.DataFrame(stockchain_live.chain).astype(str)

# Display the DataFrame data
st.write(stockchain_df)

# Add a dropdown menu to allow users to select which block in the chain to display
st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", stockchain_live.chain
)

# Display the selected block on the sidebar
st.sidebar.write(selected_block)
