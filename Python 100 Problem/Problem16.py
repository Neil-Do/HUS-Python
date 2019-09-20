def problem16():
    print("Chuong trinh cho biet trong mot chuoi co bao nhieu chu cai va bao nhieu chu so.")
    s = input("Xin moi nhap chuoi: ")
    d = {"DIGITS" : 0, "LETTERS" : 0}
    for c in s:
        if c.isdigit():
            d["DIGITS"] += 1
        elif c.isalpha():
            d["LETTERS"] += 1
        else:
            pass
    print("So chu cai la ", d["LETTERS"])
    print("So chu so la ", d["DIGITS"])


problem16()
