#What you need to do is create an if-elif-else statement that will do 3 things:
#1) Check if the user entered Celsius or Fahrenheit
#2) Accept either upper or lowercase designation values (i.e. c or C for Celsius)
#3) If the user did not enter Celsius or Fahrenheit, print an error message
#4) Convert to the alternate
#5) Print the value, specifying whether it is Celsius or Fahrenheit
#In my solution, the if-elif-else statement is eight lines long.
#You must include code to terminate the program when an error is detected.
#If you don’t handle this in the if-elif-else statement,
#the application will crash (research on the web to learn how)

#code supplied by professor:
temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1]) #all of the string except for its last character
input_type = temp[-1] #get the last character
print("You entered: ", temp)
print("The degree entry is: ", degree)
print("The degree type is: ", input_type)

# Add your code here:


#uncomment the next line to print result:
# print("The temperature in", output_type, "is", result, "degrees.
