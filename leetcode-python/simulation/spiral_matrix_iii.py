# https://leetcode-cn.com/problems/spiral-matrix-iii/

from typing import List
import unittest


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[]]
        return ans


class TestCases(unittest.TestCase):
    def test_case_01(self):
        rows = 1
        cols = 4
        rStart = 0
        cStart = 0
        actual = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
        expected = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.assertListEqual(actual, expected)
