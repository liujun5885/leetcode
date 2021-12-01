object _3SumWithMultiplicity {
    def threeSumMulti(arr: Array[Int], target: Int): Int = {
        var output = 0
        for (i <- 0 until arr.length - 2) {
            for (j <- i + 1 until arr.length - 1) {
                for (k <- j + 1 until arr.length) {
                    if (arr(i) + arr(j) + arr(k) == target) {
                        output += 1
                    }
                }
            }
        }
        output % (math.pow(10, 9).toInt + 7)
    }
}
