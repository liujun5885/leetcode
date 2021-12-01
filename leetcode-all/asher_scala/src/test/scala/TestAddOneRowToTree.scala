import org.scalatest.FunSuite

class TestAddOneRowToTree extends FunSuite {
    test("case1") {
        val root = new AddOneRowToTree.TreeNode(
            4, new AddOneRowToTree.TreeNode(
                2, new AddOneRowToTree.TreeNode(3), new AddOneRowToTree.TreeNode(1)
            ), new AddOneRowToTree.TreeNode(6, new AddOneRowToTree.TreeNode(5))
        )
        val expected = new AddOneRowToTree.TreeNode()
        assert(AddOneRowToTree.addOneRow(root, 1, 2) === expected)
    }
}
