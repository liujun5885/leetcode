object CoinChange {
    def coinChange(coins: Array[Int], amount: Int): Int = {
        val dp = Array.fill[Int](amount + 1)(amount + 1)
        dp(0) = 0
        for (i <- coins) {
            for (j <- i to amount) {
                dp(j) = math.min(dp(j - i) + 1, dp(j))
            }
        }
        if (dp(amount) == amount + 1) -1 else dp(amount)
    }
}
