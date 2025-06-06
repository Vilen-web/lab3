'''Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.'''

class klass:
    def getString(self):
        self.input_string = input()
    def printString(self):
        print(self.input_string.upper())
p1=klass()
p1.getString()
p1.printString()


'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.'''

class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2

shape = Shape()
print("Area of Shape:", shape.area())
n=int(input("Enter length: "))
square = Square(n)
print("Area of Square:", square.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
l=int(input("Enter length of Rectangle: "))
w=int(input("Enter width of Rectangle: "))
rectangle=Rectangle(l,w)
print("Area of Rectangle:", rectangle.area())

'''
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")
    def move(self, xmove, ymove):
        self.x += xmove
        self.y += ymove
    def dist(self, poind):
        return math.sqrt((self.x - poind.x) ** 2 + (self.y - poind.y) ** 2)

x1=int(input("Enter x coordinate of 1st point: "))
y1=int(input("Enter y coordinate of 1st point: "))
x2=int(input("Enter x coordinate of 2nd point: "))
y2=int(input("Enter y coordinate of 2nd point: "))
point1 = Point(x1,y1)
point2 = Point(x2,y2)

point1.show()
point2.show()

a=int(input("Enter the value of changing x coordinate: "))
b=int(input("Enter the value of changing y coordinate: "))
point1.move(a,b)
point1.show()

distance = point1.dist(point2)
print("Distance between two points:", distance)
