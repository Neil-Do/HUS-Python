import random

def solve2():
    print (random.choice([i for i in range(11) if i%2==0]))


def test(a):
    for e in a:
        if e < 0 or e >= 11 or e % 2 == 1:
            return False
    return True


a = [random.randint(0, 5) * 2 for i in range(30)]
print(a)
print(test(a))
