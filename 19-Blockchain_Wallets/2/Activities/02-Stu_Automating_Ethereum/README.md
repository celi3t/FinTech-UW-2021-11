# Automating Ethereum

In this activity, you will be adding functions that automate the process of accessing the balance from the Ganache blockchain as well as sending a signed transaction to the Ganache blockchain. These functions will then be incorporated into the Streamlit web application.

## Instructions

This function will be broken down into two main sections:

  1. Create the `get_balance` function and add it to the Streamlit application.

  2. Create the `send_transaction` function and add it to the Streamlit application.

Complete the following steps:

Start by adding your mnemonic seed phrase to the `SAMPLE.env` file included in the activity's Unsolved folder. Once the variables have been added, resave this as a `.env` file.

Section 1: Create the `get_balance` function and add it to the Streamlit application

  1. Open the `etherum.py` file.

  2. Create a Python function called `get_balance`. The function will take two arguments: `w3` and `address`.

  3. Call the `w3.eth.get_balance` function and pass it the `address` argument. Set this function call equal to a variable called `wei_balance`.

  4. Call the `w3.fromWei` function and pass it `wei_balance` as an argument. Specify that you want to convert the wei balance to ether. Set this call equal to a variable called `ether`.

  5. Return the `ether` balance from the function.

  6. Open the `app.py` file.

  7. Import the `w3`, `get_balance`, and `generate_account` functions from the `ethereum.py` file.

  8. In the `Display Ethereum Account Balance` section, call the `get_balance` function and pass it `w3` and `account.address`. Set this function call equal to a variable called `ether_balance`.

  9. Write the `ether_balance` to the Streamlit page.

  10. Save your files. Navigate to the Unsolved folder inside a terminal instance. Run the application by typing `streamlit run app.py`.  Both your account address and ether balance should display to the Streamlit page.

Section 2: Create the `send_transaction` function and add it to the Streamlit application

  1. Return to the `ethereum.py` file.

  2. Create a Python function called `send_transaction`. The function will take four arguments called `w3`, `account`, `receiver`, and `ether`.

  3. Inside the function, set a medium gas price strategy by calling the function `w3.eth.setGasPriceStrategy(medium_gas_price_strategy)`.

  4. Call the `w3.teWei` function and pass it the argument `ether`. You will also need to specify that "ether" is the denomination of the value being converted. Finally, set this function call equal to the variable `wei_value`.

  5. Estimate the gas it will take to mine the transaction. Call the function `w3.eth.estimateGas` and pass it 3 arguments as key:value pairs:

  ```python
  { "to": receiver, "from": account.address, "value" : wei_value}
  ```

  This function should be set equal to the variable `gas_estimate`.

  6. Construct the transaction object. Set the transaction object equal to the variable `raw_tx`. The keys you will need complete are: "to", "from", "value", "gas", "gasPrice" (the corresponding value is `w3.eth.generateGasPrice`) and the "nonce" (the corresponding value is `w3.eth.getTransactionCount(account.address)).

  7. Call the `account.signTransaction` function and pass it the `raw_tx` as an argument. Set this equal to a variable called `signed_tx`.

  8. Return the `w3.eth.sendRawTransaction` function. You will need to pass `signed_tx.rawTransaction` as the function argument.

  9. Navigate back to the `app.py` file.

  10. Import the `send_transaction` function from the `ethereum.py` file.

  11. In the `An Ethereum Transaction` section, create two user input fields:

      * A text input field that will take in the receiver's Ethereum address. Set this equal to a variable called `receiver`

      * A number input field that will take in the amount of ether to be sent in the transaction. Set this equal to a variable called `ether`

  12. Create a streamlit button that reads "Send Transaction"

  13. Inside the button, call the `send_transaction` function and pass four arguments: `w3`, `account`, `receiver` and `ether. Set this function call equal to a variable called `transaction_hash`.

  14. Create an streamlit markdown line that reads "## Ethereum Transaction Hash:"

  15. Write the `transaction_hash` to the page.

  16. Save your files. Navigate to the Unsolved folder inside a terminal instance. Run the application by typing `streamlit run app.py`.  Both your account address and ether balance should display to the Streamlit page. Now add values to the `receiver` and `ether` input fields and click the "Send Transaction` button.  After a bit, a transaction hash should be displayed to the screen.

  17. Pat yourselves on the back! This was a challenging activity to complete. You did a fabulous job putting all of the pieces together.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
