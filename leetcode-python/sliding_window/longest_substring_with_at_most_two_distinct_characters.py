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
            while left <= right and len(char_dict) > 2:
                char_dict[s[left]] -= 1
                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1

            while right < n:
                char_dict[s[right]] += 1
                if len(char_dict) > 2:
                    break
                else:
                    right += 1

            ans = max(ans, right - left)

        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "eceba"
        expected = 3
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "ccaabbb"
        expected = 5
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)
