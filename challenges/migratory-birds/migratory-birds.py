#!/bin/python

import unittest


def migratory_birds(n, ar):
    print n
    res = []
    for i in range(100):
        res.append(0)
    for a in ar:
        res[a] = res[a] + 1
    return res.index(max(res))


class TestBreakingBest(unittest.TestCase):
    def test_case1(self):
        s = "1 4 4 4 5 3"
        res = migratory_birds(6, map(int, s.strip().split(' ')))

        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
