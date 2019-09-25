def createList():
    l = [i**2 for i in range(1, 21)]
    for i in range(5, len(l)):
        print(l[i])


createList()
