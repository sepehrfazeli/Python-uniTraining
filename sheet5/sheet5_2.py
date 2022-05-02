import random
from sheet5.sheet5_1 import norm


def gen(x):
    return [[random.uniform(-1, 1), random.uniform(-1, 1)] for x in range(1, x)]


def check(x):
    return sum([1 for y in x if norm(y, 2) <= 1])


def Pi(x):
    return (check(gen(x)) / x) * 4


print(Pi(10000))
