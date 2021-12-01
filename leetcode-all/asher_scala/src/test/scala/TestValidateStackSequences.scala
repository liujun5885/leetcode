import org.scalatest.FunSuite

class TestValidateStackSequences extends FunSuite {
    test("case1") {
        val pushed = Array(1, 2, 3, 4, 5)
        val popped = Array(4, 5, 3, 2, 1)
        assert(ValidateStackSequences.validateStackSequences(pushed, popped) === true)
    }

    test("case2") {
        val pushed = Array(1, 2, 3, 4, 5)
        val popped = Array(4, 3, 5, 1, 2)
        assert(ValidateStackSequences.validateStackSequences(pushed, popped) === false)
    }
}

