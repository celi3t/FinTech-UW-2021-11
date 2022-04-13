# Travel Expenses Contract

## Background

You work for a FinTech company that offers accounting services to small and medium businesses. The first service your company launched is a travel expenses application that keeps track of any expense using a smart contract.

In this activity, you will practice variable declarations, and basic math and assignation operations in Solidity by creating a travel expenses smart contract. You will complete the code for the `TravelExpenses` contract and it's `RecordExpense` function.

## Instructions

Open [Remix](http://remix.ethereum.org/), import the starter file and perform the following code drills. Once you finish, compile the file to ensure the code works.

1. Create a public payable address variable named `corporate_account` and assign a valid Ethereum address to it.

2. Create a payable address variable named `personal_account` and assign a valid Ethereum address to it

3. Define and assign a string variable named `employee_name` that has your name.

4. Create a constant `256 bit` unsigned integer `daily_expenses_eth` with an initial value of `1`.

5. Create a `256 bit` unsigned integer named `current_expenses_wei` with an initial value of `0`.

6. Create an unsigned integer `current_taxes_wei` with an initial value of `0`.

7. Create a `16 bit` unsigned integer `expenses_count` and assign a value of `0`.

8. Create an unsigned `32 bit` integer `eth_usd_rate` and assign the current value in USD of `1 ETH` to it.

9. Create a `256` unsigned integer constant `eth_wei_rate` and assign the number of Wei in one Ether.

10. Create a new public unsigned `256 bit` integer variable named `daily_expenses_wei` and assign the value of `daily_expenses_eth` plus `eth_wei_rate`.

11. Create an unsigned `256 bit` integer `expense_usd_no_tax` and assign the value of the `new_net_expense_usd` minus taxes.

12. Create an unsigned `256 bit` integer `taxes_usd` and assign the taxes in USD from `new_net_expense_usd`.

13. Update the `current_expenses_wei` by adding the `expense_usd_no_tax` converted to Wei.

14. Update the `current_taxes_wei` by adding the `taxes_usd` converted to Wei.

15. Increase `expenses_count` in one unit.

---
© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
