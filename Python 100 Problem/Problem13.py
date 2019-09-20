def problem13():
    print("Chuong trinh chap nhan dau vao la mot chuoi cac tu tach biet boi khoang trang. Chuong trinh se loai bo cac tu trung lap, sap xep theo thu tu bang chu cai.")
    s = input("Moi nhap chuoi: ")
    stringSet = {word for word in s.split(" ")}
    print(sorted(stringSet))


problem13()
