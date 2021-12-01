import org.scalatest.FunSuite

class Test3SumWithMultiplicity extends FunSuite {
    test("case01") {
        val arr = Array(1, 1, 2, 2, 3, 3, 4, 4, 5, 5)
        val target = 8
        val expected = 20
        assert(_3SumWithMultiplicity.threeSumMulti(arr, target) === expected)
    }
}
