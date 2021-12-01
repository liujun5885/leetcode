import scala.collection.mutable

object AverageOfLevelsInBinaryTree {

    class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
        var value: Int = _value
        var left: TreeNode = _left
        var right: TreeNode = _right
    }

    def traverseTree(root: TreeNode, level: Int, levelMap: mutable.Map[Int, Array[Int]]): Unit = {
        if (root == null) {
            return
        }
        if (!levelMap.contains(level)) {
            levelMap(level) = Array[Int](0, 0)
        }
        levelMap(level)(0) += root.value
        levelMap(level)(1) += 1

        traverseTree(root.left, level + 1, levelMap)
        traverseTree(root.right, level + 1, levelMap)
    }

    def averageOfLevels(root: TreeNode): Array[Double] = {
        val levelMap = mutable.Map[Int, Array[Int]]()
        traverseTree(root, 0, levelMap)
        val result = new Array[Double](levelMap.size)
        for ((k, v) <- levelMap) {
            result(k) = (v(0): Float) / v(1)
        }
        result
    }
}
