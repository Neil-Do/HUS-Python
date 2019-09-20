def problem14():
    print("Chuong trinh nhan dau vao la cac chuoi nhi phan 4 chu so, phan cach boi dau phay. Chuong trinh se loc va in ra cac so nhi phan chia het cho 5.")
    s = input("Moi nhap chuoi: ")
    div_5 = {"0000", "1010", "0101", "1111"}
    result = [n for n in s.split(",") if n in div_5]
    print(','.join(result))


problem14()
