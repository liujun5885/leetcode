# https://leetcode-cn.com/problems/roman-to-integer/

from unittest import TestCase


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        one_char_vs_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        two_char_vs_num = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        i = 0
        while i < len(s):
            if s[i:i + 2] in two_char_vs_num:
                ans += two_char_vs_num[s[i:i + 2]]
                i += 2
            else:
                ans += one_char_vs_num[s[i:i + 1]]
                i += 1

        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "III"
        expected = 3
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "LVIII"
        expected = 58
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "MCMXCIV"
        expected = 1994
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "I"
        expected = 1
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)
