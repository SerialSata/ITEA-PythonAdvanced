import gc
import sys

a = 1
b = a

print(sys.getrefcount(1))

b = 2

print(sys.getrefcount(1))

l = [1, 2, 3]
l.append(l)
print(l)
print(l[3])

d = {}
for i in range(10):
    d = {}
    d['a'] = d
print(d)
print(gc.collect())

print(.1+.2)

import math

print(math.fsum([.1, .1, .1, .1]))

import decimal

print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))
