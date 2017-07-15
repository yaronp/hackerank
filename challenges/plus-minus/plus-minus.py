#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


res = [0.0,0.0,0.0]

for i in arr:
    if i > 0:
        res[0] += 1
    elif i < 0:    
        res[1] += 1
    elif i == 0:
        res[2] += 1       
tot = sum(res)

res = map(lambda x: x/tot, res)

for i in res:
    print("%.6f" % i)

        