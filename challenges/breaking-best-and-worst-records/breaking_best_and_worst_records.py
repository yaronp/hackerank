#!/bin/python
import math


def get_record(s):
    scores = map(int, s.strip().split(' '))
    max_score = min_score = scores[0]
    min_count, max_count = 0, 0

    i = 0
    for j in range(len(scores)-1):
        i = i + 1
        if scores[j+1] > max_score:
            max_count = max_count + 1
            max_score = scores[j+1]
        if scores[j+1] < min_score:
            min_count = min_count + 1
            min_score = scores[j+1]
    return [str(min_count), str(max_count)]


if __name__ == '__main__':
    n = int(raw_input().strip())
    s = map(int, raw_input().strip().split(' '))
    result = get_record(s)
    print " ".join(result)
