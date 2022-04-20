pragma solidity ^0.5.0;

contract XP_Token {
    // Set the contract owner to msg.sender here (make sure it is a payable address)

    // Set the symbol of the token here (make sure to set the string as public)

    // Set the exchange_rate for how many tokens to distribute per wei

    // Set a mapping of address to uint called "balances"

    // Create a function called `balance` that is a `public view` that `returns(uint)`
    // This function should return the balance of msg.sender from the balances mapping


    // Create a `public` function named `transfer` that accepts `address recipient` and `uint value` as parameters
    // This function should subtract the value from msg.sender's balance then add value to the recipient's balance


    // Create a `public payable` function called `purchase`
    // This function will multiply the exchange rate by the msg.value, add the amount
    // to the msg.sender's balance, and transfer the msg.value to the owner address


    // Create a `public` function named `mint` that accepts `address recipient` and `uint value` as parameters
    // Require that the msg.sender is the owner and add the value to the recipient's balance

}
