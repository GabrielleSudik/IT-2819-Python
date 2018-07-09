#reading & writing files
#1. open the files
#2. read each line from the input file
#3. print each line to the command prompt
#4. and then write the line to the output file

#open file and print each line with a for loop:
with open('A06input.txt', 'r') as f:
    for line in f:
        print(line)

#create a new file:
with open('A06output.txt', 'w') as f:
    pass

#print stuff to new file
#name source file
with open('A06input.txt', 'r') as rf:
    #name destination file
    with open('A06output.txt', 'w') as wf:
        #write one line to tell readers what it is
        wf.write('This is the output text file.\n')
        #for loop to print each line in source file to output file
        for line in rf:
            wf.write(line)

tryingSomething = ['apple', 'banana', 'carrot']

with open('A06output.txt', 'a') as wf: #for append, so you don't overwrite
    for fruit in tryingSomething:
        wf.write(fruit)
        wf.write('\n')

#that also did a for loop to print stuff, but stuff created within the code
#instead of an outside file.
