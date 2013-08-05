#!/usr/bin/env python

def acc(n = 0):
    rst = 0
    for i in range(n+1):
        rst += i
    return rst

for i in range(10):
    print("acc(" + str(i) + ") returns " + str(acc(i)))

print("acc() returns " + str(acc()))

