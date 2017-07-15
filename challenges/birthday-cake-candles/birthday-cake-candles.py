#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    m = max(ar)
    c = 0
    for i in ar:
      if m ==i:
        c += 1
    return c

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print (result)
