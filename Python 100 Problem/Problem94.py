print("Chuong trinh dem va in do ky tu cua chuoi do nguoi dung nhap vao. Xin moi nhap chuoi: ")
s = input()
charDict = {}
for e in s:
    if e not in charDict:
        charDict[e] = 1
    else:
        charDict[e] += 1
print(charDict)
