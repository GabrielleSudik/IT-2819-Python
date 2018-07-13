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
 
#your code:

class Triangle(Shape):

    def __init__(self):
        Shape.__init__(self,3)
        #another way to write that is with the built-in function super.
        #noted here for eduational purposes:
        #super().__init__(3)
        
    def findArea(self):
        a, b, c = self.sides
        semi = (a + b + c) / 2
        print('The semi-perimeter is ' +str(semi))
        area = (semi*(semi-a)*(semi-b)*(semi-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
    
#use 5,4,3 to understand the results
#remember w*h/2 = area
# ** is like sqrt
#Heron's Formula: sqrt[(semi*(semi-a)*(semi-b)*(semi-c))]
