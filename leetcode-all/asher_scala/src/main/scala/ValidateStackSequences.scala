import scala.collection.mutable

object ValidateStackSequences {
    def validateStackSequences(pushed: Array[Int], popped: Array[Int]): Boolean = {
        //         val popped = Array(4, 5, 3, 2, 1)
        //         val pushed = Array(1, 2, 3, 4, 5)
        val ints = mutable.Stack[Int]()
        var j = 0

        for (i <- popped) {
            if (ints.isEmpty || ints.top != i) {
                while (j < pushed.length && pushed(j) != i) {
                    ints.push(pushed(j))
                    j += 1
                }
                if (j == pushed.length) {
                    return false
                }
                else {
                    j += 1
                }
            } else {
                ints.pop()
            }
        }

        ints.isEmpty
    }
}
