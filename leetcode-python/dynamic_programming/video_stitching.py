# https://leetcode-cn.com/problems/video-stitching/

from typing import List
from unittest import TestCase


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        ans = 0
        return ans


class TestCases(TestCase):
    def test_1(self):
        clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
        time = 10
        expected = 3
        actual = Solution().videoStitching(clips, time)
        self.assertEqual(expected, actual)
