import math


def norm(v, p):
    under = sum([x ** p for x in v])
    log = (1 / p) * (math.log10(under))
    return 10 ** log


print(norm([2, 2], 2))
