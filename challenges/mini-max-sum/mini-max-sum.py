#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
asum = sum(arr)
max = 0
min = asum
for i in arr:
  curr = asum-i
  if max < curr:
        max = curr
  if min > curr:
    min = curr
print min, max
