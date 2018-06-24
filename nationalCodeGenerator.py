import random
import math


def getRandomArbitrary(min, max):
    return random.random() * (max - min) + min;


def NationalCodeGenerator():
    nccode = []
    sum = 0
    last = 0

    for i in range(1, 10):
        rndnumber = math.floor(getRandomArbitrary(0, 9))
        nccode.append(rndnumber)
        sum = sum + (rndnumber * i)

    res = sum % 11
    if res < 2:
        last = res
    else:
        last = 11 - res

    nccode.append(last)

    string = ''
    for item in nccode:
        string += item.__str__()

    return string