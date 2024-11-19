#2.	Write a python program that prints number from 1 to n. Accept the value of n from the user. However,  for the multiples of 3, print “Fizz” instead of the number and for the multiples of 5, print “Buzz”. For the numbers which are multiples of both 3 and 5, print “FizzBuzz”. But if a number is a prime number, print “Prime” instead of the number, even if it satisfies the “Fizz”, “Buzz” or “FizzBuzz” conditions.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fizzbuzz_with_prime(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print("Prime")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Accept value of n from the user
n = int(input("Enter the value of n: "))
fizzbuzz_with_prime(n)
