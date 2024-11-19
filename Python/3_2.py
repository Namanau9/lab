#B) Write a python program to accept a number from the user and check whether the number is an Armstrong Number or not. A number is said to be Armstrong if the sum of the cubes of its digits is equal to the original number.

def is_armstrongno(x):
   original_no = x
   sum_of_cubes = 0

   while x>0:
      digit = x%10
      sum_of_cubes += digit **3
      x=x//10
   return sum_of_cubes == original_no

def recur():
     for i in range(1,10):
         num = int(input("Enter a number :"))
         if is_armstrongno(num):
             print(f"{num} is an Armstrong number:")
         else:
             print(f"{num} is not an Armstrong number:")

recur()
        