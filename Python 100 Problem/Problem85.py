
def solve1():
    l = [5,6,77,45,22,12,24]
    result = list(filter(lambda x: x % 2 == 0, l))
    print(result)


def solve2():
    li = [5,6,77,45,22,12,24]
    # Code by Quantrimang.com
    li = [x for x in li if x%2!=0]
    print (li)
