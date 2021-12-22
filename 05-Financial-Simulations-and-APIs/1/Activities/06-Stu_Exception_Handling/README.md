# Exception Handling

In this activity, you will be provided with a list of cryptocurrencies, only some of which are valid. Your task is to make a request for each coin and, if it's a valid coin, append the JSON data to a list of valid coins. If it's not a valid coin, append the name of the coin to a list of invalid coins. 

## Instructions

1. Import the required libraries and dependencies. 

2. Use the [Free Crypto API](https://alternative.me/crypto/api/) ticker endpoint.

3. Use `coin_list` for a list of currency names. (There are too many coins to manually sort through.) Iterate over each coin name in the list, passing in the coin name for each API call.

4. Loop over the coin list. Be sure to do the following: 

    - Check each coin in `coin_list`.
    
    - Using `url` and the coin name, make a `get` request to the API using [`request.get`](https://requests.readthedocs.io/en/master/user/quickstart/#response-content).
    
    - Check if the response is valid.
    
    - Catch any server errors and print the trace.
    
    - Append the valid coin names' JSON data to the `valid_coins` list.
    
    - Append the invalid coin names to the `invalid_coins` list.

5. Print the results. 

>**Hint**: Are there any errors in the `response` metadata? You may need to check the JSON file to determine where the error is being handled. 
---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
