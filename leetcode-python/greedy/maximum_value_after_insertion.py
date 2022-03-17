# https://leetcode-cn.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = ""
        if n[0] == '-':
            sign = "-"
            n = n[1:]

        n_len = len(n)
        i = 0
        while i < n_len:
            if (not sign and int(n[i]) < x) or (sign and int(n[i]) > x):
                break
            i += 1

        if i == 0:
            return sign + str(x) + n
        else:
            return sign + n[:i] + str(x) + n[i:]


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        n = "73"
        x = 6
        actual = Solution().maxValue(n, x)
        expected = "763"
        self.assertEqual(actual, expected)

    def test_case_02(self):
        n = "73"
        x = 1
        actual = Solution().maxValue(n, x)
        expected = "731"
        self.assertEqual(actual, expected)

    def test_case_03(self):
        n = "-55"
        x = 2
        actual = Solution().maxValue(n, x)
        expected = "-255"
        self.assertEqual(actual, expected)

    def test_case_04(self):
        n = "-55"
        x = 6
        actual = Solution().maxValue(n, x)
        expected = "-556"
        self.assertEqual(actual, expected)
