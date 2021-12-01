class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(data_set):
        stack = []
        for i in range(len(data_set)):
            node = TreeNode(data_set[i])
            parent_index = (i - 1) // 2
            position = (i - 1) % 2
            if parent_index >= 0:
                if position == 0:
                    stack[parent_index].left = node
                else:
                    stack[parent_index].right = node
            stack.append(node)

        return stack[0]

    @staticmethod
    def print_tree(root):
        if root is None:
            return
        TreeNode.print_tree(root.left)
        print(root.val)
        TreeNode.print_tree(root.right)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if root.val is None:
            return True

        if root.left is None:
            return True

        return root.left.value < root.val < root.left.value and self.isValidBST(root.left) and self.isValidBST(root.right)


def test_case1():
    data_set = [2, 1, 3]
    root = TreeNode.build(data_set)
    expected = True
    actual = Solution().isValidBST(root)
    assert actual == expected
