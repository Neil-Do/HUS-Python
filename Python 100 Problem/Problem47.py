def useMapAndFilter():
    l = [i for i in range(1, 11)]
    l1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, l)))
    print("Map: ", l1)


useMapAndFilter()
