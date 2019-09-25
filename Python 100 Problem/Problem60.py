import re

def findStringCreateByNumber():
    print("Nhap vao chuoi tu: ")
    s = input()
    stringList = s.split(" ")
    pattern = "\d+"
    r1 = [e for e in stringList if re.match(pattern, e)]
    print(r1)


findStringCreateByNumber()
