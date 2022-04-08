# Cats Mini Project

## Background

Students are a developer working for a large e-commerce and gaming platform that wishes to expand their customer base and begin selling virtual cats online. They have tasked you a skilled blockchain developer with building the first prototype that has a user interface and checks account balances before allowing transactions to be sent.

## Instructions

Complete each of the following steps:

1. In the `Unsolved` folder, create your `.env` file, which will save your mnemonic seed phrase in the variable `MNEMONIC`.

2. Navigate to your Ganache application and copy the mnemonic seed phrase into the `.env` file.

3. Inside the `generate_account` function, use the `Wallet()` class from the bip44 package, to generate a wallet instance. Then, derive your private and public keys by calling the `.derive_account` method on the `wallet` object and passing it the string “eth”. Save the two returned values as variables named `private` and `public`.

4. Pass the private-key value to `Account.privateKeyToAccount`, and save the returned `account` object as a variable named `account`.


5. Then, build a `get_balance` function that will fetch the balance of your Ethereum address by using Web3.py. To do so, complete the following steps:

* Create a function named `get_balance` that accepts two arguments, `w3` and `address`.

* Call the `w3.eth.getBalance` method, and pass it the `address` variable. Save the returned value as a variable named `wei_balance`.

* Call the function `w3.fromWei`, and pass it your `wei_balance` variable and the string “ether”. Save the returned value as a variable named `ether`.

* Return the account balance in ether.

6. Navigate to the `cat_shop.py` file.

7. Import the `w3` and the following functions from the `crypto_wallet.py` file:

* `generate_account`

* `get_balance`

8. Review the provided code, as you will be adding to it to build your application.

9. Inside the `get_cats` function in the for loop use `st.write` to add the objects from the object above into the code which provides the cats’ information such as the price and name.

10. Then, create Streamlit application headings using `st.markdown` to explain this app is for buying cats.

11. Call the `generate_account` function and save it as a variable  called `account` be sure to pass in `w3`.

12. Call the `get_balance` function and save it as a variable `ether`.

13. Create a select box to choose a Cat using `st.sidebar.selectbox`

14. Create a header using ` st.sidebar.markdown()` to display cat name and price.

15. Then, create a variable called `cat_price` to retrieve the cat price from the `cat_database` using block notation.

16. Finally, use a conditional statement using the `if` keyword to check if the selected cat can be purchased. This will be done by checking the user's account balance that wishes to make the purchase by checking if the `ether` variable we created is greater than or equal to the `cat_price`.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
