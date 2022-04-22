# Building an ERC20 token with OpenZeppelin

In this activity, you will build an official ERC20-compatible version of the `XP_Token` using the OpenZeppelin libraries.

## Instructions

The starter code will contain imports of the ERC20 and ERC20Detailed standards and the basic XP_Token contract structure.

Complete the following steps to make the contract operational:

1. Starting with the `onlyOwner` modifier, add a `require` that checks to see if `msg.sender` is equal to the `owner` of the contract.

    * Leave the underscore `_;` at the end of the function so the Solidity program returns to the function that called the modifier.

2. For the constructor function's definition, perform the following:

    * Pass in the variables that ERC20Detailed expects, which are `string name`, `string symbol`, and `uint decimals`. Use the following values:

      * `"XP_Token"` for the first parameter.

      * `"XPT"` as the second parameter.

      * `18` as the third parameter. This sets our token's `decimals` variable to be the same as Ethereum's ether.

3. Within the constructor, set `owner` to be the `msg.sender`. Then, call the internal `_mint` function and give the `initial_supply` to the `owner`.

4. In the `mint` function, call the internal `_mint` function the same way, only pass the `recipient` and `amount` parameters to `_mint` instead.

5. Finally, restrict the `mint` function only to be called by the owner by adding `onlyOwner` to the function's modifiers. Add the `onlyOwner` modifier after the `public` modifier.

6. Compile, deploy and test your XP_Token contract. Start by creating an initial supply of tokens and confirm the balance. Transfer tokens to another Remix address and then check the owner's new token balance.


## Hints

* The OpenZeppelin documentation for the [ERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) standard for assistance with the function names and parameters.

* The [ERC20Detailed](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#ERC20Detailed) section will provide more information about the contract extension.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
