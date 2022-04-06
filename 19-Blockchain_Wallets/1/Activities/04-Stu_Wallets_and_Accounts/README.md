# Wallets and Accounts


This activity will give you the opportunity to solidify your understanding of the relationship between the mnemonic seed phrase you just created and how it is used in relationship to the HD wallet, the creation of a private key, and ultimately the Ethereum account and address.

## Instructions

Complete the following steps:

1. In the Unsolved folder for this activity, create a `.env` file. Inside the `.env` file create a variable called `MNEMONIC` and set it equal to the mnemonic seed phrase that you created in the prior activity.

2. Call the `os.getenv` function and pass it the mnemonic variable from the `.env` file. Set that equal to the variable `mnemonic`. Confirm the data type of the `mnemonic` variable to confirm it was imported from the `.env` file properly.

3. Create your digital `wallet` by calling the `Wallet` module and passing it your mnemonic seed phrase.

4. Create your public/private key pair by calling the `derive_account` function on your digital wallet and passing it the argument "eth" to confirm you are creating the keys for an Ethereum account. Display the byte strings for both your public and private keys.

5. Create your Ethereum account by calling the `privateKeyToAccount` function on the `Account` module and passing it your private key. View the account object.

6. Print the hash codes associated with the account's address and private keys.

7. Create and encode a message to be included in a signed Ethereum transaction.

8. Using the Web3 eth API's [`account.sign_message` function](https://web3py.readthedocs.io/en/stable/web3.eth.account.html#sign-a-message), create a signed message by passing in the encoded message and your private key.

9. To verify the message was created and signed, call the [`account.recover_message` function](https://web3py.readthedocs.io/en/stable/web3.eth.account.html#verify-a-message) and pass it the encoded message and the message signature.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
