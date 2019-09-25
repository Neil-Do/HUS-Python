class Rectangle():
    def __init__(self, edge1, edge2):
        self.edge1 = edge1
        self.edge2 = edge2

    def getArea(self):
        return self.edge1 * self.edge2


r1 = Rectangle(2, 5)
print(r1.getArea())
