class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.string = ''
        self.children_names_set = set()
    
    def setEnd(self):
        self.isEnd = True

    def resetIsEnd(self):
        self.isEnd = False

    def getChild(self, char: str) -> 'TrieNode':
        return self.children[self._getIndex(char)]

    def _getIndex(self, char: str) -> int:
        return ord(char) - ord('a')

    def setName(self, s):
        self.string = s


    def containsChild(self, k: str) -> bool:
        return k in self.children_names_set

    def recordChildName(self, name: str):
        return self.children_names_set.add(name)



class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.newRoot()
        self.keys = set()
    
    def newRoot(self):
        return TrieNode()
    
    def _getIndex(self, char: str) -> int:
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            idx = self._getIndex(c)
            if p.children[idx] is None:
                p.recordChildName(c)
                p.children[idx] = self.newRoot()
                p.children[idx].setName(c)
            p = p.children[idx]
        p.setEnd()

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            idx = self._getIndex(c)
            if p.children[idx] is None:
                return False
            p = p.children[idx]
        return p is not None and p.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            idx = self._getIndex(c)
            if not p.children[idx]:
                return False
            p = p.children[idx]
        return True
    
    def getChild(self, char: str) -> 'TrieNode':
        return self.root.children[self._getIndex(char)]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Use trie.
        1. insert all words into trie
        2. use backtracking to check if each word is in board
        """
        rows, cols = len(board), len(board[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        trie = Trie()
        for word in words:
            trie.insert(word)

        matched_words = []

        def backtracking(r, c, parent, curr_letter):
            letter = board[r][c]
            curr_letter += letter
            curr_node = parent.getChild(letter)
            # print(f'curr_node is {curr_node.string} end state is {curr_node.isEnd}')

            if curr_node is None:
                return
            # check if this is the end TrieNode; if yes, we reach the end of a matched word
            if curr_node.isEnd:
                matched_words.append(curr_letter)
                curr_node.resetIsEnd()
                
            visited[r][c] = True
            for i, j in DIRECTIONS:
                x, y = r + i, c + j
                if 0 <= x < rows and 0 <= y < cols and visited[x][y] is False:
                    # print(f'letter is {letter}, board[x][y] is {board[x][y]}')
                    if curr_node.containsChild(board[x][y]):
                        backtracking(x, y, curr_node, curr_letter)

            visited[r][c] = False
        
        for r in range(rows):
            for c in range(cols):
                if trie.startsWith(board[r][c]):
                    backtracking(r, c, trie, "")
        return matched_words
