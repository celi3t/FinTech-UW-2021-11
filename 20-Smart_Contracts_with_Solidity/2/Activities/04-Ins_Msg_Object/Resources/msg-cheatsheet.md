# The `msg` Object Attributes Cheatsheet

The `msg` object represents the transaction call, originated by an ethereum address, or the message call, originated by a contract's address, that triggers a contract execution.

This object contains the following special attributes which allow access to the blockchain.

* `msg.sender`: Represents the ethereum address that initiated the contract call. It can be an ethereum address or a contract's address.

* `msg.value`: Represents the value of Ether that is sent in the transaction (expressed in Wei).

* `msg.data`: Represents the data payload of the call into our contract (expressed in bytes).

* `msg.sig`: Represents the first four bytes of the data payload.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
