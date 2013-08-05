#!/usr/bin/env python

def ftoc(f):
    return (f - 32) * 5 / 9

def ctof(c):
    return c * (9 / 5) + 32

print("Celsius degree 55 is equal to Fahrenheit degree " + str(ctof(55)));
print("Fahrenheit degree 55 is equal to Celsius degree " + str(ftoc(55)));

