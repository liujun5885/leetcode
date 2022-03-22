# https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

from unittest import TestCase


class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        s = [i for i in reversed(s)]
        i = 0
        while i < len(s):
            if i == len(s) - 1 and s[i] == '1':
                return ans

            if s[i] == '0':
                ans += 1
                i += 1
            else:
                ans += 1
                j = i
                while j < len(s) and s[j] == '1':
                    ans += 1
                    j += 1
                if j < len(s):
                    s[j] = '1'
                i = j

        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "1101"
        expected = 6
        actual = Solution().numSteps(s)
        self.assertEqual(actual, expected)

    def test_2(self):
        s = "10"
        expected = 1
        actual = Solution().numSteps(s)
        self.assertEqual(actual, expected)

    def test_3(self):
        s = "1"
        expected = 0
        actual = Solution().numSteps(s)
        self.assertEqual(actual, expected)
