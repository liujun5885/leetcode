# https://leetcode-cn.com/problems/minimum-path-sum/

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[rows - 1][cols - 1]


import unittest


class TestCases(unittest.TestCase):
    def test_01(self):
        grid = [[1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]]
        actual = Solution().minPathSum(grid)
        expected = 7
        self.assertEqual(actual, expected)

    def test_02(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        actual = Solution().minPathSum(grid)
        expected = 12
        self.assertEqual(actual, expected)
