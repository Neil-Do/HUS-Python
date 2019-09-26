def solve1():
    l = [12,24,35,70,88,120,155]
    print([e for e in l if e % 35 != 0])


def solve2():
    l = [12,24,35,70,88,120,155]
    print(list(filter(lambda x: x % 35 != 0, l)))


solve2()
