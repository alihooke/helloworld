__author__ = 'alihooke'
import math

def primefactors(x):
    for i in range(2, int(math.sqrt(x))):
        if (x % i)==0:
            return [i] + primefactors(x//i)
    return [x]

print(max(primefactors(600851475143)))