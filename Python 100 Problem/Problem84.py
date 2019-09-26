S = ["Anh","Em"]
V = ["Chơi","Yêu"]
O =  ["Bóng đá","Xếp hình"]

def solve1():
    result = []
    for es in S:
        result.append(es)
        for ev in V:
            result.append(ev)
            for eo in O:
                result.append(eo)
                print(" ".join(result))
                result.pop()
                result.pop()
                result.pop()


def solve2():
    # Code by Quantrimang.com
    for i in range(len(S)):
        for j in range(len(V)):
            for k in range(len(O)):
                cau = "%s %s %s." % (S[i], V[j], O[k])
                print (cau)
