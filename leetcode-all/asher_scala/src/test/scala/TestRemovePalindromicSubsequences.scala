import org.scalatest.FunSuite

class TestRemovePalindromicSubsequences extends FunSuite {
    test("case1") {
        val s = "ababa"
        val expected = 1
        assert(RemovePalindromicSubsequences.removePalindromeSub(s) === expected)
    }
    test("case2") {
        val s = "abb"
        val expected = 2
        assert(RemovePalindromicSubsequences.removePalindromeSub(s) === expected)
    }
    test("case3") {
        val s = "baabb"
        val expected = 2
        assert(RemovePalindromicSubsequences.removePalindromeSub(s) === expected)
    }
    test("case4") {
        val s = "bbaabaaa"
        val expected = 2
        assert(RemovePalindromicSubsequences.removePalindromeSub(s) === expected)
    }
}
