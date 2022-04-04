# https://leetcode-cn.com/problems/sqrtx/

from unittest import TestCase


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            ans = (l + r) // 2
            if ans * ans < x:
                l = ans + 1
            elif ans * ans > x:
                r = ans - 1
            else:
                return ans
        return (l + r) // 2


class TestCases(TestCase):
    def test_1(self):
        x = 6
        expected = 2
        actual = Solution().mySqrt(x)
        self.assertEqual(expected, actual)

    def test_2(self):
        x = 8
        expected = 2
        actual = Solution().mySqrt(x)
        self.assertEqual(expected, actual)

    def test_3(self):
        x = 9
        expected = 3
        actual = Solution().mySqrt(x)
        self.assertEqual(expected, actual)

    def test_4(self):
        x = 0
        expected = 0
        actual = Solution().mySqrt(x)
        self.assertEqual(expected, actual)

    def test_5(self):
        x = 1
        expected = 1
        actual = Solution().mySqrt(x)
        self.assertEqual(expected, actual)
