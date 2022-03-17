# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return 0


class TestCases:
    def test_case_01(self):
        arr = ["un", "iq", "ue"]
        actual = Solution().maxLength(arr)
        expected = 4
        assert actual == expected
