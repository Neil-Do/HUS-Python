def wordSort():
    print("Chuong trinh giup sap xep theo thu tu mot chuoi cac tu. Xin moi nhap vao chuoi tu, cac tu ngan cach nhau boi dau phay (',').")
    s = input("Nhap chuoi tu: ")
    word_list = s.split(',')
    word_list.sort()
    print(','.join(word_list))


wordSort()
