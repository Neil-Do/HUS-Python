def f(n):
    try:
        if n == 0: return 0
        elif n == 1: return 1
        return f(n - 1) + f(n - 2)
    except:
        print("n khong phai so nguyen hoac nho hon 0.")



print("Chuong trinh de quy fibonacci, moi nhap n: ")
try:
    n = int(input())
    while n < 0:
        print("n can lon hon hoac bang 0, moi nhap lai.")
        n = int(input())
    fibList = [str(f(i)) for i in range(0, n + 1)]
    print(",".join(fibList))
except:
    print("Nhap n sai.")
