# lesson 14 follow-along
# loops with lists and multiple assignments

#start with the for loop:
for i in range(4):
    print(i) #prints 0-3

#another way:
for i in [0,1,2,3]:
    print(i) #prints 0-3    

#so...
list1 = [0,1,2,3]
for i in list1:
    print(i) #prints 0-3 

#the list function can create a list for you, with help from range:
print(list(range(5))) #creates list of 1 - 4
print(list(range(0, 101, 5))) #creates list of 0 - 100 in increments of 5

#range(len) is useful when you also need an index number
supplies = ['pens', 'staplers', 'folders', 'notepads', 'pencils', 'desks']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#multiple assignments:
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(disposition)

#or all in one line:
size, color, disposition = 'thin', 'grey', 'sleepy'
print(color)

a = 'AAA'
b = 'BBB'
print(a) # prints AAA
a = b
print(a) # prints BBB

