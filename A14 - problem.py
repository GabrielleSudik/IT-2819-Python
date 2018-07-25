# Programming Courses Game

# Mainline



def main():
    courses={"Computer Concepts":"IT 1025",\
        "Programming Logic":"IT 1050",\
        "Java Programming":"IT 2670",\
        "C++ Programming":"IT 2650",\
        "Python Programming":"IT 2800"}

    print ("Learn your programming courses!\n")

    correct=0
    incorrect=0
  
    # Game Loop

    print ("Here's how it works: There are 5 IT courses at Tri-C.")
    print ("You need to learn and then memorize their course numbers.")
    print ("I'll provide the names of the courses, then you guess the number.")
    print ("Hint: they are in format \'IT ####\'.")
    print ("AND so you don't go nuts, they are (in random order):")
    for course in courses.keys():
        print(courses[course])
    


    print(courses['Computer Concepts'])
    print(courses.keys())
    print(courses.values())

    for course in courses.keys():
        guess = input('What is the course number for ' + course + '?')
        if guess == courses[key]:
            print('That is correct!')
            correct = correct+1
        else:
            print('Sorry, that is wrong.')
            incorrect = incorrect+1
            print('That course number is ' + courses[key] + '.')

	    
    # Display correct and incorrect answers
    print ("You missed ",incorrect," courses.")
    print ("You got ",correct," courses.\n")

# Entry Point
response=""
while (response!="n"):
    main()
    response=input("\n\nPlay again?(y/n)\n# ")




    
