#IT2819 Assignment 3
#Start with some provided code. Then:
#1)Capitalize the first letter of each name (basically the 1st character of each string).
#2)Create a 3rd string and concatenate the 2 strings to create a single name
#(with a space in between).


#code provided by professor:
#firstname=raw_input('Enter your first name : ')
#lastname=raw_input('Enter your last name : ')
#looks like raw_input doesn't exist in Python 3
firstname = input('Enter your first name : ')
lastname = input('Enter your last name: ')
firstname.capitalize()
lastname.capitalize()
print ("Hi. Your first name is %s" % firstname.capitalize());
print ("Your last name is %s" % lastname.capitalize());
fullname = (firstname.capitalize() + ' ' + lastname.capitalize())
print('And your full name is %s' % fullname)
print()

#trying another way:

firstname = input('Enter your first name : ')
lastname = input('Enter your last name: ')
capfirstname = firstname.capitalize()
caplastname = lastname.capitalize()
fullname = capfirstname + ' ' + caplastname
print('Hello, %s' % fullname)
print()

#and another:

firstname = input('Enter your first name : ')
lastname = input('Enter your last name: ')
fullname = firstname + ' ' + lastname
print('Hi there, %s' % fullname.title())
