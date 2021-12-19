from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        visited = [0] * numCourses
        valid = True

        for i in prerequisites:
            edges[i[1]].append(i[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid and visited[i] == 0:
                dfs(i)

        return valid
