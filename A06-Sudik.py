#wrap the code from A 05 inside a while loop and allow as many conversions
#as the user wants.
#Here are some points to add to the A 05 mix:
#1) Use a while loop so that the user can convert as many temperatures as they like.
#2) To exit the loop, the use can enter either a lower case ‘x’ or upper case ‘X’.
#3) If an error is detected, print an error message and loop again.

print("Welcome to the temperature converter.")
print("Press x at any time to quit.")
print()
temp = input("Input the temperature you would like to convert (e.g., 45F, 102C etc.) : ")

while True:

    degree_str = temp[:-1]

    if temp == 'x' or temp == 'X':
        print("Thanks for checking! The program will end.")
        exit()
    elif degree_str.isdigit() == False:
        print('Your entry needs a positive integer followed by a single letter. You killed the program!!!!')
        exit()
    else:
        degree = int(temp[:-1]) #all of the string except for its last character
        input_type = temp[-1] #get the last character
        print("You entered: ", temp)
        print("The degree entry is: ", degree)
        print("The degree type is: ", input_type)

    input_type_ok = (input_type == 'c' or input_type == 'C' or input_type == 'f' or input_type == 'F')

    if input_type_ok != True:
        print("Next time, please specify C or F. Try again.")
        print()
        temp = input("Input the next temperature you would like to convert (e.g., 45F, 102C etc.) : ")
        continue
     
    elif input_type == ('c' or 'C'):
        output_type = 'Fahrenheit'
        result = (float(degree)*9)/5 + 32
    
    else:
        output_type = 'Celcius'
        result = (float(degree) - 32) * (5/9)

    print("The temperature in", output_type, "is", result, "degrees.")
    print()
    temp = input("Input the next temperature you would like to convert (e.g., 45F, 102C etc.) : ")

