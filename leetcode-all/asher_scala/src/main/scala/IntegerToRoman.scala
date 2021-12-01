object IntegerToRoman {
    def intToRoman(num: Int): String = {
        val romanMap = Map(
            1000 -> "M",
            500 -> "D",
            100 -> "C",
            50 -> "L",
            10 -> "X",
            5 -> "V",
            1 -> "I",
        )
        val romans = List(1000, 500, 100, 50, 10, 5, 1)
        var start = num
        var result = ""

        for (i <- romans.indices) {
            val p = romans(if (i % 2 == 0) i else i + 1)
            if (i > 0 && romans(i - 1) - (start - start % p) == p) {
                result += romanMap(p) + romanMap(romans(i - 1))
                start %= p
            }
            else {
                result += romanMap(romans(i)) * (start / romans(i))
                start %= romans(i)
            }
        }

        result
    }
}
