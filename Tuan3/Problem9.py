from math import sqrt

def E(x):
    return sum(x) / len(x)


def D(x):
    power_2_of_x = [e**2 for e in x]
    return E(power_2_of_x) - (E(x)) ** 2


def sd(x):
    return sqrt(D(x))
