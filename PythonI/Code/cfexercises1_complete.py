#!/usr/bin/env python3

"""Some simple functions from the MulQuaBio Python I practical."""
__author__ = 'Michael Jordan (mgj23@imperial.ac.uk)'
__version__ = '0.0.1'

import sys

def foo_1(x):
    return x ** 0.5

def foo_2(x, y):
    if x > y:
        return x
    return y

def foo_3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo_4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x): # a recursive function that calculates the factorial of x
    if x == 1:
        return 1
    return x * foo_5(x - 1)
     
def foo_6(x): # Calculate the factorial of x in a different way; no if statement involved
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

def main(argv):
    print(foo_1(4))
    print(foo_2(2, 4))
    print(foo_3(1, 2, 3))
    print(foo_4(4))
    print(foo_5(4))
    print(foo_6(4))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
