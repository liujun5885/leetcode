from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class TestSolution:
    def test_case01(self):
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = 2
        actual = Solution().uniquePathsWithObstacles(obstacleGrid)
        assert actual == expected

    def test_case02(self):
        obstacleGrid = [[0, 1], [0, 0]]
        expected = 1
        actual = Solution().uniquePathsWithObstacles(obstacleGrid)
        assert actual == expected

    def test_case03(self):
        obstacleGrid = [[0, 0]]
        expected = 1
        actual = Solution().uniquePathsWithObstacles(obstacleGrid)
        assert actual == expected
