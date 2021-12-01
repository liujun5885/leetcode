import org.scalatest.FunSuite

class TestIntegerToRoman extends FunSuite {
    test("case1") {
        val expected = "III"
        assert(IntegerToRoman.intToRoman(3) === expected)
    }

    test("case2") {
        val expected = "IV"
        assert(IntegerToRoman.intToRoman(4) === expected)
    }

    test("case3") {
        val expected = "IX"
        assert(IntegerToRoman.intToRoman(9) === expected)
    }

    test("case4") {
        val expected = "LVIII"
        assert(IntegerToRoman.intToRoman(58) === expected)
    }

    test("case5") {
        val expected = "MCMXCIV"
        assert(IntegerToRoman.intToRoman(1994) === expected)
    }
}
