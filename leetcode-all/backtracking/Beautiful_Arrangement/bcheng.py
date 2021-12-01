# Copyright (c) 2020 App Annie Inc. All rights reserved.
class Solution:
    def deep_search(self, current):
        if current > self.n:
            self.res += 1
            return
        for i in range(1, self.n + 1):
            if self.visited[i - 1]:
                continue
            if current % i == 0 or i % current == 0:
                self.visited[i - 1] = True
                self.deep_search(current + 1)
                self.visited[i - 1] = False

    def countArrangement(self, n: int) -> int:
        self.n = n
        self.res = 0
        self.visited = [False] * n
        self.deep_search(1)
        return self.res
