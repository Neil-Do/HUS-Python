import os

print("Bai 1: Chuong trinh thuc thi lenh cua he thong thong qua python.")
try:
    command = input('Nhap lenh: ').strip()
    os.system(command)
except:
    print("Loi thuc thi lenh")
finally:
    print("Ket thuc chuong trinh cua bai 1.")
