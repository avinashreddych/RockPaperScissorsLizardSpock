import math


def newton_sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess