# Enforcing Contract Terms Using Conditionals

## Background

Implementing terms and rules is a common practice in smart contracts. In this activity, you will enforce contract terms using conditionals.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the starter files, and perform the following code drills. Once you finish, compile the files to ensure the code works.

1. Use the `TradeController.sol` file to create a contract named `TradeController` that contains:

    * An unsigned integer variable `previous_price`.

    * A string variable `trade_type`.

2. Add a public function named `makeTrade` to the `LatestTrade` contract as follows:

    * Define an unsigned integer `current_price` as the unique function's parameter.

    * Into the body of the function, use an `if` statement to check if the input parameter `current_price` is less than the contract variable `current_price`, if so, set the `trade_type` string variable as "Buy" and set the `previous_price` to the `current_price`.

3. Modify the `makeTrade` function of the `LatestTrade` contract as follows.

    * Add a boolean variable `buy_anyway` as the second parameter.

    * Use an `OR ( || )` clause within the `if` statement to check if it's true that the `current_price` is less than the `previous_price` or if `buy_anyway` is true.

    * Add an `else if` statement to check if the `current_price` is greater than the `previous_price`. If it is, set the `trade_type` to "Sell" and the `previous_price` equal to the `current_price`.

    * Add an `Else` statement to set the `trade_type` to "Hold" in case the previous conditions were false.

4. Use the `PersonalSavings.sol` file to update the `PersonalSavings` contract as follows:

    * Add an `if` statement to the `withdraw` function to validate if the `recipient` address parameter is equal to the `public_savings` or the `private_savings` addresses, and the balance of the contract is greater than or equal to the `amount` parameter; if so, call the `transfer` method of the `recipient` address.

## Hints

* You can get the balance of the current contract by calling `address(this).balance` as mentioned [here](https://ethereum.stackexchange.com/a/21449).

* If you want to review how conditional operators work in Solidity, [read this page from the Solidity documentations where a full list is presented](https://docs.soliditylang.org/en/v0.5.0/types.html#booleans)

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
