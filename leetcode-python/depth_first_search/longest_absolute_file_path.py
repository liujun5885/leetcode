# https://leetcode-cn.com/problems/longest-absolute-file-path/

from unittest import TestCase
import os


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
            level_input.append((level, i.replace('\t', '')))

        level = 0
        folder = []
        for i in level_input:
            if '.' in i[1]:
                path_list.append(os.path.join(*(folder[:i[0]] + [i[1]])))
                continue
            if i[0] == level:
                level += 1
                folder.append(i[1])
            elif i[0] < level:
                # path_list.append('/'.join(folder))
                level = i[0]
                folder = folder[0:i[0]]
                folder.append(i[1])
                level += 1

        if len(path_list) == 0:
            return 0

        return max(map(lambda x: len(x), path_list))


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

    def test_03(self):
        input = "a"
        expected = 0
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(actual, expected)

    def test_04(self):
        input = "file1.txt\nfile2.txt\nlongfile.txt"
        expected = 12
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(actual, expected)

    def test_05(self):
        input = "dir\n        file.txt"
        expected = 16
        actual = Solution().lengthLongestPath(input)
        self.assertEqual(actual, expected)
