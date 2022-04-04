# https://leetcode-cn.com/problems/snakes-and-ladders/

from typing import List
from unittest import TestCase


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ans = 0
        return ans


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
