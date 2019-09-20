class xSquare():
    def __init__(self):
        x = 0
    def squareNumber(self):
        print("Chuong trinh tinh gia tri binh phuong cua 1 so, xin moi nhap vao mot so nguyen: ")
        x = int(input("x: "))
        print(x ** 2)


obj = xSquare()
obj.squareNumber()
