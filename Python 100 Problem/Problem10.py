def print2DArray(arr2D):
    for r in arr2D:
        print(r)


def create2dArray():
    print("Chuong trinh tao mang 2 chieu, xin moi nhap vao kich thuoc cua mang 2 chieu: ")
    row_number = int(input("row: "))
    col_number = int(input("column: "))

    arr2D = []
    for r in range(row_number):
        arr_row = []
        for c in range(col_number):
            arr_row.append(r * c)
        arr2D.append(arr_row)
    print2DArray(arr2D)


create2dArray()
