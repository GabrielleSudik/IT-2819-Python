# lesson 12 follow-along
# random number game

import random

print('Hello, what is your name?')
name = input()

print(name + ', I am thinking of a number between 1 and 20 (inclusive).')
secretNumber = random.randint(1,20)

print('DEBUG: the secret number is ' + str(secretNumber))
# tip: adding a line of code like that is good for troubleshooting while you write
# you then code out or delete when the program is correct.

# for loop starts at 1, ends at 7. ie, 6 guesses, starting with actual 1st guess
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input()) #remember input returns a string, need to convert to int

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this is for the correct guess

if guess == secretNumber:
    print('That is the number! You guessed it right in ' + str(guessesTaken) + ' guesses.')
else:
    print('Sorry, I was thinking of ' +str(secretNumber) + '.')
