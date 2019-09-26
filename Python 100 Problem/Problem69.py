def solve1(n):
    gen = (str(i) for i in range(0, n + 1) if i % 35 == 0)
    s = ",".join(gen)
    print(s)


def generator(n):
    for i in range(0, n + 1):
        if i % 35 == 0:
            yield i


def solve2(n):
    l = [str(i) for i in generator(n)]
    print(",".join(l))


try:
    print("Chuong trinh tao ra generator cac so nguyen duong chia het cho 5 va 7 trong doan [0, n]. Xin moi nhap vao n nguyen duong: ")
    n = int(input())
    while n < 0:
        print("n < 0, moi nhap lai: ")
        n = int(input())
    solve2(n)
except:
    print("Loi nhap lieu.")
