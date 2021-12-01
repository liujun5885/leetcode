import org.scalatest.FunSuite

class TestAdvantageShuffle extends FunSuite {
    test("case01") {
        val A = Array(2, 7, 11, 15)
        val B = Array(1, 10, 4, 11)
        val expected = Array(2, 11, 7, 15)
        assert(AdvantageShuffle.advantageCount(A, B) === expected)
    }


    test("case02") {
        val A = Array(12, 24, 8, 32)
        val B = Array(13, 25, 32, 11)
        val expected = Array(24, 32, 8, 12)
        assert(AdvantageShuffle.advantageCount(A, B) === expected)
    }
}
