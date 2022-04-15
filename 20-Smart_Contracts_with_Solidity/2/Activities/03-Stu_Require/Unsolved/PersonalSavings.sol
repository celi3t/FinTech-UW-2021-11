pragma solidity ^0.5.0;

/*
1. Instead of the `if` statement, use a `require` statement to validate that the `recipient` address is either
  the `public_savings` or the `private_savings` address.

2. In the case of an error, show the following message: "This is not your account."

3. Instead of the `if` statement to validate the contract balance, use a `require` statement.

4. In the case of an error, show the following message: "You don't have enough funds!".
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";

  function withdraw(uint amount, address payable recipient) public {
    if ((recipient == public_savings || recipient == private_savings) && (address(this).balance >= amount)) {
      recipient.transfer(amount);
    }
  }

  function deposit() public payable {
  }

  function() external payable {
  }
}
