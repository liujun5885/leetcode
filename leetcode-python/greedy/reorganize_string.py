class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ''
        return ans


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        s = "aab"
        actual = Solution().reorganizeString(s)
        expected = "aba"
        self.assertEqual(actual, expected)
