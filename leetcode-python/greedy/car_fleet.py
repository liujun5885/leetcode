# https://leetcode-cn.com/problems/car-fleet/

from typing import List
import unittest


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_vs_speed = sorted(zip(position, speed), key=lambda x: x[0])
        time_list = [float(target - pos) / sp for pos, sp in pos_vs_speed]
        ans = 1
        cur_time = time_list[len(time_list) - 1]
        for i in range(len(time_list) - 1, -1, -1):
            if time_list[i] > cur_time:
                ans += 1

            cur_time = max(cur_time, time_list[i])

        return ans


class TestCases(unittest.TestCase):
    def test_01(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        expected = 3
        actual = Solution().carFleet(target, position, speed)
        self.assertEqual(actual, expected)

    def test_02(self):
        target = 10
        position = [3]
        speed = [3]
        expected = 1
        actual = Solution().carFleet(target, position, speed)
        self.assertEqual(actual, expected)

    def test_03(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        expected = 1
        actual = Solution().carFleet(target, position, speed)
        self.assertEqual(actual, expected)
