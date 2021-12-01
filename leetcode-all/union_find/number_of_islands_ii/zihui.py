from typing import List

class Solution:
    def generateIdx(self, r, c, n):
        return r * n + c

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.graph = [-1] * m * n
        self.lands = 0
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = []

        for r, c in positions:
            idx = self.generateIdx(r, c, n)
            if self.graph[idx] != -1:
                ans.append(self.lands)
                continue
            self.lands += 1
            self.graph[idx] = idx
            neighbors = [(r + rd, c + cd) for rd, cd in DIRECTIONS if 0 <= r + rd < m and 0 <= c + cd < n]
            for rd, cd in neighbors:
                nidx = self.generateIdx(rd, cd, n)
                if self.graph[nidx] != -1:
                    self.union(idx, nidx)
            ans.append(self.lands)
        return ans

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
        return self.graph[x]

    def union(self, x: tuple, y: tuple) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.graph[py] = px
        self.lands -= 1


if __name__ == '__main__':
    cases = [
        {'m': 3, 'n': 3, 'positions': [[0, 0], [0, 1], [1, 2], [2, 1]]},
        {'m': 1, 'n': 1, 'positions': [[0, 0]]},
        {'m': 1, 'n': 2, 'positions': [[0, 1], [0, 0]]},
        {'m': 2, 'n': 2, 'positions': [[0, 0], [1, 1], [0, 1]]},
        {'m': 4, 'n': 3, 'positions': [[1, 1], [0, 2], [2, 2], [1, 2]]},
        {'m': 3, 'n': 3, 'positions': [[0, 0], [0, 1], [1, 2], [1, 2]]},
    ]
    expected = [
        [1, 1, 2, 3],
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 2]
    ]
    for i in range(len(cases)):
        output = Solution().numIslands2(**cases[i])
        if not output == expected[i]:
            print(f'Case {i + 1} Failed. Output is {output}, expected is {expected[i]}')
        else:
            print(f'Case {i + 1} passed.')
