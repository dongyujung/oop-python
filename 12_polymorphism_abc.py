# Abstract base class

# Abstract base class, shape
# Will not have definition on its own
# Only contain methods

from abc import ABCMeta, abstractmethod


# Trying to make sure every shape has a method called area:
# Make use of abstract base class
class Shape(metaclass = ABCMeta):

    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print("Area of square: ", self.side * self.side)


class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        print("Area of rectangle: ", self.width * self.length)


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
# An abstract base class should not be able to instantiate an object for itself
shape = Shape()




