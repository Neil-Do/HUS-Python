def problem18():
    print("Chuong trinh tinh gia tri cua a + aa + aaa + aaaa.")
    a = int(input("Moi nhap vao so a nguyen: "))
    aa = int(str(a) + str(a))
    aaa = int(str(a) + str(a) + str(a))
    aaaa = int(str(a) + str(a) + str(a) + str(a))
    print(str(a + aa + aaa + aaaa))


problem18()
