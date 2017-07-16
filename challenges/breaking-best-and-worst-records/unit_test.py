import unittest

from breaking_best_and_worst_records import get_record


class TestBreakingBest(unittest.TestCase):
    def test_case1(self):
        s = "10 5 20 20 4 5 2 25 1"
        res = get_record(map(int, s.strip().split(' ')))
        self.assertEqual(res, [4, 2])

    def test_case2(self):
        s = "3 4 21 36 10 28 35 5 24 42"
        res = get_record(map(int, s.strip().split(' ')))
        self.assertEqual(res, [4, 2])


if __name__ == '__main__':
    unittest.main()
