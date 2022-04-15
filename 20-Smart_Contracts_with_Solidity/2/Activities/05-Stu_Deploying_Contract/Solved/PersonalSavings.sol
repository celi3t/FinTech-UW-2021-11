pragma solidity ^0.5.0;

/*
1. Modify the `PersonalSavings` contract to initialize the following variables:

    * An address variable `last_to_withdraw`.

    * A unsigned integer variable `last_withdraw_amount`.

    * An address variable `last_to_deposit`.

    * A unsigned integer variable `last_deposit_amount`.

    * A public unsigned integer variable `balance`.

2. Modify the `withdraw` function in the `PersonalSavings` contract as follows:

    * Replace the `if` statement for two `require` function calls as follows.

      * The first `require` function call should check if the recipient address is the public or private savings address. If the function returns false, the error message `This is not your account` will be risen.

      * The second `require` function call should check if there is enough Ether in the contract balance to commit the withdrawal operation. If the function returns false, the error message `You don't have enough funds!` will be risen.

    * Use an `if` statement to check if the `last_to_withdraw` is NOT equal to `recipient`, if so set `last_to_withdraw` equal to `recipient`.

    * Set `last_withdraw_amount` equal to the `amount` parameter.

    * Update the `balance` variable to the current contract balance minus the amount that was withdrawn.

3. Modify the `deposit` function in the `PersonalSavings` contract as follows:

    * Use an `if` statement to check if the `last_to_deposit` is NOT equal to `msg.sender`, if so set `last_to_deposit` equal to `msg.sender`.

    * Set `last_deposit_amount` equal to the `msg.value` variable.

    * Set `balance` equal to the current contract.

4. Compile the contract and fix any bugs that arise.

5. After a successfully compilation, deploy the contract on the JavaScript VM provide by the Remix IDE.

6. Test the contract's functions as follows:

    * Deposit 10 Ether to the contract.

    * Use the `balance` getter function to corroborate that the current balance of the contract is 10 Ether (10000000000000000000 Wei).

    * Use the `withdraw` function to transfer 1 Ether to the private savings address. Recall that transfers should be expresses in Wei.

    * Use the `balance` getter function to corroborate that the current balance of the contract is 9 Ether (9000000000000000000 Wei).

    * Use the `withdraw` function to transfer 1 Ether to the following address: `0xd83F8A76e7F699669Fe85C5Da2F7f09907A15a53`. Since this is not a valid address, check to make sure that the error defined in the require function was triggered.

    * Use the `withdraw` function to transfer 15 Ether to the public savings address. Since you know there are not enough funds in the contract, check to make sure that the error defined in the `require` function was triggered.
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";
  uint public balance;

  address last_to_withdraw;
  uint last_withdraw_amount;

  address last_to_deposit;
  uint last_deposit_amount;

  function withdraw(uint amount, address payable recipient) public {
    require(recipient == public_savings || recipient == private_savings, "This is not your account");
    require(address(this).balance >= amount, "You don't have enough funds!");
    if (last_to_withdraw != recipient) {
      last_to_withdraw = recipient;
    }
    last_withdraw_amount = amount;
    balance = address(this).balance - amount;

    return msg.sender.transfer(amount);
  }

  function deposit() public payable {
    if (last_to_deposit != msg.sender) {
      last_to_deposit = msg.sender;
    }

    last_deposit_amount = msg.value;
    balance = address(this).balance;
  }

  function() external payable {
  }
}
