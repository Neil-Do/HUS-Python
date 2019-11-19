s = "0100,0011,1010,1001,0000,1111"
s_l = s.split(",")
result_l = []
for n in s_l:
    dec = int(n, 2)
    if dec % 5 == 0:
        result_l.append(n)
print(",".join(result_l))
