import math


def add_frac(frac1, frac2):
    x = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    y = frac1[1] * frac2[1]
    return lowest_frac([x, y])


def sub_frac(frac1, frac2):
    x = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    y = frac1[1] * frac2[1]
    return lowest_frac([x, y])


def mul_frac(frac1, frac2):
    x = frac1[0] * frac2[0]
    y = frac1[1] * frac2[1]
    return lowest_frac([x, y])


def div_frac(frac1, frac2):
    x = frac1[0] * frac2[1]
    y = frac1[1] * frac2[0]
    return lowest_frac([x, y])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def frac2float(frac):
    return float(frac[0] / frac[1])


def cmp_frac(frac1, frac2):
    comp1 = frac2float(lowest_frac(frac1))
    comp2 = frac2float(lowest_frac(frac2))

    if (comp1 > comp2):
        return 1
    elif (comp1 == comp2):
        return 0
    else:
        return -1


def lowest_frac(frac):
    fin = [0, 0]
    nwd = math.gcd(frac[0], frac[1])
    fin[0] = frac[0] / nwd
    fin[1] = frac[1] / nwd

    return fin
