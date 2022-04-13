# https://leetcode-cn.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter
from unittest import TestCase
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        num_counter = Counter(nums)
        for key, v in num_counter.items():
            pq.append((v, key))

        k_largest = heapq.nlargest(k, pq)
        ans = []
        for i in k_largest:
            ans.append(i[1])

        return ans


class TestCases(TestCase):
    def test_1(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        expected = [1, 2]
        actual = Solution().topKFrequent(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, k = [1], 1
        expected = [1]
        actual = Solution().topKFrequent(nums, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums, k = [4, 1, -1, 2, -1, 2, 3], 2
        expected = [2, -1]
        actual = Solution().topKFrequent(nums, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums, k = [1, 2], 2
        expected = [2, 1]
        actual = Solution().topKFrequent(nums, k)
        self.assertEqual(expected, actual)
