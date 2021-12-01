import org.scalatest.FunSuite

class TestDistributeCandies extends FunSuite {
    test("case1") {
        val candyType = Array(1, 1, 2, 2, 3, 3)
        val expected = 3
        assert(DistributeCandies.distributeCandies(candyType) === expected)
    }

    test("case2") {
        val candyType = Array(1, 1, 2, 3)
        val expected = 2
        assert(DistributeCandies.distributeCandies(candyType) === expected)
    }

    test("case3") {
        val candyType = Array(6, 6, 6, 6)
        val expected = 1
        assert(DistributeCandies.distributeCandies(candyType) === expected)
    }
}
