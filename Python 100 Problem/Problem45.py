def filtList():
    l = [i for i in range(1, 11)]
    l2 = list(filter(lambda x: x % 2 == 0, l))
    print(l2)


filtList()
