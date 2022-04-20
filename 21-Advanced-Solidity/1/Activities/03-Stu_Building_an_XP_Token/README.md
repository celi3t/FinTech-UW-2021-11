# Building an XP Token

In this activity, you will leverage the `mapping` data structure to build an `XP Token` smart contract.

The `XP_Token` contract will allow you to collect Ether in exchange for `XPT` tokens that users can spend at the company's website that accepts only `XPT` tokens.

## Instructions

Complete the following steps:

1. Open up the Remix IDE, and create a new contract called `XP_Token.sol`. You can also use this [starter file](./Unsolved/XP_Token.sol).

2. After the contract is defined as `XP_Token`, add the following contract variables:

    * A `address payable` called `owner`. Set this to `msg.sender`. Since this is only called once during the deployment, you will become the contract owner.

    * A `string` called `symbol`. Set this to `XPT` and make sure that it is `public`. Setting the symbol will allow wallets like MetaMask to recognize your token's symbol/ticker.

    * Set an `exchange_rate` variable to equal the number of tokens to be distributed per `wei`. Make sure the variable is a `uint public` type!

3. Add a `mapping` data structure:

    * Create a new `mapping` called `balances` that pairs `address` to `uint`.

4. Add a new function called `balance` that is a `public view` that `returns(uint)`:

    * This function should return the `balances` of `msg.sender` by accessing the `balances` mapping, using `msg.sender` as the index/selector/key.

5. Add a new `public` function named `transfer` that accepts `address recipient` and `uint value` as parameters:

    * In this function, subtract `value` from the balance of `msg.sender` in the `balances` mapping.

    * Then, add the `value` to the `recipient` balance in the mapping.

6. Users will now need a way to purchase new `XPT` tokens! Add a `public payable` function called `purchase`. It does not need any parameters. Within the function:

    * Calculate a new `uint` called `amount` by multiplying `msg.value` with the `exchange_rate`. This equation will calculate the number of tokens to distribute.

    * Next, add the `amount` to the balance of `msg.sender`.

    * At the end of the function, transfer the `msg.value` to the `owner` address. (Remember, `owner` must be set to `payable` to call `.transfer()` on it)

7. Finally, since you as the company owner will need the ability to create new tokens when necessary, add a new function called `mint`:

    * Use the same parameters as the `transfer` function you defined earlier.

    * At the beginning of the function, `require` that the `msg.sender` is equal to `owner`. Make sure to put an error message in the `require`.

    * Then, simply add the `value` to the `recipient` address balance in the mapping.

8. Test out your contract by deploying and calling the functions that Remix exposes. Try minting some tokens using a Remix address, then sending some to another Remix address!

Celebrate the fact that you can now build what most people perceive to be magical tokens! You can extend these contracts to do anything you'd like. You can now create a complex system of value that is customizable to any use case!

## Hints

* Remember, a mapping associates one data type to another. By pairing `address` to `uint`, we can track balances.

  * For example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333` is what the data might look like in contract storage.

* For more details about how mappings work, visit the [Solidity Documentation](https://solidity.readthedocs.io/en/v0.5.13/types.html#mapping-types).

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
