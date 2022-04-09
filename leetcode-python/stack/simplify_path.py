# https://leetcode-cn.com/problems/simplify-path/

from unittest import TestCase


class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []

        for i in path.split('/'):
            if not i or i == '.':
                continue
            elif i == '..':
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append(i)

        return '/' + '/'.join(ans)


class TestCases(TestCase):
    def test_1(self):
        path = "/home/"
        expected = "/home"
        actual = Solution().simplifyPath(path)
        self.assertEqual(actual, expected)

    def test_2(self):
        path = "/../"
        expected = "/"
        actual = Solution().simplifyPath(path)
        self.assertEqual(actual, expected)

    def test_3(self):
        path = "/home//foo/"
        expected = "/home/foo"
        actual = Solution().simplifyPath(path)
        self.assertEqual(actual, expected)
