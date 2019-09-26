import random

def solve2():
    print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))


def test(a):
    for e in a:
        if e < 0 or e > 200:
            return False
    return True


a = [random.randint(0, 5) * 35 for i in range(30)]
print(a)
print(test(a))
