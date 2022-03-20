# https://leetcode-cn.com/problems/basic-calculator-ii/

from unittest import TestCase


class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        stripped_input = []
        num = ""
        for i in s.replace(' ', ''):
            if i.isdigit():
                num += i
            else:
                stripped_input.append(num)
                num = ""
                stripped_input += i
        stripped_input.append(num)
        i = 0
        while i < len(stripped_input):
            if stripped_input[i] == "*":
                middle_result = stack.pop()
                middle_result *= int(stripped_input[i + 1])
                stack.append(middle_result)
                i += 1
            elif stripped_input[i] == "/":
                middle_result = stack.pop()
                if middle_result // int(stripped_input[i + 1]) >= 0 or middle_result % int(stripped_input[i + 1]) == 0:
                    middle_result //= int(stripped_input[i + 1])
                else:
                    middle_result //= int(stripped_input[i + 1])
                    middle_result += 1
                stack.append(middle_result)
                i += 1
            elif stripped_input[i] == '+':
                stack.append(int(stripped_input[i + 1]))
                i += 1
            elif stripped_input[i] == '-':
                stack.append(-1 * int(stripped_input[i + 1]))
                i += 1
            else:
                stack.append(int(stripped_input[i]))
            i += 1

        ans = 0
        for i in stack:
            ans += i
        return ans


class TestCases(TestCase):
    def test_1(self):
        s = "3+2*2"
        expected = 7
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)

    def test_2(self):
        s = " 3/2 "
        expected = 1
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)

    def test_3(self):
        s = " 3+5 / 2 "
        expected = 5
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)

    def test_4(self):
        s = " 31+5 / 2 "
        expected = 33
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)

    def test_5(self):
        s = "14-3/2"
        expected = 13
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)

    def test_6(self):
        s = "14-13/2"
        expected = 8
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)
