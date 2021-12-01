class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int len = A.length;
        if (len < 3) {
            return 0;
        }
        
        int total = 0;
        int[] dp = new int[len];
        
        for (int i = 2; i < len; i++) {
            if (A[i] - A[i-1] == A[i-1] - A[i-2]) {
                dp[i] = dp[i-1] + 1;
                total += dp[i];
            }
        }
        return total;
    }
}

