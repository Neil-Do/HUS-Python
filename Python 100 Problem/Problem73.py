import random

def test(a):
    for e in a:
        if e < 10 or e >= 101:
            return False
    return True


a = [random.random() * 90 + 10 for i in range(30)]
print(a)
print(test(a))
