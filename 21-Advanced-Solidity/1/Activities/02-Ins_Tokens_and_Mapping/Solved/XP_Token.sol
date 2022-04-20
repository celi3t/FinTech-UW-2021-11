pragma solidity ^0.5.0;

contract XP_Token {
    // Establish the contract variables owner, symbol, and exchange rate
    address payable owner = msg.sender;
    string public symbol = "XPT";
    uint public exchange_rate = 100;

    // Map the address to the unit for the account balance
    mapping(address => uint) balances;

    // Create a function that accesses an account's balance
    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    // Create a function that transfers tokens between users
    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }

    // Create a function that allows uers to purchase tokens
    function purchase() public payable {
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    // Create a funciton that mints new tokens
    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        balances[recipient] += value;
    }
}
