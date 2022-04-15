pragma solidity ^0.5.0;

contract MsgTest {
    // Define public variables for uint balance, address msgSender, and uint msgValue.
    uint public balance = 0;
    address public msgSender;
    uint public msgValue;

    // Define a public payable function that sets the balance, msgSender, and msgValue.
    function deposit() public payable {
        balance = address(this).balance;
        msgSender = msg.sender;
        msgValue = msg.value;
    }
}
