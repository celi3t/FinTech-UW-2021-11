pragma solidity ^0.5.0;

/*
1. Use the `TradeController.sol` file to create a contract named `TradeController` that contains:

    * An unsigned integer variable `previous_price`.

    * A string variable `trade_type`.

2. Add a public function named `makeTrade` to the `LatestTrade` contract as follows:

    * Define an unsigned integer `current_price` as the unique function's parameter.

    * Into the body of the function, use an `if` statement to check if the input parameter `current_price` is
      less than the contract variable `current_price`, if so, set the `trade_type` string variable as "Buy"
      and set the `previous_price` to the `current_price`.

3. Modify the `makeTrade` function of the `LatestTrade` contract as follows.

    * Add a boolean variable `buy_anyway` as the second parameter.

    * Use an `OR ( || )` clause within the `if` statement to check if it's true that the `current_price` is
      less than the `previous_price` or if `buy_anyway` is true.

    * Add an `else if` statement to check if the `current_price` is greater than the `previous_price`. If it is,
      set the `trade_type` to "Sell" and the `previous_price` equal to the `current_price`.

    * Add an `Else` statement to set the `trade_type` to "Hold" in case the previous conditions were false.
*/


contract TradeController {
  uint previous_price;
  string trade_type;

  function makeTrade(uint current_price, bool buy_anyway) public {
    if (current_price < previous_price || buy_anyway) {
      trade_type = "Buy";
      previous_price = current_price;
    } else if (current_price > previous_price) {
      trade_type = "Sell";
      previous_price = current_price;
    } else {
      trade_type = "Hold";
    }
  }
}
