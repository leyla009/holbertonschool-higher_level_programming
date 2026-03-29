#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:
        return 0

    num = 0  # Numerator: sum of (score * weight)
    den = 0  # Denominator: sum of weights

    for tup in my_list:
        num += (tup[0] * tup[1])
        den += tup[1]

    return num / den
