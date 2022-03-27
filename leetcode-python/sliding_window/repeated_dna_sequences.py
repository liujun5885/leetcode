# https://leetcode-cn.com/problems/repeated-dna-sequences/
from typing import List
from unittest import TestCase


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seq_set = set()

        n = len(s)
        if n < 10:
            return list(ans)

        for i in range(n - 9):
            if s[i:i + 10] in seq_set:
                ans.add(s[i:i + 10])
            else:
                seq_set.add(s[i:i + 10])

        return list(ans)


class TestCases(TestCase):
    def test_1(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["AAAAACCCCC", "CCCCCAAAAA"]
        actual = Solution().findRepeatedDnaSequences(s)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_2(self):
        s = "AAAAAAAAAAA"
        expected = ["AAAAAAAAAA"]
        actual = Solution().findRepeatedDnaSequences(s)
        self.assertEqual(sorted(expected), sorted(actual))
