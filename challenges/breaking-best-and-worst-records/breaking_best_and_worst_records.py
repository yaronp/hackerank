#!/bin/python

import sys


def get_record(n,s):
    return s

if __name__ == '__main__':
    n = int(raw_input().strip())
    s = map(int, raw_input().strip().split(' '))
    result = get_record(n, s)
    print " ".join(map(str, result))
