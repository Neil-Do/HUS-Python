import re

def extractUsername():
    print("Enter Email: ")
    email = input()
    x = re.search("\w+\.*\w+@\w+\.*\w+\.\w+", email)
    while x == None:
        print("Khong dung dinh dang email, xin moi nhap lai: ")
        email = input()
        x = re.search("\w+\.*\w+@\w+\.*\w+\.\w+", email)
    username = email.split("@")[0]
    print(username)


extractUsername()
