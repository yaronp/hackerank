#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    
    for i in xrange(1, 10000):
        if (x1 + (i*v1)) == (x2 + (i*v2)):
            return 'YES'
    return 'NO'
        
    
    # Complete this function

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
