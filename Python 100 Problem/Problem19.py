def problem19():
    print("Chuong trinh loc cac so le tu danh sach cac songuyen, ngan cach nhau boi dau phay. Moi nhap vao danh sach: ")
    s = input("Danh sach so: ")
    n_list = [n for n in s.split(",") if int(n) % 2 != 0]
    print(",".join(n_list))


problem19()
