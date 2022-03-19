# https://leetcode-cn.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n_r = len(matrix)
        n_c = len(matrix[0])
        visited = [[False for _ in range(n_c)] for _ in range(n_r)]
        ans = []
        position = [0, 0]
        direction_idx = 0
        for i in range(n_r * n_c):
            ans.append(matrix[position[0]][position[1]])
            visited[position[0]][position[1]] = True
            next_row = position[0] + directions[direction_idx][0]
            next_col = position[1] + directions[direction_idx][1]

            if (next_row < 0 or next_row >= n_r) or (next_col < 0 or next_col >= n_c) or visited[next_row][next_col]:
                direction_idx = (direction_idx + 1) % 4

            position[0] += directions[direction_idx][0]
            position[1] += directions[direction_idx][1]

        return ans


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual = Solution().spiralOrder(matrix)
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertListEqual(actual, expected)
