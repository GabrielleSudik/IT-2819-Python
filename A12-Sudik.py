# Assignment 12
# Gabrielle Sudik

# This is a guess the number game

#1) Implement an array to keep track of all the guesses that a user
#makes and list them prior to each subsequent guess, like this:
#Already guessed: 0 1 6 2 7
#2) Do some research and determine how to keep a line from
#automatically adding a carriage return/line feed after each print statement.


import random

print("Program Written by Gabrielle Sudik (with assistance from Matt Weisfeld).")

print ('Hello, what is your name?')
name = input()

print ('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)
#print ('secretNumber = ' + str(secretNumber))

numbersGuessed = []

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    numbersGuessed.append(guess)
    
    if guess < secretNumber:
        print ('Your guess is too low.')
        print ('So far you have guessed these numbers:', end = ' ')
        for numbers in numbersGuessed:
               print(numbers, end = ' ')
        print()
        
    elif guess > secretNumber:
        print ('Your guess is too high.')
        print ('So far you have guessed these numbers:', end = ' ')
        for numbers in numbersGuessed:
               print(numbers, end = ' ')
        print()
               
    else:
        break # this indicates a correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
