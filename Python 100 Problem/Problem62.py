
try:
    print("Nhap chuoi: ")
    s = input()
    us = s.encode()
    print(us)
except  UnicodeDecodeError:
    print("Loi khong chuyen duoc chuoi sang dinh dang UTF8.")
except:
    print("Loi trong nhap xau.")
finally:
    print("Ket thuc Problem 62.")
