def passwordCheck(pwd):
    if len(pwd) < 6 or len(pwd) > 12:
        return False
    specialChar = {"$", "#", "@"}
    isContainLower = False
    isContainUpper  = False
    isContainNumber = False
    isContainSpecialChar = False
    for c in pwd:
        if c.islower():
            isContainLower = True
        elif c.isupper():
            isContainUpper = True
        elif c.isdigit():
            isContainNumber = True
        elif c in specialChar:
            isContainSpecialChar = True
    return isContainLower and isContainUpper and isContainNumber and isContainSpecialChar


def problem21():
    print("Chuong trinh kiem tra tinh hop le cua mat khau. Moi nhap vao chuoi cac mat khau, cac mat khau phan cach boi dau phay: ")
    sArray = input().split(",")
    pArray = []

    for s in sArray:
        if passwordCheck(s):
            pArray.append(s)
    print(",".join(pArray))


problem21()
