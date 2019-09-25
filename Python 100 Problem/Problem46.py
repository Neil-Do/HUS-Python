def squareList():
    l = [i for i in range(1, 11)]
    l2 = list(map(lambda x: x**2, l))
    print(l2)


squareList()
