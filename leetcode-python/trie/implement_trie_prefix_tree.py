# https://leetcode-cn.com/problems/implement-trie-prefix-tree/
from typing import Optional


class Trie:
    def __init__(self):
        self.children: list = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def search_prefix(self, prefix: str) -> Optional["Trie"]:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None


import unittest


class TestCases(unittest.TestCase):
    def test_01(self):
        methods = ["insert", "search", "search", "startsWith", "insert", "search"]
        params = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        results = [None, True, False, True, None, True]
        trie = Trie()
        for i in range(len(methods)):
            actual = getattr(trie, methods[i])(*params[i])
            expected = results[i]
            self.assertEqual(actual, expected)

    def test_02(self):
        methods = ["search", ]
        params = [["a"]]
        results = [False]
        trie = Trie()
        for i in range(len(methods)):
            actual = getattr(trie, methods[i])(*params[i])
            expected = results[i]
            self.assertEqual(actual, expected)
