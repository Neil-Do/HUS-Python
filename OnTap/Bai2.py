d = {}
n = int(input("Nhap n\n"))
for i in range(1, n + 1):
    i_str = str(i * i)
    d[i] = int(i_str[::-1])
print(d)
