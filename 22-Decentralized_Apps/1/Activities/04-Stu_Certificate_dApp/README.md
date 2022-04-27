## Certificate dAPP

In this short activity you will create a decentralized application for the certificate contract.

**Files**:

[app.py](./Unsolved/app.py)

[SAMPLE.env](./Unsolved/SAMPLE.env)

[certificate.sol](./Unsolved/contracts/certificate.sol)

[certificate_abi.json](./Unsolved/contracts/compiled/certificate_abi.json)

### Instructions

#### Step 1: Deploy the contract

* Deploy the [awardCertificate token](./Unsolved/contracts/certificate.sol) using Remix, MetaMask, and Ganache.

* Copy the `SAMPLE.env` file to a file called `.env` and update the file with the address of your deployed contract.

#### Step 2: Load the contract

The following should be completed in the "Contract Helper function" section of the `app.py` file.

* Load the Certificate token's compiled ABI JSON file.

* Set the contract's address by loading this value from the .env file with dotenv.

* Connect to the contract using web3.py.

#### Step 3: Complete the `Award Certificate` Section

The following should be completed in the "Award Certificate" section of the `app.py` file.

* Add the streamlit component needed to enter the certificate recipient's address.

* Add the streamlit component needed to enter a link for a certificate or a string of text for the certificate.

> **Hint** You can generate a fake certificate using a free online service and link to this certificate, or you can just accept a string of text here like: "FinTech Certificate of Completion".

* Use the web3 `contract.functions` object to perform a transaction on the `awardCertificate` contract function.

#### Step 4: Complete the `Display Certificate` Section

The following should be completed in the "Display Certificate" section of the `app.py` file.

* Use the web3 `contract.functions` object and the `certificate_id` to get the `ownerOf` the certificate.

* Use the web3 `contract.functions` object and the `certificate_id` to get the certificate's `tokenURI`.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
