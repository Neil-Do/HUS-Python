def problem15():
    print("Chuong trinh in ra cac so trong doan [1000, 3000] co tat ca cac chu so deu la so chan.")
    n_arr = []
    n = ["2"]
    for i in range(0, 9, 2):
        n.append(str(i))
        for j in range(0, 9, 2):
            n.append(str(j))
            for k in range(0, 9, 2):
                n.append(str(k))
                n_arr.append("".join(n))
                n.pop()
            n.pop()
        n.pop()
    print(",".join(n_arr))


problem15()
