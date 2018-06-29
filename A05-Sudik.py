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

temp = input("Input the (above zero) temperature you would like to convert (e.g., 45F, 102C etc.) : ")
degree_str = temp[:-1]
if degree_str.isdigit() == False:
    print('Your entry needs a positive integer followed by a single letter. You killed the program!!!!')
    exit()

degree = int(temp[:-1]) #all of the string except for its last character
input_type = temp[-1] #get the last character
print("You entered: ", temp)
print("The degree entry is: ", degree)
print("The degree type is: ", input_type)

input_type_ok = (input_type == 'c' or input_type == 'C' or input_type == 'f' or input_type == 'F')
#note you prefered to put those choices in the if statement, but it just wasn't working out :(
#it does work this way, but it's more code.

if input_type_ok != True:
    print("Next time, please specify C or F. Until then, I can't convert, and you'll get a nasty kill alert.")
    exit()
    
elif input_type == ('c' or 'C'):
    output_type = 'Fahrenheit'
    result = (float(degree)*9)/5 + 32
    
else:
    output_type = 'Celcius'
    result = (float(degree) - 32) * (5/9)
    
#uncomment the next line from the prof to print result:
print("The temperature in", output_type, "is", result, "degrees.")

#final note: the textbook says that "import sys" and later "sys.exit()" is what will make the program stop.
#but it doesn't work. plain old "exit()" does, or "quit()". without the import statement.
