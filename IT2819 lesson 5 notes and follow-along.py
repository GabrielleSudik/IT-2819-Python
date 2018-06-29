#lesson 5 follow-along
#flow control

name = 'Alice'
if name == 'Alice':
    print('Hello, Alice.')
print('Done.')

#above, if the condition in the if statement is true
#it will print what follows the :
#otherwise it skips the indented stuff
#indentation is required: it tells Python what is inside the block

name = 'Bob'
if name == 'Alice':
    print('Hello, Alice.')
print('Done.')

#fyi condition means the same as expression

password = 'swordfish'
if password == 'swordfish':
    print('access granted')
else:
    print('access denied')
print()

password = 'carp'
if password == 'swordfish':
    print('access granted')
else:
    print('access denied')  
print()

#else-if is "elif"
#it does the first true thing
#will skip all remaining, even if some are true

name = 'Eli'
age = 3500
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('You are an immortal vampire')
elif age > 100:
    print('You are not Alice, Granny.')
print()

#truthy and falsey: basically means one of several things or any thing is true
#but the absense of something is false.
#like: enter a name. any name will be true. but left blank will be false.
#with bools, a zero is the same as false. any other number is true.

print(bool(2))
print(bool(0))
print(bool(-4))



    
        
    
