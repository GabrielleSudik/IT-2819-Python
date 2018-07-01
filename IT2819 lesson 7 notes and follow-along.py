#lesson 7 follow-along
#for loop

print('My name is')
for i in range(5):
    print("Jimmy Five Times " + str(i))
print()

# range starts at 0, runs 5 times.

# find the sum of all numbers 0 - 100:
total = 0
for num in range(101):
    total = total + num
print(total)

# for loop is like a while loop, but more concise
# you don't have to initialize "i" or "num"
# and you don't have to increment

# you can make the range start at not-zero.
# here, 8 is where we start. it stops *as if* it ran 16 times
# ie, it stops at 15 (because it "started" at 0)
print('My name is')
for i in range(8, 16):
    print("Jimmy Five Times " + str(i))
print()

# you can also increase by steps: The 2 increments by 2.
print('My name is')
for i in range(8, 16, 2):
    print("Jimmy Five Times " + str(i))
print()

# and you can go backwards:
print('My name is')
for i in range(5, -1, -1):
    print("Jimmy Five Times " + str(i))
print()

# you can use break or continue in for loops
