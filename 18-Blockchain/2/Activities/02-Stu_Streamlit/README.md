# Streamlit Enhancements

## Background

In this activity, you will gain practice using the Streamlit package to serve up blockchain applications written in python.

Think about any additional information that might be important to record as part of a share transaction. For example:

* The form of payment for the shares (e.g., USD, Bitcoin, Euro, etc.).

* Current value of these shares in BTC.

* Transaction fees charged.

## Instructions

Use the provided starter code and follow the next steps to accomplish this activity:

* Create attributes for some of the following transaction features in your blockchain, and update the `streamlit` application to reflect these attributes. Specifically:

  * Add `payment_method` and `transaction_fee` attributes to your `RecordTrade` class. The `payment_method` attribute should take in a `str`. The `transaction_fee` attribute should be a `float` that is 0.10% (one-tenth of one percent).

  * In your web application, create an input text box that allows users to specify the payment method they want to use.

  * Again in your web application, using markdown, add a disclosure to users that states the `transaction_fee` to be charged.

  * Add a default value (for example: "USD") for our `payment_method` on the genesis block in the `setup` function.

  * Time permitting, add any additional information you think would be relevant for a stock exchange blockchain to your `Block` class. If they require user entry, make sure to add `text_input` for them using `Streamlit`.

  * Deploy a local copy of the blockchain in your browser using `Streamlit`.

  ---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
