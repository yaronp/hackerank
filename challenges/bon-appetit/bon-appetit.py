#!/bin/python

import unittest


def bon_appetit(n, k, b, ar):
    r = b - ((sum(ar) - ar[k]) / 2)
    if r is 0:
        return "Bon Appetit"
    else:
        return r


class TestBreakingBest(unittest.TestCase):
    def test_case1(self):
        res = bon_appetit(4, 1, 12, [3, 10, 2, 9])

        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
