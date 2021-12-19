# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def postorder(node):
            if node is None:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        return ",".join(map(str, postorder(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_int = [int(i) for i in data.split(",") if i]
        if not data_int:
            return None

        print(data_int)

        def builder(max_val, min_val):
            if not data_int or data_int[-1] > max_val or data_int[-1] < min_val:
                return None

            val = data_int.pop()
            root = TreeNode(val)
            root.right = builder(max_val, val)
            root.left = builder(val, min_val)
            return root

        return builder(max(data_int), min(data_int))
