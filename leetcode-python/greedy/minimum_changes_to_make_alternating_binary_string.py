# https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string/

from unittest import TestCase


class Solution:
    def minOperations(self, s: str) -> int:
        # split answer from odd and even
        even_ans = 0
        odd_ans = 0
        n = len(s)

        for i in range(n):
            if i % 2 == 0:
                if s[i] != '0':
                    even_ans += 1
                else:
                    odd_ans += 1
            else:
                if s[i] != '1':
                    even_ans += 1
                else:
                    odd_ans += 1

        return min(even_ans, odd_ans)


class TestCases(TestCase):
    def test_1(self):
        expected = 3
        actual = Solution().minOperations("10010100")
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = 3
        actual = Solution().minOperations("1100010111")
        self.assertEqual(expected, actual)
