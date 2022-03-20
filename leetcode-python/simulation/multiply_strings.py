# https://leetcode-cn.com/problems/multiply-strings/

from unittest import TestCase


class Solution:

    def add(self, num1: str, num2: str):
        ans = ""
        reversed_num1 = ''.join(reversed(num1))
        reversed_num2 = ''.join(reversed(num2))
        p = 0
        i = 0
        while i < len(num1) and i < len(num2):
            ans = str((int(reversed_num1[i]) + int(reversed_num2[i]) + p) % 10) + ans
            p = (int(reversed_num1[i]) + int(reversed_num2[i]) + p) // 10
            i += 1
        while i < len(num1):
            ans = str((int(reversed_num1[i]) + p) % 10) + ans
            p = (int(reversed_num1[i]) + p) // 10
            i += 1
        while i < len(num2):
            ans = str((int(reversed_num2[i]) + p) % 10) + ans
            p = (int(reversed_num2[i]) + p) // 10
            i += 1

        if p > 0:
            ans = str(p) + ans

        return ans

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        multiply_values = []
        len_1 = len(num1)
        len_2 = len(num2)

        for i in range(len_1 - 1, -1, -1):
            mid = ""
            p = 0
            for j in range(len_2 - 1, -1, -1):
                mid = str((int(num1[i]) * int(num2[j]) + p) % 10) + mid
                p = (int(num1[i]) * int(num2[j]) + p) // 10
            if p > 0:
                mid = str(p) + mid
            mid += '0' * (len_1 - i - 1)
            multiply_values.append(mid)

        ans = "0"
        for i in multiply_values:
            ans = self.add(i, ans)

        return ans


class TestCases(TestCase):
    def test_1(self):
        num1 = "123"
        num2 = "456"
        expected = "56088"
        actual = Solution().multiply(num1, num2)
        self.assertEqual(actual, expected)

    def test_2(self):
        import random
        num1 = random.randint(1, 10000)
        num2 = random.randint(1, 10000)
        expected = str(num1 * num2)
        actual = Solution().multiply(str(num1), str(num2))
        self.assertEqual(actual, expected)
