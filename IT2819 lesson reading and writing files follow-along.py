# Random tutorial about reading and writing text files.
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
    

#old way of doing it:
fi = open('LessonText.txt', 'r')
# r means we can read. w means write. r+ means read and write.

print(fi.name)
print(fi.mode) # prints how we are viewing it (r)

fi.close()
# if you don't close the file, you can get leaks then errors.

