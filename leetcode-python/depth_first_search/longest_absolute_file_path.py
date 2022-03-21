# https://leetcode-cn.com/problems/longest-absolute-file-path/

from unittest import TestCase


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path_list = []
        level_input = []
        for i in input.split('\n'):
            level = 0
            for j in i:
                if j != '\t':
                    break
                level += 1
            level_input.append((level, i.strip()))

        def dfs(s: str):
            return

        return len(path_list)


class TestCases(TestCase):
    def test_01(self):
        input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        expected = 20
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(actual, expected)

    def test_02(self):
        input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        expected = 32
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(actual, expected)
