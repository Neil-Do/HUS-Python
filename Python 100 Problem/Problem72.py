def isDescent(l):
    for i in range(len(l) - 1):
        if l[i + 1] > l[i]:
            return False
    return True


def isAscent(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True


def isOrder(l):
    if not (isDescent(l) or isAscent(l)):
        return False
    return True

from bisect import bisect_left

def binarySearch(l, x):
    try:
        assert isinstance(l, list)
        if not isOrder(l):
            l.sort()
        elif isDescent(l):
            l.reverse()

        i = bisect_left(l, x)
        if i != len(l) and l[i] == x:
            return i
        return -1

    except AssertionError:
        print("Parameter is not list.")


a = [1, 2, 4, 5, 5, 7, 9]
a.reverse()
print(a)
print(binarySearch(a, 5))
print(a)
