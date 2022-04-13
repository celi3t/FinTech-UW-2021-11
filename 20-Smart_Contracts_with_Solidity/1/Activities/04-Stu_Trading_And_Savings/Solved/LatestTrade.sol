pragma solidity ^0.5.0;

/*
1. Use the `latest_trade.sol` file to create a contract named `LatestTrade` that contains:

    * A string variable `coin` with the value `XRP` assigned to it.

    * An unsigned integer variable `price`.

    * A boolean variable `is_buy_order`.

2. Add a function named `updateTrade` to the `LatestTrade` contract as follows:

    * Define a in-memory string variable `new_coin` as the first parameter.

    * Define an unsigned integer variable `new_price` as the second parameter.

    * Define a boolean variable `is_buy` as the third parameter.

    * Into the body of the function, set the contract variables `coin`, `price`, and `is_buy_order` to the inputs of
      the `updateTrade` function. This function will update the contract variables via the `updateTrade` function.

3. Add a public getter function `getTrade` and public function `setTrade` to the `LatestTrade` contract as follows.

    * The `getTrade` function should return the `coin`, `price`, and `is_buy_order` variables of the `LatestTrade`
      contract.

    * The `setTrade` function should set the `coin`, `price`, and `is_buy_order` variables with the values of the
      input parameters `new_coin`, `new_price`, and `is_buy`.
*/

contract LatestTrade {

  string coin = "XRP";
  uint price;
  bool is_buy_order;


  function updateTrade(string memory new_coin, uint new_price, bool is_buy) public {
    coin = new_coin;
    price = new_price;
    is_buy_order = is_buy;
  }

  function getTrade() public returns (string memory, uint, bool) {
    return (coin, price, is_buy_order);
  }

  function setTrade(string memory new_coin, uint new_price, bool is_buy) public {
    coin = new_coin;
    price = new_price;
    is_buy_order = is_buy;
  }
}
