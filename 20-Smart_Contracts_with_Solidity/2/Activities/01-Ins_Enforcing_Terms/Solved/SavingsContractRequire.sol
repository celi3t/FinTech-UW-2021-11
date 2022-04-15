pragma solidity ^0.5.0;

contract SavingsContract {
    // Define an address and uint public object
    address authRecipient = 0x9e53c0DcC0fBf2ff8E26B9789A50CFf8e08348f2;
    uint public balance = 10;

    // Create a withdrawal function using a require statement
    function withdraw(uint amount, address payable recipient) public {
        require (recipient == authRecipient && amount < balance, "You are not authorized to withdraw Ether from this contract!");
        recipient.transfer(amount);
        balance = address(this).balance;
    }

    // Create a deposit function
    function deposit() public payable {
        balance = address(this).balance;
    }

    // Create the fallback function
    function() external payable {}
}
