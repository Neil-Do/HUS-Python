def solve1(n):
    gen = (str(i) for i in range(0, n + 1) if i % 2 == 0)
    s = ",".join(gen)
    print(s)


def EvenGenerator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def solve2(n):
    l = [str(i) for i in EvenGenerator(n)]
    print(",".join(l))


try:
    print("Chuong trinh tao ra generator cac so nguyen duong chan tu trong doan [0, n]. Xin moi nhap vao n nguyen duong: ")
    n = int(input())
    while n < 0:
        print("n < 0, moi nhap lai: ")
        n = int(input())
    solve2(n)
except:
    print("Loi nhap lieu.")
