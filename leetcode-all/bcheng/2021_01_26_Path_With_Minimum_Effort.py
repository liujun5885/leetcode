from collections import deque
from typing import List


class Solution:
    def under_limit(self, k):
        # print('k', k)
        q = deque(((0, 0),))
        seen = {(0, 0)}
        while q:
            i, j = q.popleft()
            # print(i, j)
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if -1 < x < self.m and -1 < y < self.n:
                    if -k <= self.h[i][j] - self.h[x][y] <= k:
                        if (x, y) == (self.m - 1, self.n - 1):
                            return True
                        if (x, y) not in seen:
                            seen.add((x, y))
                            q.append((x, y))
        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.h = heights
        self.m = len(heights)
        self.n = len(heights[0])
        if self.m+self.n==2:
            return 0
        l = 0
        h = 10 ** 6 + 1
        while l < h:
            k = (l + h) // 2
            if self.under_limit(k):
                h = k
            else:
                l = k+1
        return l
