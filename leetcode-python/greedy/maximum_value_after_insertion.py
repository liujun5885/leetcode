class Solution:
    def maxValue(self, n: str, x: int) -> str:
        pass


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        n = "99"
        x = 9
        actual = Solution().maxValue(n, x)
        expected = "999"
        self.assertEqual(actual, expected)
