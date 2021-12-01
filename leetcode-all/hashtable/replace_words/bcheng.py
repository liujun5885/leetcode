# Copyright (c) 2020 App Annie Inc. All rights reserved.
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = SearchTree(dictionary)
        res = [tree.search_word(i) or i for i in sentence.split(' ')]
        return ' '.join(res)


class SearchTree:
    def __init__(self, dictionary):
        self.root = {}
        for i in dictionary:
            self.add_word(i)

    def add_word(self, word):
        cur = self.root
        for char in word:
            if char in cur:
                if not cur[char]:
                    return
            else:
                cur[char] = {}
            cur = cur[char]
        if cur:
            cur.clear()

    def search_word(self, word):
        cur = self.root
        m = []
        for char in word:
            if char not in cur:
                return False
            m.append(char)
            cur = cur[char]
            if not cur:
                return ''.join(m)
        return False


