object MissingNumber {
    def missingNumber(nums: Array[Int]): Int = {
        nums.length * (nums.length + 1) / 2 - nums.sum
    }
}
