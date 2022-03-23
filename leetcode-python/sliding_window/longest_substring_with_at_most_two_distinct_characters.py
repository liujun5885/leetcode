from unittest import TestCase


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "eceba"
        expected = 3
        actual = Solution().lengthOfLongestSubstringTwoDistinct(s)
        self.assertEqual(expected, actual)
