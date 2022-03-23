# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/

from unittest import TestCase
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        n = len(s)
        left, right = 0, 0
        char_dict = defaultdict(int)

        while right < n:
            if len(char_dict) <= 2:
                char_dict[s[right]] = right
                right += 1

            if len(char_dict) > 2:
                min_idx = min(char_dict.values())
                del char_dict[s[min_idx]]
                left = min_idx + 1

            ans = max(ans, right - left)

        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "eceba"
        expected = 3
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "ababffzzeee"
        expected = 5
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "abcabcabc"
        expected = 2
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)
