#lesson 6 follow-along

#flow control: while loop

spam = 0
while spam <5:
    print('Hello, world!')
    spam = spam +1

#the "while" line checks for true/false of the statement
#while true, it will run the block
#so it stops when spam reachs 5

print()

name = ''
while name != 'your name':
    print('Please type your name:')
    name = input()
print('Thank you')
print()

#that loop doesn't have a counter
#but it still has a true/false check in the while line

#next is a bug example: an infinite loop:

#while True:
#    print('Hi!')

#you can escape those with ctrl-c

#another way:

name = ''
while True:
    print('Please type your name again:')
    name = input()
    if name == 'your name':
        break
print('Thank you.')
print()

#In that example, the true/false statement will always be true
#so we end the loop with the "break" statement

#continue statement:
#it skips the loop when a certain condition is met

spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3: #here's the condition. the block will skip using "continue"
        continue
    print('spam is ' + str(spam))
print('The end.')


