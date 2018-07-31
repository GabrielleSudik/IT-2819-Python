#IT2819 Assignment 4
#The single line you will add will start like this: satisfactory =
#What you need to do is create a condition on the right hand side
#of the equation that implements the following constraints:
#1) The car must be a Ford
#2) The car must be a Mustang 
#3) The car must be of the model year 1965 OR 1966 
#4) The color of the car can NOT be “Yellow”

print ('Assignment 04 by Matt Weisfeld, with help from Gabrielle Sudik.')
#user input
#company = input("What is the requested car's company?")
company = "Ford"
print ("The requested company name is: " + company)

#model = input("What is the requested model?")
model = "Mustang"
print ("The requested model is: " + model)

year = input("What is the requested production year? ")
print ("The requested production year is: " + year)

color = input("What is the requested color? ")
print ("The requested color is: " + color)

#single line of code to be added here:

satisfactory = (company == 'Ford' and model == 'Mustang' and
                (year == '1965' or year == '1966') and color != 'yellow');


if satisfactory == True:
    print ("We have the requested car in stock")
else:
    print ("Unfortunately, we do not have the requested car in stock")
