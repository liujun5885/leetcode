# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mask_list = []
        for s in arr:
            mask = 0
            for i in s:
                idx = ord(i) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                else:
                    mask |= 1 << idx
            if mask > 0:
                mask_list.append(mask)

        ans = 0

        def traceback(n, m):
            nonlocal ans
            if n == len(mask_list):
                ans = max(ans, bin(m).count('1'))
                return

            if mask_list[n] & m == 0:
                traceback(n + 1, mask_list[n] | m)
            traceback(n + 1, m)

        traceback(0, 0)

        return ans


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        arr = ["un", "iq", "ue"]
        actual = Solution().maxLength(arr)
        expected = 4
        self.assertEqual(actual, expected)
