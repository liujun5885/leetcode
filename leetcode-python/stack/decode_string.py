# https://leetcode-cn.com/problems/decode-string/

from unittest import TestCase


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                buf = ""
                repeat = ""
                while len(stack) > 0:
                    val = stack.pop()
                    if val == "[":
                        while len(stack) > 0 and stack[-1].isdigit():
                            repeat = stack.pop() + repeat
                        break
                    else:
                        buf = val + buf
                stack.append(int(repeat) * buf)

        return ''.join(stack)


class TestCases(TestCase):
    def test_1(self):
        s = "3[a]2[bc]"
        expected = 'aaabcbc'
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "3[a2[c]]"
        expected = 'accaccacc'
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "2[abc]3[cd]ef"
        expected = 'abcabccdcdcdef'
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "abc3[cd]xyz"
        expected = 'abccdcdcdxyz'
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = ""
        expected = ''
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "100[leetcode]"
        expected = "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)
