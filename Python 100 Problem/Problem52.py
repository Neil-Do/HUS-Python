import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2


cr1 = Circle(5)
print(cr1.getArea())
