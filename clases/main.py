from math import pi

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
        return pi*2*self.radius
    
    def get_area(self):
        return pi*(self.radius**2)
    
    def multiply_circle(self, n):
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


if __name__=='__main__':
    circle = Circle(radius = 2)
    circle.set_radius(20)
    print(f"circle.get_perimeter()")
    biger_circle = circle.multiply_circle(n = -2)
    print(biger_circle.get_area())
    