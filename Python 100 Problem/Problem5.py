class InOutString():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Nhap chuoi: ")
    def printString(self):
        print(self.s.upper())


strObj = InOutString()
strObj.getString()
strObj.printString()
