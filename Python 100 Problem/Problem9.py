from math import sqrt
def evaluate(d):
    c = 50
    h = 30
    q = sqrt((2 * c * d) / h)
    print("%d bang can bac 2 cua [(2 nhan %d nhan %d) chia %d]" % (q, c, d, h))


evaluate(100)
