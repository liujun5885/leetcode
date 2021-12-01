class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['\0'] = {}
        res = []
        temp = []
        visited = [[0] * len(board[0]) for i in range(len(board))]

        def search(i, j, cur):
            char = board[i][j]
            if char not in cur:
                return
            temp.append(char)
            if '\0' in cur[char]:
                res.append(''.join(temp))
                cur[char].pop('\0')
            visited[i][j] = 1
            for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if x<0 or y<0 or x == len(board) or y == len(board[0]) or visited[x][y]:
                    continue
                search(x,y,cur[char])
            temp.pop()
            visited[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, trie)
        return res
