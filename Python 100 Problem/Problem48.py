def filterCreateList():
    l = [i for i in range(1, 21)]
    l1 = list(filter(lambda x: x % 2 == 0, l))
    print(l1)


filterCreateList()
