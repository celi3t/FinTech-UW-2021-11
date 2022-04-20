# Securing an XP_Token

In this activity, you will implement the SafeMath library and use it for all math operations to secure your token from integer underflow and overflow vulnerabilities, as well as other math-related vulnerabilities.

## Instructions

Complete the following steps:

1. Navigate to Remix, and open up your `XP_Token` contract. You can also use this [starter file](./Unsolved/XP_Token.sol).

2. Add the following import statement just below the `pragma` and above the `contract XP_Token` definition:

  ```solidity
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
  ```

* You can find this URL later by a quick internet search for "OpenZeppelin SafeMath" and copying the "raw" URL to the contract from GitHub. You may do this with any other contract library in the future as well.

3. Add the following as the first line of code in your smart contract:

  ```solidity
  using SafeMath for uint;
  ```

This will link the SafeMath library to the `uint` type, allowing us to call `.add()`, `.sub()`, `.mul()`, `.div()`, and so on directly from a `uint` instead of using `+`, `-`, `*`, and `/`.

4. Replace every math operation in the contract with the SafeMath equivalent. For example:

  ```solidity
  balances[msg.sender] -= value;
  ```

  Becomes:

  ```solidity
  balances[msg.sender] = balances[msg.sender].sub(value);
  ```

5. Compile and deploy your contract. Attempt to transfer tokens from an account with a 0 balance of token to another account. Confirm in the terminal that an error message was produced.

You should now be safe from any integer underflows and overflows!

## Hints

* Remember to include the variable reassignments -- SafeMath will not mutate the variable it is operating on. You must reassign the variable using an equals sign (`=`).

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
