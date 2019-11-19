s = input("Nhap chuoi\n")
s_l = s.split(" ")
d = {}
for e in s_l:
    value = e + e[::-1]
    d[e] = value
print(d)
