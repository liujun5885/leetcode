# Definition for a binary tree node.
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
    stack = []

    def travers(self, root, buffer):
        if root is None:
            return
        self.travers(root.left, buffer)
        buffer.append(root.val)
        self.travers(root.right, buffer)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        buffer = []
        self.travers(root, buffer)
        j = 0
        for i in buffer:
            if i is not None:
                j += 1
                if j == k:
                    return i


def test_case1():
    data_set = [3, 1, 4, None, 2]
    root = TreeNode.build(data_set)
    k = 1
    expected = 1
    actual = Solution().kthSmallest(root, k)
    assert actual == expected


def test_case2():
    data_set = [5, 3, 6, 2, 4, None, None, 1]
    root = TreeNode.build(data_set)
    k = 1
    expected = 1
    actual = Solution().kthSmallest(root, k)
    assert actual == expected


if __name__ == '__main__':
    data_set = [5, 3, 6, 2, 4, None, None, 1]
    root = TreeNode.build(data_set)
    TreeNode.print_tree(root)
