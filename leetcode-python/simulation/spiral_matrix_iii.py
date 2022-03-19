# https://leetcode-cn.com/problems/spiral-matrix-iii/

from typing import List
import unittest


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]

        i = 1
        while True:
            for r, c, steps in ((0, 1, i), (1, 0, i), (0, -1, i + 1), (-1, 0, i + 1)):
                for _ in range(steps):
                    rStart += r
                    cStart += c
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                    if len(ans) == rows * cols:
                        return ans

            i += 2


class TestCases(unittest.TestCase):
    def test_case_01(self):
        rows = 1
        cols = 4
        rStart = 0
        cStart = 0
        actual = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
        expected = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.assertListEqual(actual, expected)

    def test_case_02(self):
        rows = 5
        cols = 6
        rStart = 1
        cStart = 4
        actual = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
        expected = [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3],
                    [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1],
                    [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
        self.assertListEqual(actual, expected)
