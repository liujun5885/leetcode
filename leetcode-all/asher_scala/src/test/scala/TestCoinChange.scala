import org.scalatest.FunSuite

class TestCoinChange extends FunSuite {
    test("case01") {
        val coins = Array[Int](186, 419, 83, 408)
        val amount = 6249
        val expected = 20
        assert(CoinChange.coinChange(coins, amount) === expected)
    }
}
