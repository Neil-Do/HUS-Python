import re

def extractCompanyname():
    print("Enter Email: ")
    email = input()
    pattern = "(\w+\.*\w+)@(\w+\.*\w+)\.\w+"
    x = re.search(pattern, email)
    while x == None:
        print("Khong dung dinh dang email, xin moi nhap lai: ")
        email = input()
        x = re.search(pattern, email)
    companyname = re.match(pattern, email).group(2)
    print(companyname)


extractCompanyname()
