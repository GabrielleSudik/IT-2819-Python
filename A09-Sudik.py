#A09
#create a class Triangle that inherits from the professor's code and does
#findArea

class Shape:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
 
    def inputSides(self):
        self.sides = [float(input("Enter length of side "+str(i+1)+" : ")) for i in range(self.n)]
 
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
 
t = Shape(3)
t.inputSides()
t.dispSides()

#your code:

print('Now let\'s get the area of a triangle.')
class Triangle(Shape):
    def __init__(self):
        self.base = [float(input('What is the width of the triangle\'s base?'))]
        self.height = [float(input('What is the triangle\'s height?'))]

    def findArea(self):
        print('Let\'s multiple base and height to get the area.')
        self.area = (self.base*self.height)/2
        print('The area of your triangle is ', self.area)

    #def printArea(self.area):


t2 = Triangle()
t2.findArea()
#t2.printArea(self.area)
    
