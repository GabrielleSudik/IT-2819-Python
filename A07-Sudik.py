# Assignment 07 - for loops
# Your mission is to use a for loop to check to see if the number entered
# by the use is actually a prime number.

import math

print("Assignment 07 - written by Gabrielle Sudik")
# get user input
num = input("Enter a number: ")
while num.upper()!= "X":
 # check to make sure we have an integer, if not, quit
 if num.isdigit() != True:
     print("A number greater than 1 must be entered. Goodbye!")
     quit()
 # convert the imput string to an integer
 numInt = int(num)
 # prime numbers are greater than 1
 if numInt > 1:
     print("Check for factors.")
     # code for prime number generation goes here:
     start = 2
     if numInt == 2:
         print(numInt, "is a prime number.")
     if numInt > 2:
         for i in range(start, numInt):
             if numInt % i == 0:
                print(numInt, "is not a prime number.")
                break
             else:
                print(numInt, "is a prime number.")
                start = numInt+1
                break

 # if input number is less than
 # or equal to 1, it is not prime
 else:
     print(numInt, "is not a prime number.")
 # get user input
 num = input("Enter another number: ")
print("Goodbye!")

