# lesson 13 follow-along
# lists: multiple values in an ordered sequence

spam = ['cat', 'bat', 'rat', 'bird']
print(spam)
print(spam[2]) #prints rat (first position is 0)

spam2 = [['rabbit', 'hare'], ['emu', 'ostrich']]
print(spam2) #all 4 items
print(spam2[1]) #second "item", which is the second list
print(spam2[1][0]) #emu

#negatives count from the end
print(spam[-1]) #prints bird

#slices capture, well... slices of a list.
print(spam[1:3]) #starts at position 1 and goes up to (but doesn't include) 3rd spot.

#replacing items in a list:
spam3 = [10, 20, 30, 40]
spam3[2] = 'hello'
print(spam3) #prints [10, 20, 'hello', 40]
#you can do the same with slices

#you can do slices on the ends like so:
spam4 = [5, 15, 25, 35, 45]
print(spam4[:2]) #prints 5, 15
print(spam4[2:]) #prints 25, 35, 45

#deleting:
del spam4[2] #cuts out 25 (3rd spot)
print(spam4)

#use of length in lists:
print(len(spam4)) #returns 4

#list replication:
print(spam4*3) #prints it 3 times

#treat string as a list:
print (list('Hello')) # prints each letter

#finding items in a list:
print(15 in spam4) #true
print(15 not in spam4) #false
