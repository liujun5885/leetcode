# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
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

        def preorder(node):
            if node is None:
                return ['None']
            return [node.val] + preorder(node.left) + preorder(node.right)

        return ','.join(map(str, preorder(root)))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.raw_data = data.split(",")
        if not self.raw_data:
            return None

        def builder():
            if not self.raw_data:
                return None

            cur = self.raw_data[0]
            self.raw_data = self.raw_data[1:]

            if cur == 'None':
                return None

            root = TreeNode(int(cur))
            root.left = builder()
            root.right = builder()
            return root

        return builder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
