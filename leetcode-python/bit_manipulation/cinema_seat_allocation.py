# https://leetcode-cn.com/problems/cinema-seat-allocation/

from unittest import TestCase
from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        for seat in reservedSeats:
            if 1 < seat[1] < 10:
                reserved[seat[0]] |= 1 << seat[1] - 1

        ans = (n - len(reserved)) * 2
        masks = [0b1000011111, 0b1110000111, 0b1111100001]
        for i in reserved.values():
            for j in masks:
                if i | j == j:
                    ans += 1
                    break

        return ans


class TestCases(TestCase):
    def test_1(self):
        n = 3
        reserved_seats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
        expected = 4
        actual = Solution().maxNumberOfFamilies(n, reserved_seats)
        self.assertEqual(actual, expected)

    def test_2(self):
        n = 4
        reserved_seats = [[4, 3], [1, 4], [4, 6], [1, 7]]
        expected = 4
        actual = Solution().maxNumberOfFamilies(n, reserved_seats)
        self.assertEqual(actual, expected)
