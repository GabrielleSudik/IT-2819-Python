#A10
#understanding scope
#- inside of outer_function() add another function called inner_function().
#Within inner_function() create a 3rd variable called 'a' and then set it to 30.
#Also within inner_function(), simply
#print the value of that 'a'.
#So, inner_function() will have 2 lines of code, creating a variable 'a=30'
#and then printing it.
#Finally, directly after the inner_function() body,
#call inner_function() from within outer_function().
#Output should be 30,20,10
#Once this is implemented, try experimenting with different scenarios
#and learn as much as you can about scope. 

#starter code, with my additions:
def outer_function():
    def inner_function():
        a = 30
        print('a =',a)
    inner_function()
    a = 20
    print('a =',a)

a = 10
outer_function()
print('a =',a)

#that prints 30,20,10

#now experiment:

def first_function():
    b = 2
    print('b =',b)
    def second_function():
        b = 3
        print('b =',b)
    second_function()
    b = 4
    print('b =',b)

b = 5
first_function()
print('b =',b)

#keep experimenting. see you lesson 10 notes.
