// Travel Expenses Contract

pragma solidity ^0.5.0;

// This is a comment - any code commented is not executed -

/*
This is a multi-line comment.
You can comment out many lines at once.
For the most part, you will see single-line comments, but it is good to understand multi-line comments as well.

As in single-line comments, any code contained within multi-line comments is not executed.
*/

contract TravelExpenses {
  // 1. Create a public payable address variable named `corporate_account` and assign a valid Ethereum address to it.
  address payable public corporate_account = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;

  // 2. Create payable address variable named `personal_account` and assign a valid Ethereum address to it
  address payable personal_account = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;

  // 3. Define and assign a string variable named "employee_name` that has your name.
  string employee_name = "John Doe";

  // 4. Create a constant `256 bit` unsigned integer `daily_expenses_eth` with an initial value of `1`.
  uint256 constant daily_expenses_eth = 1;

  // 5. Create a `256 bit` unsigned integer named `current_expenses_wei` with an initial value of `0`.
  uint256 current_expenses_wei = 0;

  // 6. Create an unsigned integer `current_taxes_wei` with an initial value of `0`.
  uint current_taxes_wei = 0;

  // 7. Create a `16 bit` unsigned integer `expenses_count` and assign a value of `0`.
  uint16 expenses_count = 0;

  // 8. Create an unsigned `32 bit` integer `eth_usd_rate` and assign the current value in USD of `1 ETH` to it.
  uint32 eth_usd_rate = 143;

  // 9. Create a `256` unsigned integer constant `eth_wei_rate` and assign the number of Wei in one Ether.
  uint256 constant eth_wei_rate = 1000000000000000000;

  // 10. Create a new public unsigned `256 bit` integer variable named `daily_expenses_wei` and assign the value of
  //    `daily_expenses_eth` plus `eth_wei_rate`.
  uint256 public daily_expenses_wei = daily_expenses_eth * eth_wei_rate;

  function RecordExpense(uint32 new_net_expense_usd, uint tax_rate) public {
    // 11. Create an unsigned `256 bit` integer `expense_usd_no_tax` and assign the value of the `new_net_expense_usd`
    //    minus taxes.
    uint256 expense_usd_no_tax = new_net_expense_usd - new_net_expense_usd * tax_rate / 100;

    // 12. Create an unsigned `256 bit` integer `taxes_usd` and assign the taxes in USD from `new_net_expense_usd`.
    uint256 taxes_usd = new_net_expense_usd * tax_rate / 100;

    // 13. Update the `current_expenses_wei` by adding the `expense_usd_no_tax` converted to Wei.
    current_expenses_wei += expense_usd_no_tax * eth_wei_rate / eth_usd_rate;

    // 14. Update the `current_taxes_wei` by adding the `taxes_usd` converted to Wei.
    current_taxes_wei = taxes_usd * eth_wei_rate / eth_usd_rate;

    // 15. Increase `expenses_count` in one unit.
    expenses_count += 1;
  }
}
