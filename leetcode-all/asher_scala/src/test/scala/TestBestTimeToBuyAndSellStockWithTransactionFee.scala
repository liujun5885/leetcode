import org.scalatest.FunSuite

class TestBestTimeToBuyAndSellStockWithTransactionFee extends FunSuite {
    test("case01") {
        val prices = Array(1, 3, 2, 8, 4, 9)
        val fee = 2
        val expected = 8
        assert(BestTimeToBuyAndSellStockWithTransactionFee.maxProfit(prices, fee) === expected)
    }

    test("case02") {
        val prices = Array(1, 3, 7, 5, 10, 3)
        val fee = 3
        val expected = 6
        assert(BestTimeToBuyAndSellStockWithTransactionFee.maxProfit(prices, fee) === expected)
    }
}
