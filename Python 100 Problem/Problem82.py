import time

def solve1():
    t1 = time.time()
    print([str(1 + 1) for i in range(100)])
    t2 = time.time()
    print("running time: ", t2 - t1)


def solve2():
    from timeit import Timer
    t = Timer("for i in range(100):1+1")
    print (t.timeit())

solve1()
print()
solve2()
