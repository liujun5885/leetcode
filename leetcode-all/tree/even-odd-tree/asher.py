# Definition for a binary tree node.
from collections import defaultdict


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
    def __init__(self):
        self.buffer = defaultdict(list)

    def travers(self, root, level):
        if root is None:
            return
        self.travers(root.left, level + 1)
        if root.val:
            self.buffer[level].append(root.val)
        self.travers(root.right, level + 1)

    def validate_even(self, els):
        for i in range(len(els)):
            if els[i] % 2 != 1:
                return False
            if i > 0 and els[i] <= els[i - 1]:
                return False

        return True

    def validate_odd(self, els):
        for i in range(len(els)):
            if els[i] % 2 != 0:
                return False
            if i > 0 and els[i] >= els[i - 1]:
                return False
        return True

    def validate(self):
        for level, els in self.buffer.items():
            # even
            if level % 2 == 0:
                if not self.validate_even(els):
                    return False
            # odd
            else:
                if not self.validate_odd(els):
                    return False

        return True

    def isEvenOddTree(self, root: TreeNode) -> bool:
        self.travers(root, 0)
        return self.validate()


def test_case1():
    data_set = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
    root = TreeNode.build(data_set)
    expected = True
    actual = Solution().isEvenOddTree(root)
    assert actual == expected


def test_case2():
    data_set = [5, 4, 2, 3, 3, 7]
    root = TreeNode.build(data_set)
    expected = False
    actual = Solution().isEvenOddTree(root)
    assert actual == expected


def test_case3():
    data_set = [5, 9, 1, 3, 5, 7]
    root = TreeNode.build(data_set)
    expected = False
    actual = Solution().isEvenOddTree(root)
    assert actual == expected


def test_case4():
    data_set = [1]
    root = TreeNode.build(data_set)
    expected = True
    actual = Solution().isEvenOddTree(root)
    assert actual == expected


def test_case5():
    data_set = [11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17]
    root = TreeNode.build(data_set)
    expected = True
    actual = Solution().isEvenOddTree(root)
    assert actual == expected


def test_case6():
    data_set = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
    root = TreeNode.build(data_set)
    expected = True
    actual = Solution().isEvenOddTree(root)
    assert actual == expected
