# https://leetcode-cn.com/problems/search-a-2d-matrix/

from typing import List
from unittest import TestCase


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])
            print(start, end, x, y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False


class TestCases(TestCase):
    def test_1(self):
        matrix = [[1, 1]]
        target = 2
        expected = False
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)
