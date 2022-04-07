# https://leetcode-cn.com/problems/snakes-and-ladders/
from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        q = deque([(1, 0)])

        def id_to_x_y(id: int):
            # convert id to row and column.
            x = n - (id - 1) // n - 1
            if (n - 1 - x) % 2 == 0:
                y = (id - 1) % n
            else:
                y = n - 1 - (id - 1) % n
            return x, y

        while len(q) > 0:
            p = q.popleft()
            for i in range(1, 7):
                idx = p[0] + i
                if idx > n * n:
                    break

                x, y = id_to_x_y(idx)
                if board[x][y] != -1:  # if it's a ladder or a snake, next is board[x][y]
                    idx = board[x][y]

                if idx == n * n:  # if next is n * n, it's the end, move = current move + 1
                    return p[1] + 1

                if idx not in visited:
                    visited.add(idx)
                    q.append((idx, p[1] + 1))  # move to next

        return -1


class TestCases(TestCase):
    def test_1(self):
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1]
        ]
        expected = 4
        actual = Solution().snakesAndLadders(board)
        self.assertEqual(expected, actual)

    def test_2(self):
        board = [
            [-1, -1], [-1, 3]
        ]
        expected = 1
        actual = Solution().snakesAndLadders(board)
        self.assertEqual(expected, actual)
