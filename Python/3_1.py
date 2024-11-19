#A) Write a python program to display following patterns:
#1 2 3 4 5 6 7
#1 2 3 4 5
#1 2 3
#1

def display_pattern():
   for i in range( 7, 0, -2):                                     #start from 7 and reduce by 2 after every row
      for j in range(1, i+1):	#print numbers from 1 to i
         print( j, end="")
      print()                                 #move to next line after each row
display_pattern()                          #call the function to display the pattern