# Import required libraries
import streamlit as st
from datetime import datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import hashlib

# Our Block class
@dataclass
class Block:
    shares: Any
    buyer_id: int
    seller_id: int
    trade_time: str = datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = "0"

    def hash_block(self):
        # Declare a hashing algorithm
        sha = hashlib.sha256()

        # Encode the time of trade
        trade_time_encoded = self.trade_time.encode()
        # Add the encoded trade time into the hash
        sha.update(trade_time_encoded)

        # Turn the shares data into an encoded string
        data = str(self.shares).encode()
        # Add the encoded shares traded data into the hash
        sha.update(data)

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
