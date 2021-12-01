# Copyright (c) 2020 App Annie Inc. All rights reserved.
from typing import List


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
    def offset(self, x, y):
        return self.n * x + y

    def coordinate(self, i):
        return divmod(i, self.n)

    def numIslands2(self, m, n, positions: List[List[int]]):
        self.m = m
        self.n = n
        count = 0
        grid = [[0] * n for i in range(m)]
        us = UnionSet(m * n)
        res = []
        for x, y in positions:
            merged = 0
            if grid[x][y]:
                res.append(count)
                continue
            grid[x][y] = 1
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if i < 0 or i >= m or j < 0 or j >= n:
                    continue
                if grid[i][j] == 0:
                    continue
                merged += us.union(self.offset(x, y), self.offset(i, j))
            count = count + 1 - merged
            res.append(count)
        return res


Solution().numIslands(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
