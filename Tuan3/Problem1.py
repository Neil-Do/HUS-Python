def inputData():
    print("Xin moi nhap vao day cac so nguyen, xuong dong sau khi nhap xong moi so. De ket thuc nhap, vui long de trong dong cuoi cung. ")
    # data = [ [even_number_list], [odd_number_list] ]
    data = [[], []]
    s = input("Nhap so: \n")
    try:
        while s != "":
            if int(s) % 2 == 0:
                data[0].append(int(s))
            else:
                data[1].append(int(s))
            s = input()
    except:
        print("Loi nhap du lieu khong hop le.")
    data[0].sort()
    data[1].sort(reverse=True)
    print()
    result = zip(data[0], data[1])
    for i in result:
        print(i)


inputData()
