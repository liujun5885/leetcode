object AdvantageShuffle {
    def advantageCount(A: Array[Int], B: Array[Int]): Array[Int] = {
        val C = new Array[Int](A.length)

        var maxSmaller = 0
        for (i <- A.indices) {
            if (A(i) <= B(i)) {
                maxSmaller += 1
            }
        }
        if (maxSmaller == 0) {
            return A
        }

        var ret = A.clone()

        var i = 1
        while (i < A.length) {
            if (C(i) < i) {
                val tmp = A(i)
                if ((i & 1) == 0) {
                    A(i) = A(0)
                    A(0) = tmp
                } else {
                    A(i) = A(C(i))
                    A(C(i)) = tmp
                }
                var ss = 0
                for (i <- A.indices) {
                    if (A(i) <= B(i)) {
                        ss += 1
                    }
                }
                if (ss == 0) {
                    return A
                } else if (ss < maxSmaller) {
                    ret = A.clone()
                    maxSmaller = ss
                }

                C(i) += 1
                i = 1
            } else {
                C(i) = 0
                i += 1
            }
        }

        ret
    }
}
