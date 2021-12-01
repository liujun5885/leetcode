class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:    
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        land_count = sum([grid[i][j] == '1' for j in range(col) for i in range(row)])
        uf = UnionFind(row * col, land_count)
        # print(f'originally, uf.parent is {uf.parent}')
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                idx = i * col + j
                if i < row - 1 and grid[i + 1][j] == '1':
                    uf.union(idx, idx + col)
                if j < col - 1 and grid[i][j + 1] == '1':
                    uf.union(idx, idx + 1)
        return uf.land_count
    
class UnionFind:
    def __init__(self, size, count):
        self.parent = [i for i in range(size)]
        self.land_count = count
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        for i in range(len(self.parent)):
            if self.parent[i] == py:
                self.parent[i] = px
        self.land_count -= 1
    
    def find(self, x):
        # find x with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
