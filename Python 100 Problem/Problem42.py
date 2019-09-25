def createTuple():
    t = tuple(i for i in range(1, 11))
    t2 = tuple(i for i in t if i % 2 == 0)
    print(t2)


createTuple()
