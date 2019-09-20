def problem17():
    print("Chuong trinh cho biet trong chuoi co bao nhieu chu hoa va bao nhieu chu thuong.")
    s = input("Moi nhap chuoi: ")
    C_UPPER = 0
    C_LOWER = 0
    for c in s:
        if c.isupper():
            C_UPPER += 1
        elif c.islower():
            C_LOWER += 1
        else:
            pass
    print("So chu cai viet hoa la: ", C_UPPER)
    print("So chu cai viet thuong la: ", C_LOWER)


problem17()
