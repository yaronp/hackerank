#!/bin/python

import sys

def do_logic(grade):
    d = grade % 10
    if grade  >= 38:
        if d < 5 and d > 2:
            return grade + 5 - d
        if d < 10 and d > 7:
            return grade + (10 - d)
    return grade

def solve(grades):
    return map(do_logic, grades)

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))

