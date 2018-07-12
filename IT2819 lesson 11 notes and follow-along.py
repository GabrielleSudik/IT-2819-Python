# lesson 11 follow-along
# exception handling
# try and except statments

#let's try dividing by zero
#without the try/except code, when you try to pass 0 as an argument
#you get a runtime error of "ZeroDivisionError"

def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error. You tried to divide by zero. SHAME.')

#See how the except line is for ZeroDivisionError?
#That's the error message Python gives
#So we use that same error name to name our except line

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

#How about needed user input to be a specific type?
#We want an int below, but a user might type a word.

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) > 4:
        print('Cat lady! Even if you are not a lady!')
    else:
        print('That is a reasonable number of cats.')
except ValueError:
    print('I need an integer, no letters please.')

#Like above, ValueError is the message we get if we don't handle the error

#With all these try/except handling, the program still won't work.
#But it's cleaner and nicer for the user. No walls of unreadable red text.
