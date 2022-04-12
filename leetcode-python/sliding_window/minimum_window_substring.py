# https://leetcode-cn.com/problems/minimum-window-substring/

from unittest import TestCase
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        m, n = len(s), len(t)
        start = 0
        end = 0
        t_counter = Counter(t)
        s_counter = Counter()

        def t_in_window():
            for k, v in t_counter.items():
                if s_counter.get(k, 0) < v:
                    return False
            return True

        while start < m and end < m:
            while not t_in_window() and end < m:
                s_counter[s[end]] += 1
                end += 1

            if not t_in_window():  # if t is not in window, it means there is no substring from t.
                break

            while t_in_window() and start < m:
                s_counter[s[start]] -= 1
                start += 1

            s_counter[s[start - 1]] += 1  # add previous char
            if t_in_window() and (ans == "" or len(ans) > end - start + 1):
                ans = s[start - 1:end]
            s_counter[s[start - 1]] -= 1  # remove added char

        return ans


class TestCases(TestCase):
    def test_1(self):
        s, t = "ADOBECODEBANC", "ABC"
        expected = "BANC"
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        s, t = "a", "a"
        expected = "a"
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_3(self):
        s, t = "a", "aa"
        expected = ""
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)
