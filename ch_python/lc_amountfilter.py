#!/usr/bin/env python

amount = [33, 15, 3100, 568, 299, 75, 68]
amount2 = [x for x in amount if x <= 1000]

print(amount2)
print(sum(amount2)) 

