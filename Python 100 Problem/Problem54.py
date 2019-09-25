class Shape():
    def getArea(self):
        return 0


class Square(Shape):
    def __init__(self, edge):
        self.edge = edge

    def getArea(self):
        return self.edge ** 2


s1 = Square(4)
print(s1.getArea())
