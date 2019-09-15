from random import randint



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

def smallestInRow(arr):
    # arr := square matrix
    arr_smallestInRow = []
    for r in range(len(arr)):
        smallest = arr[r][0]
        for e in arr[r]: #element in row r
            if e < smallest:
                smallest = e
        arr_smallestInRow.append(smallest)
    print("smallest in row: ")
    print(arr_smallestInRow)
    return arr_smallestInRow


def greatestInCol(arr):
    # arr := square matrix
    arr_greatestInCol = []
    for c in range(len(arr)):
        col_c = [row[c] for row in arr]
        greatest = col_c[0]
        for e in col_c: # element in col c
            if e > greatest:
                greatest = e
        arr_greatestInCol.append(greatest)
    print("greatest in column")
    print(arr_greatestInCol)
    return arr_greatestInCol


def matrixPrinter(mat):
    for r in mat:
        print(r)


def randomMatrix(r, c):
    rand_matrix = []
    for i in range(r):
        line = []
        for j in range(c):
            e = randint(0, 10)
            line.append(e)
        rand_matrix.append(line)
    matrixPrinter(rand_matrix)
    print()
    return rand_matrix


def randomSquareMatrix(n):
    return randomMatrix(n, n)


def bai6():
    mat = randomSquareMatrix(5)
    sml_arr = smallestInRow(mat)
    grt_arr = greatestInCol(mat)
    flag = False
    for c in range(len(grt_arr)):
        for r in range(len(sml_arr)):
            if grt_arr[c] == sml_arr[r]:
                print(r + 1, c + 1)
                flag = True
    if flag == False:
        print("Khong ton tai diem yen ngua.")


def congMaTran(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Ma tran khong cung kich thuoc, khong the cong.")
        return []

    result_matrix = []
    for r in range(len(a)):
        row_r = []
        for c in range(len(a[0])):
            row_r.append(a[r][c] + b[r][c])
        result_matrix.append(row_r)
    return result_matrix


def nhanMaTran(a, b):
    if len(a[0]) != len(b):
        print("So cot cua ma tran a khong bang so hang cua ma tran b. Khong the thuc hien phep nhan.")
        return []

    maTranTich = []
    for r in range(len(a)):
        hang = []
        for c in range(len(b[0])):
            rc_element = 0
            a_r = a[r]
            b_c = [row[c] for row in b]
            for i in range(len(a_r)):
                rc_element += a_r[i] * b_c[i]
            hang.append(rc_element)
        maTranTich.append(hang)
    return maTranTich


def bai7():
    a = randomMatrix(3, 4)
    b = randomMatrix(3, 4)
    c = randomMatrix(4, 2)

    sum_matrix = congMaTran(a, b)
    print("Tong cua 2 ma tran a va b la: ")
    matrixPrinter(sum_matrix)

    product_matrix = nhanMaTran(a, c)
    print("Tich cua 2 ma tran a va c la: ")
    matrixPrinter(product_matrix)


def getMatrixSize(n):
    matrixSizes = []
    for i in range(1, n + 1):
        if n % i == 0:
            matrixSizes.append([i, n // i])
    return matrixSizes

def createMatrix(matrixSize, matrixElements):
    # matrixSize := [r, c]
    e_index = 0
    mat = []
    for r in range(matrixSize[0]):
        mat_row_r = []
        for c in range(matrixSize[1]):
            mat_row_r.append(matrixElements[e_index])
            e_index += 1
        mat.append(mat_row_r)
    return mat


def bai8():
    print("Bai 8. Nhap vao so nguyen duong n va n so nguyen, in ra ma tran co kich thuoc khac nhau tu n so nguyen da nhap. Xin moi nhap vao so nguyen duong n.")
    n = int(input("n: "))
    while n < 1:
        print("N khong nguyen duong, xin moi nhap lai.")
        n = int(input("n: "))

    matrixElements = []
    for i in range(n):
        matrixElements.append(int(input("Nhap vao so nguyen thu " + str(i + 1) + ": ")))

    matrixSizes = getMatrixSize(n)
    for i in range(len(matrixSizes)):
        mat = createMatrix(matrixSizes[i], matrixElements)
        matrixPrinter(mat)


def magicSquareTest(mat):
    if len(mat) != len(mat[0]):
        print("Ma tran khong phai ma tran vuong, do do khong the la ma phuong.")
        return False

    Sum = sum(mat[0])

    # sum of element in row
    for r in mat:
        if sum(r) != Sum:
            return False

    # sum of element in column
    for c in range(len(mat)):
        col_c = [row[c] for row in mat]
        if sum(col_c) != Sum:
            return False

    # main diagonal
    sum_of_main_diagonal = 0
    for i in range(len(mat)):
        sum_of_main_diagonal += mat[i][i]
    if sum_of_main_diagonal != Sum:
        return False
    # end of main diagonal

    # antidiagonal

    # sum of row index and column index
    soi = len(mat) - 1
    sum_of_antidiagonal = 0
    for i in range(len(mat)):
        sum_of_antidiagonal += mat[i][soi - i]
    if sum_of_antidiagonal != Sum:
        return False
    # end of antidiagonal

    return True

def magicSquareTestPrint(mat):
    if magicSquareTest(mat):
        print("Ma tran vuong da cho la ma phuong.")
    else:
        print("Ma tran da cho khong phai la ma phuong.")


def bai9():
    magicSquare = [
        [2, 16, 13, 3],
        [11, 5, 8, 10],
        [7, 9, 12, 6],
        [14, 4, 1, 15]
    ]
    matrixPrinter(magicSquare)
    magicSquareTestPrint(magicSquare)
    print()

    mat = randomSquareMatrix(4)
    magicSquareTestPrint(mat)


def bai10():
    pass


if __name__ == "__main__":
    bai8()
