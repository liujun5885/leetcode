object BestTimeToBuyAndSellStockWithTransactionFee {
    def maxProfit(prices: Array[Int], fee: Int): Int = {
        var buy = 5 * math.pow(10, 4).toInt
        var maxP = 0

        for (i <- prices) {
            if (i > buy) {
                maxP += i - buy
                buy = i
            } else if (i + fee < buy) {
                buy = i + fee
            }
        }
        maxP
    }
}
