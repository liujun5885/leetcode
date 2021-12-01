import org.scalatest.FunSuite

class TestShortestUnsortedContinuousSubarray extends FunSuite {
  test("case1") {
    val nums = Array(2, 6, 4, 8, 10, 9, 15)
    assert(ShortestUnsortedContinuousSubarray.findUnsortedSubarray(nums) === 5)
  }
  test("case2") {
    val nums = Array(1, 2, 3, 4)
    assert(ShortestUnsortedContinuousSubarray.findUnsortedSubarray(nums) === 0)
  }
  test("case3") {
    val nums = Array(1)
    assert(ShortestUnsortedContinuousSubarray.findUnsortedSubarray(nums) === 0)
  }
}
