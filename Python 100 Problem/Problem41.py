def printTuple():
    t = tuple(i**2 for i in range(1, 10))
    half = len(t) // 2
    print(t[:half])
    print(t[half:])


printTuple()
