# https://leetcode-cn.com/problems/spiral-matrix-ii/

from typing import List
from unittest import TestCase


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]

        x, y = 0, 0
        cur = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(1, n * n + 1):
            ans[x][y] = i

            next_x, next_y = x + directions[cur][0], y + directions[cur][1]
            if next_x >= n or next_x < 0 or next_y >= n or next_y < 0 or ans[next_x][next_y] != 0:
                cur = (cur + 1) % 4
            x, y = x + directions[cur][0], y + directions[cur][1]

        return ans


class TestCases(TestCase):
    def test_1(self):
        n = 3
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        actual = Solution().generateMatrix(n)
        self.assertListEqual(expected, actual)
