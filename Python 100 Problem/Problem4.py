def createListAndTuple():
    print("Nhap vao mot chuoi so, phan tach voi nhau bang dau phay. Chuong trinh se tao ra mot list va mot tuple cac so.")
    s_input = input("Moi nhap chuoi so: ")
    n_list = [int(n) for n in s_input.split(",")]
    print(n_list)
    print(tuple(n_list))


createListAndTuple()
