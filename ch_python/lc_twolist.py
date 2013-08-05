#!/usr/bin/env python

xlist = range(2, 10)
ylist = range(1, 10)
result = [str(x) + " * " + str(y) + " = " + str(x * y) for x in xlist for y in ylist]

print(result)
