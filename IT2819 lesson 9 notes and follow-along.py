# lesson 9 follow-along
# functions, none, keyword arguments

#functions are mini programs within programs
#functions group code that will be called multiple times
#avoid duplicating code

#here's the syntax:
def hello():
    print('Hi')
    print('Howdy')
    print('Hello, there.')

#here's how you call it (this will run 3 times)
hello()
hello()
hello()

print()

#parameter -- the thing that accepts an argument
def hello2(name):
    print('Hello, ' + name)

#arguments: the variables that get passed to the funtion
hello2('Alice')
hello2('Mad Hatter')

print()

#you can have functions in functions
#example breaks down into more fundamental pieces
print('Hey-hey has ' + str(len('hey-hey')) + ' characters in it.')
print('Hey-hey has ' + str(7) + ' characters in it.')
print('Hey-hey has ' + '7' + ' characters in it.')

print()

#functions can return values:
def plusOne(number):
    return number + 1

plusOne(5)
plusOne(8)
#those won't print anything because plusOne doesn't print anything.
#instead:
newNumber = plusOne(5)
print(newNumber)
newNumber = plusOne(8)
print(newNumber)
print()

#None value (ie, no value is returned)
#example: print() returns nothing. In this case, None is built in.
#None indicates lack of a value.

spam = print()
spam
print('It printed a blank line')

#keyword arguments. optional parameters that change what happens to a function
print('Hello', end=' ')
print('World.')

print('cat','dog','mouse')
print('cat','dog','mouse', sep='&')
#note end and sep are keyword arguments for print.
#presumably, other functions have different keyword arguments.
