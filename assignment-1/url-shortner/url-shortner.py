from math import floor
import string

def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    res = base[r]
    quotient = floor(num/b)

    while quotient:
        r = quotient % b
        quotient = floor(quotient / b)
        res = base[int(r)] + res
    return res

def tobase10(num, b = 62):
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    limit = len(num)
    result = 0

    for i in range(limit):
        result = b * result + base.find(num[i])

    return result

encoder = toBase62(1234)
print(toBase62(1234))
print(tobase10(encoder))
