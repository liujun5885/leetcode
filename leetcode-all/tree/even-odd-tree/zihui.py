class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level_cnt = 0
        curr_level = [root]
        next_level = []

        while curr_level:
            for i in range(len(curr_level)):
                node = curr_level[i]
                if node.val % 2 == level_cnt % 2:
                    return False
                if i > 0 and level_cnt % 2 == 0 and node.val <= curr_level[i - 1].val:
                    return False
                if i > 0 and level_cnt % 2 != 0 and node.val >= curr_level[i - 1].val:
                    return False
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            next_level = []
            level_cnt += 1
        return True
