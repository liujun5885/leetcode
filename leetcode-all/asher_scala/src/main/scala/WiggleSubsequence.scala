object WiggleSubsequence {
    def wiggleMaxLength(nums: Array[Int]): Int = {
        if (nums.isEmpty) {
            return 0
        }
        if (nums.length < 3) {
            return 1
        }
        var diff = nums(1) - nums(0)
        var max = if (diff == 0) 0 else 1
        for (i <- 2 until nums.length) {
            if (diff != 0 && diff * (nums(i) - nums(i - 1)) < 0) {
                max += 1
            } else if (diff == 0 && nums(i) - nums(i - 1) != 0) {
                max += 1
            }
            diff = nums(i) - nums(i - 1)
        }
        max + 1
    }
}
