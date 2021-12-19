# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        def preorder(node: Node):
            if node is None:
                return ['None']

            ret = [str(node.val)]
            for child in node.children:
                ret.append(preorder(child))
            return ','.join(ret)

    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        split_data = data.split(',')
        if not split_data:
            return None
        return None

    # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
