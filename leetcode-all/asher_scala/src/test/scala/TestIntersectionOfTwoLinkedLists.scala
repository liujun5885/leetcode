import org.scalatest.FunSuite

class TestIntersectionOfTwoLinkedLists extends FunSuite {
    test("case1") {
        val rootA = new IntersectionOfTwoLinkedLists.ListNode(1)
        val expected = rootA
        assert(IntersectionOfTwoLinkedLists.getIntersectionNode(rootA, rootA) === expected)
    }
}
