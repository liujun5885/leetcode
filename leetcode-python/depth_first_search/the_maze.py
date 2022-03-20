# https://leetcode-cn.com/problems/the-maze/

from unittest import TestCase
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(x, y):
            if x < 0 or x >= rows or y >= cols or y < 0 or visited[x][y]:
                return False
            if x == destination[0] and y == destination[1]:
                return True

            visited[x][y] = True
            up, down, left, right = x - 1, x + 1, y - 1, y + 1
            while up >= 0 and maze[up][y] == 0:
                up -= 1

            if dfs(up + 1, y):
                return True

            while down < rows and maze[down][y] == 0:
                down += 1

            if dfs(down - 1, y):
                return True

            while left >= 0 and maze[x][left] == 0:
                left -= 1
            if dfs(x, left + 1):
                return True

            while right < cols and maze[x][right] == 0:
                right += 1

            if dfs(x, right - 1):
                return True

            return False

        return dfs(start[0], start[1])


class TestCases(TestCase):
    def test_1(self):
        maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
        start = [4, 3]
        destination = [0, 1]
        expected = False
        actual = Solution().hasPath(maze, start, destination)
        self.assertEqual(actual, expected)
