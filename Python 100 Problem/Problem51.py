class Vietnam():
    @staticmethod
    def printNationality():
        print("Vietnam.")


class Hanoi(Vietnam):
    @staticmethod
    def printProvince():
        print("Hanoi Capital.")


print(Hanoi.__base__)
