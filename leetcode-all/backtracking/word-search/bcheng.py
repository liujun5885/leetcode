# Copyright (c) 2020 App Annie Inc. All rights reserved.
class Solution:
    def check(self, i, j, k):
        if self.board[i][j] != self.word[k]:
            return False
        if k == self.ep:
            return True
        self.visited[i][j] = 1
        for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
            if x < 0 or y < 0 or x >= self.m or y >= self.n:
                continue
            if self.visited[x][y]:
                continue
            if self.check(x, y, k + 1):
                return True
        self.visited[i][j] = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.ep = len(word) - 1
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [([0] * self.n) for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.check(i, j, 0):
                    return True
        return False
