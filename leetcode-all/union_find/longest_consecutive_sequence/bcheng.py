class UnionSet:
    def __init__(self, size):
        self.parents = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        parent = self.parents[i]
        if parent == i:
            return i
        root = self.find(parent)
        self.parents[i] = root
        self.rank[root] = self.rank[i] + 1
        return root

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return 0
        if self.rank[root_i] <= self.rank[root_j]:
            new_root = root_i
            new_child = root_j
        else:
            new_root, new_child = root_j, root_i
        self.parents[new_child] = new_root
        self.rank[new_root] = self.rank[new_child] + 1
        return 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        us = UnionSet(len(nums))
        mapping = {v:i for i,v in enumerate(nums)}
        for i, v in enumerate(nums):
            j = mapping.get(v-1)
            if j is not None:
                us.union(i,j)
            j = mapping.get(v+1)
            if j is not None:
                us.union(i,j)
        seqs = {}
        for i in range(len(nums)):
            root = us.find(i)
            if root not in seqs:
                seqs[root] = set()
            seqs[root].add(nums[i])
        res = 0
        for v in seqs.values():
            if len(v)>res:
                res = len(v)
        return res
