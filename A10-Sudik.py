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
    print('b =',b) #2
    def second_function():
        b = 3
        print('b =',b) #3
    second_function()
    b = 4
    print('b =',b) #4

def third_function():
    b = 7
    print('b =',b) #7

def fourth_function():    
    global b
    b = 8
    print('b =',b)

b = 5
print('b =',b) #5 (global)
first_function() #2,3 (local)
print('b =',b) #5 (global)
b = 6
print('b =',b) #6 (global)
third_function() #7 (local)
print('b =',b) #6 (global)
fourth_function() #8 (global, assigned in local)
print('b =',b) #8 global (set in fourth_function)

