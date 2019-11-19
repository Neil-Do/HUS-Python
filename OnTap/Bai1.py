l = []
for i in range(1100, 9091, 11):
    if i % 3 != 0:
        l.append(str(i))
print("; ".join(l))
