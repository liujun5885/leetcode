import org.scalatest.FunSuite

class TestCheckIfAStringContainsAllBinaryCodesOfSizeK extends FunSuite {
    test("case01") {
        val s = "00110110"
        val k = 2
        val expected = true
        assert(CheckIfAStringContainsAllBinaryCodesOfSizeK.hasAllCodes(s, k) === expected)
    }
    test("case02") {
        val s = "00110"
        val k = 2
        val expected = true
        assert(CheckIfAStringContainsAllBinaryCodesOfSizeK.hasAllCodes(s, k) === expected)
    }
}
