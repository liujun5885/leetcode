object CheckIfAStringContainsAllBinaryCodesOfSizeK {
    def hasAllCodes(s: String, k: Int): Boolean = {
        var subStringSet = Set[String]()
        for (i <- 0 to s.length - k) {
            subStringSet += s.substring(i, i + k)
        }
        subStringSet.size == math.pow(2, k).toInt
    }
}
