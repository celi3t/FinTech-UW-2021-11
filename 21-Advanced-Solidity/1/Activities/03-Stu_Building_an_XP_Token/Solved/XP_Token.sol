pragma solidity ^0.5.0;

contract XP_Token {

    // Set the contract owner to msg.sender here (make sure it is a payable address)
    address payable owner = msg.sender;

    // Set the symbol of the token here (make sure to set the string as public)
    string public symbol = "XPT";

    // Set the exchange_rate for how many tokens to distribute per wei
    uint public exchange_rate = 100;

    // Set a mapping of address to uint called "balances"
    mapping(address => uint) balances;

    // Create a function called `balance` that is a `public view` that `returns(uint)`
    // This function should return the balance of msg.sender from the balances mapping
    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    // Create a `public` function named `transfer` that accepts `address recipient` and `uint value` as parameters
    // This function should subtract the value from msg.sender's balance then add value to the recipient's balance
    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }

    // Create a `public payable` function called `purchase`
    // This function will multiply the exchange rate by the msg.value, add the amount
    // to the msg.sender's balance, and transfer the msg.value to the owner address
    function purchase() public payable {
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    // Create a `public` function named `mint` that accepts `address recipient` and `uint value` as parameters
    // Require that the msg.sender is the owner and add the value to the recipient's balance
    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        balances[recipient] += value;
    }
}
