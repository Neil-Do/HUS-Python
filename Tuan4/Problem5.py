print("Bai 5. Chuong trinh xu ly ngoai le neu nguoi dung nhap sai. Xin moi nhap vao mot so nguyen: ")
n = 0
while True:
    try:
        n = int(input("Enter an integer: \n"))
        break
    except:
        print("Nhap sai dinh dang, xin moi nhap lai.")
print("So nguyen la: " + str(n))
