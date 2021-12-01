# Define a function "warble" that takes in a string as an argument, adds " arglebargle" to the end of it, and returns the result.
def warble(string_param):
    return(f"{string_param} arglebargle")

# Print the result of calling your "warble" function with the argument "hello".
print(warble("hello"))

# Define a function "wibble" that takes a string as an argument, prints the argument, prepends "wibbly " to the argument, and returns the result
def wibble(string_param):
    return(f"wibbly {string_param}")

# Print the result of calling your "wibble" function with the argument "bibbly"
print(wibble("bibbly"))

# Define a function "print_sum" that takes in two numbers as arguments and prints the sum of those two numbers.
def print_sum(num_1, num_2):
    sum = num_1 + num_2
    print(sum)

# Define a function "return_sum" that takes in two numbers as arguments and returns the sum of those two numbers
def return_sum(num_1, num_2):
    sum = num_1 + num_2
    return sum

# Define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers.
def triple_sum(num_1, num_2, num_3):
    sum = num_1 + num_2 + num_3
    return sum

"""
Define a function "dance_party" that takes in a string as an argument, 
then prints "dance!", then updates the string by calling "wibble" function 
with that argument, followed by "warble" function with that argument, 
then returns the updated stringdef dance_party(string_param):

""" 
def dance_party(string_param):
    print("dance!")
    print(string_param)
    print(wibble(warble(string_param)))

# Print the result of calling your "dance_party" function with your name as the argument
dance_party("Andrew")
