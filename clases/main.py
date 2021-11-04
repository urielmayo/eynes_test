from math import pi
from turtle import Turtle

class Circle:
    def __init__(self, radius):
        try:
            if radius <= 0:
                raise ValueError("radius has to be greater than cero.")
        except ValueError as ve:
            print(f"ValueError: {ve}")
            exit()
        else:
            self.radius = radius
        
    def get_perimeter(self):
        """returns circle perimeter"""
        return pi*2*self.radius
    
    def get_area(self):
        """returns circle area"""
        return pi*(self.radius**2)
    
    def multiply_circle(self, n):
        """
        Generates a new circle which radius is self circle radius times parameter 'n'.
        'n' must be grater than zero. Otherwise the new circle won't be created
        """
        try:
            if n <= 0:
                raise ValueError("multplication times zero is not allowed")
        except ValueError as ve:
            print(f"ValueError in multiply_circle(): {ve}")
        else:
            return Circle(radius = self.radius * n)

    def set_radius(self,radius):
        try:
            if radius <= 0:
                raise ValueError("radius has to be greater than cero. Unable to modify variable")
        except ValueError as ve:
            print(f"ValueError in set_radius(): {ve}")
        else:
            self.radius = radius
    
    def __str__(self):
        t = Turtle()
        t.circle(radius = self.radius)
        return ""



if __name__=='__main__':
    circle = Circle(radius = 2)
    circle.set_radius(100)
    print(f"circle.get_perimeter()")
    print(circle)
    