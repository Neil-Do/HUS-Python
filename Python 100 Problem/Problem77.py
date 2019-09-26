import random

def test(a):
    for e in a:
        if e < 100 or e > 200:
            return False
    return True


a = random.sample(range(100, 201), 5)
print(a)
print(test(a))
