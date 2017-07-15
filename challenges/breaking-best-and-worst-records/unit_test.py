import unittest

from breaking_best_and_worst_records import get_record


class TestBreakingBest(unittest.TestCase):
    def test_case1(self):
        n = "9"
        s = "10 5 20 20 4 5 2 25 1"
        res = get_record(n, s)
        self.assertEqual(res, [4, 0])


if __name__ == '__main__':
    unittest.main()
