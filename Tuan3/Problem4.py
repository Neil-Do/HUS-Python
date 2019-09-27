import re

def validatePassword():
    print("Chuong trinh kiem tra tinh hop le cua mat khau. Moi nhap vao mat khau: ")
    s = input()

    lower_pattern = "[a-z]"
    upper_pattern = "[A-Z]"
    specialChar = "[~!@#$%^&*]"
    validate_flag = True
    if len(s) < 8 or len(s) > 100:
        print("Do dai khong hop le. Do dai mat khau can tu 8 - 100 ky tu.")
        validate_flag = False
    if re.search(lower_pattern, s) is None:
        print("Chuoi khong chua chu cai thuong.")
        validate_flag = False
    if re.search(upper_pattern, s) is None:
        validate_flag = False
        print("Chuoi khong chua chu cai in hoa.")
    if re.search(specialChar, s) is None:
        validate_flag = False
        print("Chuoi khong chua ky tu dac biet ~!@#$%^&*.")
    if re.search(r"\d", s) is None:
        validate_flag = False
        print("Chuoi khong chua chu so.")
    if validate_flag:
        print("Mat khau hop le.")


validatePassword()
