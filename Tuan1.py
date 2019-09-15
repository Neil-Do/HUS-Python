import math
import bisect
import random as rd

def bai1():
    print("Bai 1, giai phuong trinh bac 2 ax^2 + bx + c = 0. Moi nhap vao 3 gia tri a, b, c.")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))

    if a == 0:
        if b == 0 and c != 0:
            print("Phuong trinh vo nghiem.")
        elif b == 0 and c == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh co nghiem x = ", c/b)
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("Phuong trinh vo nghiem.")
        elif delta == 0:
            delta_sqrt = math.sqrt(delta)
            print("Phuong trinh co nghiem kep: ", (-b - delta_sqrt)/(2 * a))
        else:
            delta_sqrt = math.sqrt(delta)
            print("Phuong trinh co 2 nghiem phan biet")
            print("x1 = ", (-b - delta_sqrt)/(2 * a))
            print("x2 = ", (-b + delta_sqrt)/(2 * a))


def laTamGiac(a, b, c):
    if(a > b + c or b > a + c or c > a + b):
        return False
    return True


def chuViTamGiac(a, b, c):
    return a + b + c


def dienTichTamGiac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def bai2():
    print("Bai 2, xac dinh 3 gia tri a, b, c co phai la 3 canh cua tam giac hay khong. Neu co thi tinh chu vi, dien tich. Moi nhap vao bo 3 canh a, b, c:")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))

    if laTamGiac(a, b, c):
        print("a, b, c la 3 canh cua 1 tam giac.")
        print("Chu vi cua tam giac la: ", chuViTamGiac(a, b, c))
        print("Dien tich cua tam giac la: ", dienTichTamGiac(a, b, c))
    else:
        print("a, b, c khong phai la 3 canh cua tam giac.")

def gocPhanTu(x, y):
    if x == 0 and y == 0:
        print("Diem da cho la goc toa do.")
    elif x == 0:
        print("Diem da cho nam tren truc hoanh.")
    elif y == 0:
        print("Diem da cho nam tren truc tung.")
    else:
        if x > 0 and y > 0:
            print("Diem da cho thuoc goc phan tu thu nhat.")
        elif x < 0 and y > 0:
            print("Diem da cho thuoc goc phan tu thu 2.")
        elif x < 0 and y < 0:
            print("Diem da cho thuoc goc phan tu thu 3.")
        else:
            print("Diem da cho thuoc goc phan tu thu 4.")


def bai3():
    print("Bai 3, tim goc phan tu cua diem da cho. Moi nhap 2 toa do x, y.")
    x = float(input("Nhap vao gia tri x = "))
    y = float(input("Nhap vao gia tri y = "))
    gocPhanTu(x, y)


def bai4():
    print("Bai 4, chuong trinh in ra cac so chinh phuong nho hon hoac bang n. Moi nhap n: ")
    n = int(input("n:"))

    i = 0
    while(i ** 2 < n):
        print(i ** 2)
        i += 1


def giaiThuaKep(n):
    if n < 1: return 0
    ketQua = 1

    i = 0
    if n % 2 == 0:
        i = 2
    else:
        i = 1

    while i <= n:
        ketQua = ketQua * i
        i = i + 2
    return ketQua


def bai5():
    print("Bai 5, tinh giai thua kep n!!. Nhap n:")
    n = int(input())

    ketQua = giaiThuaKep(n)
    print("Ket qua la: ", ketQua)


# Bai 6 sai, can xem lai
def bai6():
    print("Bai 6, viet chuong trinh tinh sin(x) theo khai trien Taylor. Nhap x va so nguyen n lon hon 0:")
    x = float(input("x:"))
    n = int(input("n:"))

    ketQua = 0
    i = 0
    while(i <= n):
        ketQua += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        i += 1
    print("Ket qua la: ", ketQua)


def bai8():
    print("Bai 8, chuyen so nguyen duong n thanh dang nhi phan. Nhap n:")
    n = int(input("n: "))
    while n < 1:
        print("n khong phai la so nguyen duong, xin moi nhap lai:")
        n = int(input("n: "))

    list_of_binary = []
    while n != 0:
        list_of_binary.append(n % 2)
        n //= 2

    list_of_binary.reverse()
    binary_string = "".join(str(e) for e in list_of_binary)
    print("Dang nhi phan cua n la: ", binary_string)


def bai9():
    print("Bai 9, Nhap so nguyen duong n, liet ke cac so nguyen a, b, c trong doan [1, n] de bo 3 (a, b, c) lap thanh 1 bo Pitago.")
    n = int(input("Nhap n: "))
    while n < 1:
        print("n khong phai la so nguyen duong, xin moi nhap lai:")
        n = int(input("n: "))

    # Tao mang binh phuong cac so tu 1 den n
    element_square = [i**2 for i in range(1, n + 1)]
    print(element_square)


    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_square_hat = element_square[a - 1] + element_square[b - 1]
            c= bisect.bisect(element_square, c_square_hat)

            if c**2 == c_square_hat:
                print(a, b, c)


# function for testing bisect lib
def test_bisect():
    arr = [i**2 for i in range(1, 8)]
    print(arr)
    print(bisect.bisect(arr, 35))


def bai10Input():
    print(
    "Bai 10, giai he phuong trinh bac nhat 3 an 2 phuong trinh: \n" \
    "x + y + z = e\n" \
    "ax + by + cz = d\n" \
    "Moi nhap 5 so nguyen duong a, b, c, d, e de giai: "
    )

    coefficient_name = ["a", "b", "c", "d", "e"]
    coefficient_value = []

    for i in range(5):
        coeff = int(input("Nhap {}: ".format(coefficient_name[i])))
        while coeff < 0:
            print("{} khong phai la so nguyen duong, xin moi nhap lai: ".format(coefficient_name[i]))
            coeff = int(input("{}: ".format(coefficient_name[i])))
        coefficient_value.append(coeff)

    return coefficient_value


def bai10():
    coefficient_value = bai10Input()
    a_subtract_c = coefficient_value[0] - coefficient_value[2]
    b_subtract_c = coefficient_value[1] - coefficient_value[2]
    d_subtract_ce = coefficient_value[3] - coefficient_value[2] * coefficient_value[4]
    e = coefficient_value[4]

    for x in range(e + 1):
        for y in range(e - x + 1):
            if a_subtract_c * x + b_subtract_c * y == d_subtract_ce:
                print(x, y, e - x - y)


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):

    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n])


def isSuperPrime(n):
    if not is_prime(n):
        return False
    while n != 0:
        n //= 10
        print(n)
        if is_prime(n):
            return True
    return False


def primalityTest(n):
    k = 30
    for i in range(k):
        a = rd.randrange(n - 1) + 1
        print(a)
        if a**(n - 1) % n != 1:
            return False
    return True


def superPrime():
    primalityTest(29)


if __name__ == "__main__":
    _known_primes = [2, 3]
    _known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
    print(isSuperPrime(4547337172376300111955330758342147474062293202868155909489))
