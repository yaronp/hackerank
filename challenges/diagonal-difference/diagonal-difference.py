#!/bin/python

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)

v0, v1 = 0, 0
for i in range(n):
    v0 = v0 + a[i][i]
    v1 = v1 + a[n-i-1][i]   
print abs(v0-v1)
