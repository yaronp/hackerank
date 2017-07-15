#!/bin/python

import sys

def super_reduced_string(s):
    modified = False
    the_str = s

    while True:
        prev = ''
        new_s = ''
        for c in the_str:
            if prev == c:
                modified = True
                new_s = new_s[:-1]
                prev = ''
            else:
                new_s = new_s + c
                prev = c
        the_str = new_s
        if not modified or len(the_str) == 0:
            return 'Empty String' if len(the_str) == 0 else the_str
        modified = False

    
    

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
