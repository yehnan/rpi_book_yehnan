#!/usr/bin/env python

a = [1, 2, 3, 4, 5]
b = a
b[2] = 99
print(a)
print(b)



a = [1, 2, 3, 4, 5]
b = list(a)
b[2] = 99
print(a)
print(b)

