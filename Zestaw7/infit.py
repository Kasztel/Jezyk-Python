# Python program to demonstrate
# infinite iterators
# we can pr

import itertools
import random

counta = 0
countb = 0



# for in loop
print("a)")
for i in itertools.cycle('01'):
    if counta > 7:
        break
    else:
        print(i, end=", ")
        counta += 1
print()
print("b)")

directions = ['N', 'E', 'W', 'S']

it = (random.choice(directions) for _ in range(10))
for i in it:
    print(i, end=", ")



print()
print("c)")
for i in itertools.cycle('0123456'):
    if countb > 14:
        break
    else:
        print(i, end=", ")
        countb += 1
