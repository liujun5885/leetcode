# https://leetcode-cn.com/problems/string-compression/

from typing import List
import unittest


class Solution:
    def compress(self, chars: List[str]) -> int:
        mid_zipped = []
        i = 0
        while i < len(chars):
            c = chars[i]
            n = 0
            while i < len(chars) and chars[i] == c:
                n += 1
                i += 1

            if n > 1:
                mid_zipped.append(c + str(n))
            else:
                mid_zipped.append(c)

        result = ''.join(mid_zipped)
        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)


class TestCases(unittest.TestCase):
    def test_01(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6
        actual = Solution().compress(chars)
        self.assertEqual(actual, expected)
