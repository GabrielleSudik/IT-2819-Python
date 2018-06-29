#This program will say hello and ask my name.

print('Hello world.')
print('What is your name?')
myName = input()
print('Hello ' + myName)
print('The length of your name is: ')
print(len(myName))
print('How old are you?')
myAge = input()
print('In one year, you will be ' + str(int(myAge) + 1) + '.')

#python reads all input as a string by default
#to make it something else, you do this for example: int(myAge)
#in that last line, we first made myAge and int to add 1
#then made that result a string(int(myAge)+1) to make it a string

print('What is the name of your pet?')
      
petName = input()
print('Hello, ' + petName)
petNameLength = len(petName)
print('That name is ' + str(petNameLength) + ' letters long.')
