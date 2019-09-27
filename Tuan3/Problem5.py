def createRecord(s):
    name, score = s.split(",")
    name = name.split(" ")
    firstname = name[-1]
    name.pop()
    lastname = " ".join(name)
    return (firstname, lastname, float(score), )


def prob5(list_s):
    list_record = []
    for s in list_s:
        list_record.append(createRecord(s))

    print("Sap xep theo ten, ho")
    list_record.sort()
    for e in list_record:
        print(e)
    print("\n\n")
    list_record.sort(key = lambda tup: tup[2])
    print("Sap xep theo diem: ")
    for e in list_record:
        print(e)


ls = [
    "Do Tat Thanh, 10",
    "Pham Thi Thu Thao, 9",
    "Nguyen Dinh Bao, 8",
    "Nguyen Thi Kim Ngan, 7",
    "Nguyen Quynh Trang, 6",
    "Dinh Quynh Khanh, 5",
    "Truong Thi Trang, 4"
]
prob5(ls)
