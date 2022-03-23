# https://leetcode-cn.com/problems/video-stitching/

from typing import List
from unittest import TestCase


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        ans = 0
        left, right = 0, 0

        max_n = [0 for _ in range(time)]
        for a, b in clips:
            if 0 <= a < time:
                max_n[a] = max(max_n[a], b)

        for i in range(time):
            right = max(right, max_n[i])
            if i == right:
                return -1

            if i == left:
                ans += 1
                left = right

        return ans


class TestCases(TestCase):
    def test_1(self):
        clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
        time = 10
        expected = 3
        actual = Solution().videoStitching(clips, time)
        self.assertEqual(expected, actual)
