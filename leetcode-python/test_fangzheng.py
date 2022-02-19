import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        result = 0

        ceiling = int(math.pow(2, 31)) // 10
        print(int(math.pow(2, 31)))

        x = abs(x)
        while x != 0:
            divisor = x // 10
            reminder = x - divisor * 10
            result = result * 10 + reminder
            x = divisor
            if x > 0 and result > ceiling:
                return 0

        return result * sign


class TestSolution:
    def test_case_01(self):
        actual = Solution().reverse(123)
        expected = 321
        assert actual == expected
