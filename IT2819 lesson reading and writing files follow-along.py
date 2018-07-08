# Random tutorial about reading and writing text files.
# Watched for assignment 10.
# Start with a txt file created in the same folder as this py file.

# this next thing is a context manager. it's considered best practice.
# it will close things when you're done.
with open('LessonText.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    # .readline and readlines do variations of how it prints to screen

    print(f.read) #prints status of file

with open('LessonText.txt', 'r') as f:
    for line in f:
        print(line, end=' and ')
        #that iterates each line, and adds your "end" to it too.
        #but not necessarily in the way you'd expect to see it.

with open('LessonText.txt', 'r') as f:
    f_contents = f.read(10) #prints first 10 characters of f
    print(f_contents)
    f_contents = f.read(10) #prints next 10 characters of f
    print(f_contents)

print()

#way when you don't know length of doc:
with open('LessonText.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
    

#old way of doing it:
fi = open('LessonText.txt', 'r')
# r means we can read. w means write. r+ means read and write.

print()
print(fi.name)
print(fi.mode) # prints how we are viewing it (r)

fi.close()
# if you don't close the file, you can get leaks then errors.

# there are more methods under read. Like "tell" says where you are.

# writing!
# careful you don't overwrite a file you don't mean to.

# to create a new file:
with open('LessonText2.txt', 'w') as f:
    pass

# to write something to it:
with open('LessonText2.txt', 'w') as f:
    f.write('Test text')

# fyi here's an example of a more robust IDE being useful.
# you can keep check the text files within the IDE's tabs

with open('LessonText2.txt', 'w') as f:
    f.write('Second line')
    f.write('Third line')

# If you ran those last two blocks, you'll see that the second block overwrote the first
# multiple write lines in the same block will just keep printing

# copying a file:
with open('LessonText.txt', 'r') as rf:
    with open('LessonTextCopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            
# copying a picture file:
with open('Gabrielle.png', 'rb') as rf:
    with open('GabrielleCopy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)

# or:
with open('Gabrielle.png', 'rb') as rf:
    with open('GabrielleSecondCopy.png', 'wb') as wf:
        chunk_size = 128 # that number denotes size of chunk. could be different.
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
