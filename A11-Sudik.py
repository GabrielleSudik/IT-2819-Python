# Assignment 11
# Gabrielle Sudik
# Assignment 11 is meant to demonstrate your understanding of Python exceptions
# as well as test your understanding of nested if-statements.
#1) Use exception handling to make sure that the program does not crash
#if the user enters some bad input. Make sure (and this is important),
#that the program does not just
#terminate, it must ask the user to reenter a valid format.
#2) As another temperature, format (Kelvin). Thus, if I enter the number 100C,
#then the program must calculate both the Fahrenheit and
#the Kelvin equivalent (you need to research all the formulas).


print("Program Written by Matt Weisfeld and Gabrielle Sudik")

while True:

    temp = input("Input the temperature you would like to convert. (e.g., 45F, 102C, 1000K)\n" +
                   "Pressing X will end the program: ")

    if temp[-1].upper() == "X":
        break;
        
    try:
        degree = int(temp[:-1]) #all of the string except for its last character
        input_type = temp[-1] #get the last character

        print("You entered: ", degree, input_type.upper())
        
        if input_type.upper() == "C":

            result = int(round((9 * degree) / 5 + 32))
            output_type = "Fahrenheit"
            print("The temperature in", output_type, "is", result, "degrees.")
            result = int(degree + 273)
            output_type = "Kelvin"
            print("The temperature in", output_type, "is", result, "degrees.")
            if (result <= 0):
                print("That is below absolute zero, and is impossible! Oops!")

        elif input_type.upper() == "F":

            result = int(round((degree - 32) * 5 / 9))
            output_type = "Celsius"
            print("The temperature in", output_type, "is", result, "degrees.")
            #K = 5/9 (° F - 32) + 273
            result = int(round(((degree - 32) * 5 / 9) + 273))
            output_type = "Kelvin"
            print("The temperature in", output_type, "is", result, "degrees.")
            if (result <= 0):
                print("That is below absolute zero, and is impossible! Oops!")

        elif input_type.upper() == "K":

            result = int(round(degree) - 273)
            output_type = "Celcius"
            print("The temperature in", output_type, "is", result, "degrees.")
            # (K - 273.15)* 1.8000 + 32.00
            result = int(round((degree - 273)*1.8 + 32))
            output_type = "Fahrenheit"
            print("The temperature in", output_type, "is", result, "degrees.")
            if (degree < 0):
                print("That is below absolute zero, and is impossible! Oops!")


        else:
            print("Sorry, you need to specify C or F.")

    except ValueError:
        print("Sorry, you need to enter an integer followed by C or F.")
                
    except NameError:
        print("Sorry, you need to enter an integer followed by C or F.")    

print("Goodbye!")
