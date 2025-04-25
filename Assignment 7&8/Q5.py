import math

class Shape:
    def area(self):
        pass  

    def peri(self):
        pass 

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h 

    def peri(self):
        return 2 * (self.w + self.h)  

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r 

    def peri(self):
        return 2 * math.pi * self.r

r = Rectangle(10, 12)
c = Circle(5)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.peri())
print("Circle Area:", c.area())
print("Circle Perimeter:", c.peri())
