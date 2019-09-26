import random

def test(a):
    for e in a:
        if e < 5 or e > 95:
            return False
    return True


a = [random.random() * 90 + 5 for i in range(30)]
print(a)
print(test(a))
