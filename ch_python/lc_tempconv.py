#!/usr/bin/env python

flist = [32, 212, 10, 55, 78, 110, 178]
clist = []

for f in flist:
    c = (f - 32) * 5 / 9
    clist.append(c)

print(flist)
print(clist)

#

flist = [32, 212, 10, 55, 78, 110, 178]
clist = [(f - 32) * 5 / 9 for f in flist]

print(flist)
print(clist)

