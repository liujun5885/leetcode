# https://leetcode-cn.com/problems/combination-sum-ii/

from typing import List
from unittest import TestCase
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        seq = []
        candidate_counter = sorted(Counter(candidates).items())

        def dfs(pos, rest):
            nonlocal seq
            nonlocal ans
            if rest == 0:
                ans.append(seq[:])
                return

            if pos >= len(candidate_counter) or candidate_counter[pos][0] > rest:
                return

            dfs(pos + 1, rest)

            most = min(rest // candidate_counter[pos][0], candidate_counter[pos][1])
            for i in range(1, most + 1):
                seq.append(candidate_counter[pos][0])
                dfs(pos + 1, rest - i * candidate_counter[pos][0])

            seq = seq[:-most]

        dfs(0, target)

        return ans


class TestCases(TestCase):
    def test_case_01(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]
        actual = Solution().combinationSum2(candidates, target)
        self.assertEqual(sorted(expected), sorted(actual))
