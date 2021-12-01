class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        LEN = len(A)
        if LEN < 3:
            return 0
        total = 0
        i = 2
        dp = [0] * LEN
        while i < LEN:
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                total = total + dp[i]
            i += 1
        return total

