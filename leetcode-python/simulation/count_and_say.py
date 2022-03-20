# https://leetcode-cn.com/problems/count-and-say/

from unittest import TestCase


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):
            cur = ''
            char_n = 1
            j = 1
            while j < len(ans):
                if ans[j] == ans[j - 1]:
                    char_n += 1
                else:
                    cur += str(char_n) + ans[j - 1]
                    char_n = 1
                j += 1
            cur += str(char_n) + ans[j - 1]
            ans = cur
        return ans


class TestCases(TestCase):
    def test_1(self):
        n = 4
        expected = "1211"
        actual = Solution().countAndSay(n)
        self.assertEqual(actual, expected)
