#4.	Write a python program that defines a function to calculate the factorial of a number. Print the result in a user-friendly format. Ask the user to input a string. Implement error handling to manage invalid inputs (e.g., negative numbers or non-integer values)
def factorial(n):
    # Check if the input is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1  # Base case: 0! = 1 and 1! = 1
    else:
        return n*factorial(n-1)

# Ask the user to input a number
user_input = input("Please enter a non-negative integer: ")

# Validate the input
try:
    number = int(user_input)
    # Call the function and get the result
    fact = factorial(number)
    print(f'The factorial of {number} is {fact}.')
except ValueError:
    print("Invalid input! Please enter a valid non-negative integer.")
