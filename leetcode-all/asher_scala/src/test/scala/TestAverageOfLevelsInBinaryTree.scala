import org.scalatest.FunSuite

class TestAverageOfLevelsInBinaryTree extends FunSuite {
    test("case1") {
        val root = new AverageOfLevelsInBinaryTree.TreeNode(1)
        val expected = Array()
        assert(AverageOfLevelsInBinaryTree.averageOfLevels(root) === expected)
    }
}
