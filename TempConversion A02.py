#IT2819 Assignment 2
# 1)Prompt the user and accept a temperature value in Celsius from the command prompt.
# 2)Convert this Celsius value to a Fahrenheit value (make sure you have 2 variables)
# 3)Print the resultant value, with a label, to the command prompt

print('Hello, non-American.')
print('Let me help you convert Celcius to Fahrenheit.')
print('What is the temperature today in Celcius?')
celcius = input() #gets user input
#user input is already a string
print(celcius + ' Celcius, eh? In Fahrenheit, that is...')
#change string to decimal using float(celcius) to do math
fahr = (float(celcius)*9)/5 + 32
#convert float to string for printing:
print(str(fahr) + ' degrees! Welcome to Cleveland.')
