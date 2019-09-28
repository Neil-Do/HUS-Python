import random as rd
from math import sqrt


def createCoordinates(n):
    coordinatesList = []
    for i in range(n):
        coordinates = [rd.randint(0, 10) for j in range(3)]
        coordinatesList.append(coordinates)
    for e in coordinatesList:
        print(e)
    return coordinatesList


def dotProduct(a, b):
    try:
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i]
        return sum
    except:
        print("Dot product method error.")


def getNorm(a):
    a = [n**2 for n in a]
    return sqrt(sum(a))


def getCosine(a, b):
    return dotProduct(a, b) / (getNorm(a) * getNorm(b))


def bai10():
    coordinatesList = createCoordinates(4)
    max_cosin_value = float('-inf')
    max_couple = ()
    min_cosin_value = float("inf")
    min_couple = ()
    for i in range(len(coordinatesList)):
        for j in range(i + 1, len(coordinatesList)):
            cosine = getCosine(coordinatesList[i], coordinatesList[j])
            if cosine > max_cosin_value:
                max_cosin_value = cosine
                max_couple = (i, j)
            if cosine < min_cosin_value:
                min_cosin_value = cosine
                min_couple = (i, j)
    print(max_couple)
    print(max_cosin_value)
    print(min_couple)
    print(min_cosin_value)


bai10()
