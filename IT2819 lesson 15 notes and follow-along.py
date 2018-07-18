# lesson 15 follow-along
# methods and list methods
# like a function but called on a certain value

spam = ['hello', 'hi', 'howdy', 'hey']
print(spam.index('hello')) #prints 0
print(spam.index('hey')) #prints 3
#index is the method. it's called on the value spam.

spam = ['cat', 'dog', 'bat']
spam.append('bird') #adds bird on end
print(spam)
spam.insert(1, 'pig') #inserts pig in index space 1
print(spam)
spam.remove('dog')
print(spam)

#methods are limited to certain kinds of values.
#example: lists use append and insert and remove
#but strings or numbers, etc have different methods

spam.sort()
print(spam) #puts them in alpha order

spam = [2, 8, 3.14, 9, -1]
spam.sort() #puts them in numerical order
print(spam) 

spam = ['Z', 'A', 'w', 'b']
spam.sort() #first by capitalized, then alphabetical
print(spam)

#so...
spam.sort(key=str.lower) #treats them as all lower, then sorts, then prints alpha
    #note that keeps actual capitalization within the string
print(spam)
