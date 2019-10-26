class Numbers:

    __MULTIPLIER = 9999

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def add(self):
        return self.__x + self.__y

    @classmethod
    def multiply(self, a):
        return a * Numbers.__MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.__x, self.__y)

    @value.setter
    def value(self, xy_tuple):
        self.__x, self.__y = xy_tuple

    @value.deleter
    def value(self):
        del self.__x
        del self.__y


a = Numbers(1, 2)
print(a.value)
a.value = 3, 4
print(a.value)

print(Numbers.subtract(1, 2))
del a.value
