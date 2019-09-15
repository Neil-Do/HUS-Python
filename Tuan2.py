def inputBai1():
    print("Bai 1. Nhap vao mot day n so nguyen, viet ham kiem tra tinh chat cua day. Xin moi nhap so cac so nguyen n:")
    n = 0
    while(n < 1):
        print("So cac phan tu n can la so duong.")
        n = int(input("Nhap n: "))

    number_array = []
    for i in range(1, n + 1):
        t_number = int(input("Nhap so thu " + str(i) + ": "))
        number_array.append(t_number)
    return number_array


def dayDanDau(number_array):
    for i in range(1, len(number_array)):
        if number_array[i - 1] * number_array[i] > 0:
            return False
    return True


def dayTang(n_arr):
    for i in range(1, len(n_arr)):
        if n_arr[i - 1] > n_arr[i]:
            return False
    return True


def capSoCong(n_arr):
    if len(n_arr) == 1 or len(n_arr) == 2:
        return True

    c = n_arr[1] - n_arr[0]
    for i in range(2, len(n_arr)):
        if n_arr[i - 1] + c != n_arr[i]:
            return False
    return True


def capSoNhan(n_arr):
    if len(n_arr) == 1 or len(n_arr) == 2:
        return True

    q = n_arr[1] / n_arr[0]
    for i in range(2, len(n_arr)):
        if n_arr[i - 1] * q != n_arr[i]:
            return False
    return True


def bai1():
    number_array = inputBai1()
    if len(number_array) <= 50:
        print("Day so la: ", number_array)
        print("Day so co: ", len(number_array))

    if dayDanDau(number_array):
        print("Day la day dan dau.")
    else:
        print("Day khong phai la day dan dau.")

    if dayTang(number_array):
        print("Day la day tang (a[i - 1] <= a[i]).")
    else:
        print("Day khong phai la day tang.")

    if capSoCong(number_array):
        print("Day la day cap so cong.")
    else:
        print("Day khong phai la day cap so cong.")

    if capSoNhan(number_array):
        print("Day la day cap so nhan.")
    else:
        print("Day khong phai la day cap so nhan.")


def testBai1():
    pass


def gcd(a, b):

    flag = False
    if a < 0 and b < 0:
        flag = True
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        t = a
        a = b
        b = t

    while b != 0:
        r = a % b
        a = b
        b = r

    if flag:
        a = -a
    return a


def lcm(a, b):
    _gcd = gcd(a, b)
    return (a * b) / _gcd


def bai2():
    print("Bai 2: Tim UCLN, BCNN cua tu so va mau so cua phan so da cho, sau do toi gian phan so do. Nhap tu so va mau so, chu y tu so va mau so can la so nguyen: ")
    a = int(input("Nhap tu so: "))
    b = int(input("Nhap mau so: "))
    _gcd = gcd(a, b)
    _lcm = lcm(a, b)
    a = a / _gcd
    b = b / _gcd
    print("UCLN cua tu so va mau so la: ", _gcd)
    print("BCNN cua tu so va mau so la: ", _lcm)
    print("Phan so toi gian la: ", a, " / ", b)


def inputBai3():
    print("Bai 3. In ra tam giac PASCAL kich thuoc m. Xin moi nhap vao gia tri cua m nguyen duong ")
    m = int(input("m: "))
    while m < 0:
        print("M can la so nguyen duong. Xin moi nhap lai: ")
        m = int(input("m: "))
    return m


def veTamGiacPASCAL(m):
    if m < 0:
        print("m < 0. m can la so nguyen duong.")
    else:
        arr = [1]
        line_i = 0
        print(line_i, "\t", arr)
        while line_i < m:
            line_i += 1
            arr.append(1)
            for i in range(2, line_i + 1):
                arr[-i] += arr[-i - 1]
            print(line_i, "\t", arr)



def bai3():
    m = inputBai3()
    veTamGiacPASCAL(m)


def inputBai4():
    print("Bai 4. Tao character histogram cho xau s.")
    s = input("Xin moi nhap xau s: ")
    return s


def stringHistogram(s):
    s = s.lower()
    c_dict = {}
    for c in s:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1

    for key in c_dict:
        print(key, "\t", c_dict[key])


def bai4():
    s = inputBai4()
    stringHistogram(s)


def bai5():
    pass

from random import randint
def 
def bai6():



def bai7():
    pass


def bai8():
    pass


def bai9():
    pass


def bai10():
    pass


if __name__ == "__main__":
    bai4()
