class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Union Find
        1. sort all edges in ascending order: (from_row, from_col, to_row, to_col, effort)
        2. union adjacent edges
        3. if (0,0) is connected with (m, n) where m = len(heights), n = len(heights[0]), we have found the minimum effort.
        4. note: while traversing edges, we only need to concern two directions: right and down, since connections are undirected in this context
        Time Complexity: O(NlogN)
        Space Complexity: O(N) , N = total elements in heightsTime Complexity: O(NlogN)
        """
        rows, cols = len(heights), len(heights[0])
        if rows < 2 and cols < 2:
            return 0
        
        start_point, end_point = (0, 0), (rows - 1, cols - 1)
        parent = {(r, c): (r, c) for r in range(rows) for c in range(cols)}
        # sorted edges, each edge -> (from_row, from_col, to_row, to_col, effort)
        edges = sorted(
                        [
                            (
                                r, c,
                                r + rd, c + cd,
                                abs(heights[r + rd][c + cd] - heights[r][c])
                            )
                            for r in range(rows)
                            for c in range(cols)
                            for rd, cd in [(1, 0), (0, 1)]
                            if 0 <= r + rd < rows and 0<= c + cd < cols
                        
                          ],
            key = lambda x: x[-1]
        )
        
        uf = UnionFind(parent)
        for edge in edges:
            fr, fc, tr, tc, effort = edge
            uf.union((fr, fc), (tr, tc))
            if uf.is_connected(start_point, end_point):
                return effort
        
        
class UnionFind:
    def __init__(self, parent):
        self.parent = parent
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        self.parent[py] = px
        
        
