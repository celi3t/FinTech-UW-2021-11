pragma solidity ^0.5.0;

/*
4. Use the `PersonalSavings.sol` file to update the `PersonalSavings` contract as follows:

    * Add an `if` statement to the `withdraw` function to validate if the `recipient` address parameter is equal to
      the `public_savings` or the `private_savings` addresses, and the balance of the contract is greater than or
      equal to the `amount` parameter; if so, call the `transfer` method of the `recipient` address.
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";

  function withdraw(uint amount, address payable recipient) public {
      recipient.transfer(amount);
  }

  function deposit() public payable {
  }

  function() external payable {
  }
}
