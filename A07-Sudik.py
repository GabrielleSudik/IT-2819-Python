# Assignment 07 - for loops
# Your mission is to use a for loop to check to see if the number entered
# by the use is actually a prime number.

print("Assignment 07 - written by Gabrielle Sudik")
# get user input
num = input("Enter a number: ")
while num.upper()!= "X":
 # check to make sure we have an integer, if not, quit
 if num.isdigit() != True:
 print("A number must be entered.")
 quit()
 # convert the imput string to an integer
 numInt = int(num)
 # prime numbers are greater than 1
 if numInt > 1:
 print("Check for factors.")
 # code for prime number generation goes here:

 # if input number is less than
 # or equal to 1, it is not prime
 else:
 print(numInt,"is not a prime number")
 # get user input
 num = input("Enter a number: ")
print("Goodbye!")
