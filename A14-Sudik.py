# Programming Courses Game
# by Gabrielle Sudik

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
    print ("You need to memorize their course numbers by playing the game.")
    print ("I'll provide the names of the courses, then you guess the number.")
    print ("And so you don't go nuts, here are the numbers (in random order):\n")
    print ("IT 2670, IT 1025, IT 2800, IT 2650, IT 1050\n")

    for key in courses.keys():
        guess = input('What is the course number for ' + key + '? ')
        if guess == courses[key]:
            print('That is correct!')
            correct = correct+1
        else:
            print('Sorry, that is wrong.')
            incorrect = incorrect+1
            print('That course number is ' + courses[key] + '.')

	    
    # Display correct and incorrect answers
    print ("You missed ",incorrect," courses.")
    print ("You got ",correct," courses correct.\n")
    if correct == 5:
        print("Great job, you guessed all the courses correctly!")

# Entry Point
response=""
while (response!="n"):
    main()
    response=input("\n\nPlay again?(y/n)\n# ")




    
