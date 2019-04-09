from math import floor
import string

def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.lowercase + strimg.uppercase
    r = num % b
    res = base[r]
    quotient = floor(num/b)

    while quotient:
        r = quotient % b
        quotient = floor(quotient / b)
        res = base[int(r)] + res
    return res
