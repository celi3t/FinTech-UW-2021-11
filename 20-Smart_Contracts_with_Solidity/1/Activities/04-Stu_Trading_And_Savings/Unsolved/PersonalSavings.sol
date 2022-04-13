pragma solidity ^0.5.0;

/*
4. Modify the `personal_savings.sol` starter file as follows:

    * Define a public function `withdraw` with two input parameters. An unsigned integer `amount`,
      and a payable address `recipient`.

    * In the body of the `withdraw` function, set a return value the result of the `transfer` function on the
      `recipient` address using the parametrized `amount`.

    * Add a public payable function `deposit`.

    * Add a payable fallback function.
*/

contract PersonalSavings {
  address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  string account_holder = "Jane Doe";
}
