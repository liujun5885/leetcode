import javax.swing.tree.TreeNode

object AddOneRowToTree {

    class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
        var value: Int = _value
        var left: TreeNode = _left
        var right: TreeNode = _right
    }

    def addOneRow(root: TreeNode, v: Int, d: Int): TreeNode = {
        if (d == 1) {
            return new TreeNode(v, _left = root)
        }
        var q = Array[TreeNode](root)
        var l = 1

        while (q.nonEmpty && l < d) {
            var p = Array[TreeNode]()
            for (i <- q) {
                if (i.left != null) {
                    p = p :+ i.left
                }
                if (i.right != null) {
                    p = p :+ i.right
                }
                if (l == d - 1) {
                    val nl = new TreeNode(v, _left = i.left)
                    val nr = new TreeNode(v, _right = i.right)
                    i.left = nl
                    i.right = nr
                }
            }
            q = p
            l += 1
        }
        root
    }
}

object Solution {
    def wordSubsets(A: Array[String], B: Array[String]): List[String] = {
        val C = B.reduce((x, y) => if () {
            x.toSet + y.toSet
        } else {
            x.toSet + y.toSet
        })

        List()
    }

    def main(args: Array[String]): Unit = {
        val A = Array("amazon", "apple", "facebook", "google", "leetcode")
        val B = Array("lo", "eo")
        wordSubsets(A, B)
    }
}
