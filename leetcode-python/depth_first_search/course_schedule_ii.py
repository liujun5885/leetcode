from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        visited = [0] * numCourses
        stack = []

        for i in prerequisites:
            edges[i[1]].append(i[0])

        def dfs(u) -> bool:
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    valid = dfs(v)
                    if not valid:
                        return False
                elif visited[v] == 1:
                    return False
            visited[u] = 2
            stack.append(u)
            return True

        valid = True
        for i in range(numCourses):
            if visited[i] == 0:
                valid = dfs(i)
                if not valid:
                    break

        if not valid:
            return []

        return stack[::-1]
