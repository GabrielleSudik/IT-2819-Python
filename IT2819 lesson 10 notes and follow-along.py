# lesson 10 follow-along
# global and local scope

spam = 42 #global scope. forgotten when the program ends.

def eggs():
    spam = 43 #local scope.
    #local variables are forgotten when function returns its value.

print('Some code')
print('Some more code')

# code in global scope can't use local variables.
# code in local can use global variables.
# one local scope variable can't be used in a different local scope.
# the same name can represent different variables if in different scopes.

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam() #returns "eggs" which is 99 in spam.
       #even though eggs was 0 within bacon, that variable was forgotten
       #when we left the bacon function

def spam():
    #eggs = 30
    print(eggs)

eggs = 40
spam()  #returns 40 because spam uses a global variable.
        #if you uncode the eggs inside of spam(), you'll get 30 instead.

#can you assign a global variable within a local scope? yes"
def spam():
    global eggs
    eggs = 20
    print(eggs)

eggs = 50
spam() #prints 20, which is from eggs inside spam
print(eggs) #prints 20 because you re-assigned global eggs to 20 within spam
            #even though you declared eggs was 50 in the global scope
            #and spam reassigned eggs AFTER you assigned the global as 50
eggs = 60
print(eggs) #prints 60, because it was once again reassigned globally.
