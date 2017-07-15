#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    result = [0,0]
    if a0 > b0:
        result[0] = result[0] + 1
    elif b0 > a0:     
        result[1] = result[1] + 1

    if a1 > b1:
        result[0] = result[0] + 1
    elif b1 > a1:    
        result[1] = result[1] + 1

    if a2 > b2:
        result[0] = result[0] + 1
    elif b2 > a2:    
        result[1] = result[1] + 1
        
    return result

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))

