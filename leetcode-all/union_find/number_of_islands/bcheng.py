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
            return
        if self.rank[root_i] <= self.rank[root_j]:
            new_root = root_i
            new_child = root_j
        else:
            new_root, new_child = root_j, root_i
        self.parents[new_child] = new_root
        self.rank[new_root] = self.rank[new_child] + 1


class Solution:
    def offset(self, x, y):
        return self.n * x + y

    def coordinate(self, i):
        return divmod(i, self.n)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = m = len(grid)
        self.n = n = len(grid[0])
        us = UnionSet(m * n)
        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                if value == '0':
                    continue
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if i < 0 or i >= m or j < 0 or j >= n:
                        continue
                    if grid[i][j] == '0':
                        continue
                    us.union(self.offset(x, y), self.offset(i, j))
        count = 0
        for i, v in enumerate(us.parents):
            if i == v:
                x, y = self.coordinate(i)
                if grid[x][y] == '1':
                    count += 1
        return count
