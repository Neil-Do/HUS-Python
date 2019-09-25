print("Chuong trinh cho biet so cac chu cai, so cac chu so hoac so cac ky tu khac trong chuoi duoc cho. Moi nhap chuoi:")
s = input().strip()
digit = 0
alpha = 0
other = 0
for c in s:
    if c.isdigit():
        digit += 1
    elif c.isalpha():
        alpha += 1
    else:
        other += 1
print("So chu cai: ", alpha)
print("So chu so: ", digit)
print("So ky tu khac: ", other)
