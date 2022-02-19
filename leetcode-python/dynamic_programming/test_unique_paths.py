class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class TestSolution:
    def test_case01(self):
        m = 3
        n = 7
        expected = 28
        actual = Solution().uniquePaths(m, n)
        assert actual == expected

    def test_case02(self):
        m = 3
        n = 3
        expected = 6
        actual = Solution().uniquePaths(m, n)
        assert actual == expected

    def test_case03(self):
        m = 1
        n = 4
        expected = 1
        actual = Solution().uniquePaths(m, n)
        assert actual == expected

    def test_case04(self):
        m = 23
        n = 12
        expected = 193536720
        actual = Solution().uniquePaths(m, n)
        assert actual == expected
