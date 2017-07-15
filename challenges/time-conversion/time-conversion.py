#!/bin/python

import sys

def timeConversion(s):
    am = 'AM' in s

    s = s.strip('AMP')
    t = s.split(':')

    if t[0] == '12' and am:
        return '00' + ':' + t[1] + ':' + t[2]
    if t[0] == '12' and not am:
        return ':'.join(t)    
    if not am:
        return  str(int(t[0])+12) + ':' + t[1] + ':' + t[2]
    return ':'.join(t)   
        
s = raw_input().strip()
result = timeConversion(s)
print(result)
