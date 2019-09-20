class Car:
    # dinh nghia lop
    name = "Car"

    def __init__(self, name = None):
        self.name = name


car1 = Car("BMW X6")
print("%s name is %s" % (Car.name, car1.name))

car2 = Car()
car2.name = "Madza CX-5"
print("%s name is %s" % (Car.name, car2.name))
