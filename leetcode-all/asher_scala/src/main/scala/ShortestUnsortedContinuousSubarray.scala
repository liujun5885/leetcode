import scala.util.control.Breaks._

object ShortestUnsortedContinuousSubarray extends App {
    def findUnsortedSubarray(nums: Array[Int]): Int = {
        val sortedNums = nums.sorted
        var start = 0;
        var end = 0;

        breakable {
            for (i <- 0 until nums.length) {
                if (sortedNums(i) != nums(i)) {
                    start = i
                    break
                }
            }
        }

        breakable {
            for (i <- nums.length - 1 to start by -1) {
                if (sortedNums(i) != nums(i)) {
                    end = i
                    break
                }
            }
        }

        if (end == start) {
            0
        } else {
            end - start + 1
        }
    }
}
