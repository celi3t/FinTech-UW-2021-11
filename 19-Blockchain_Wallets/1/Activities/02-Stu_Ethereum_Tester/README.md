# Ethereum-Tester

In this activity you will utilize the Web3.py library as well as the `ethereum-tester` library and its `EthereumTesterProvider` to interact with a mock Ethereum blockchain.

Use the Web3.py library's [web3.eth API](https://web3py.readthedocs.io/en/stable/web3.eth.html) should you have any questions about the function you are being asked to use.

## Instructions

Complete the following steps:

1. From the Web3.py library, import `Web3` and the `EthereumTesterProvider`.

2. Set the `EthereumTesterProvider` equal to a variable called `provider`.

3. Create an instance of `Web3` passing the `provider` as a parameter. Set this equal to a variable called `w3`.

4. Use the web3.eth API's `get_block` function to access the "latest" block in your mock blockchain.

5. Use the web3.eth API's `accounts` function to access a list of account addresses that can be used to create a transaction.

6. Use the web3.eth API's `get_balance` function to determine the wei balance in one of the accounts.

7. Use Web3.py's `fromWei` function to calculate the number of ether in the account specified in step 6.

8. Create and assign the following 4 variables:

    * `sender` - assign it a value of one of the addresses from step 5.

    * `receiver` - assign it a different address from step 5.

    * `gas` - assign it a minium of 21000 units.

    * `value` - the value should be the number of ether you want to send, but you will need to use the `toWei` function to convert it to the required wei.

9. Use the web3.eth API's `send_transaction` function to send a transaction to the mock Ethereum blockchain.

10. Use the web3.eth API's `get_transaction` function to find the details of the transaction, also known as the transaction object, sent in step 9.

  > Hint:  You will need to use the transaction hash returned from the transaction to complete this step.

11. Use the web3.eth API's `get_block` function to access the "latest" block in your mock blockchain. Has the block information changed from what was returned in step 4?

12. Use the web3.eth API's `replace_transaction` function to update the units of `gas` in the original transaction. **NOTE:** This step will result in an ERROR - why do you think this occurs?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
