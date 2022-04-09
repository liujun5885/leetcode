# https://leetcode-cn.com/problems/alien-dictionary/

from collections import defaultdict, deque
from typing import List, Dict
from unittest import TestCase


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        words = [*filter(lambda x: len(x) > 0, words)]
        if len(words) == 0:
            return ""
        elif len(words) == 1:  # if this is only one word, return all different chars by any order
            return ''.join(set(words[0]))

        def init_graph(word_list: List[str]) -> Dict[str, set]:
            graph = defaultdict(set)
            for i in range(len(word_list) - 1):
                w1, w2 = word_list[i], word_list[i + 1]
                n1, n2 = len(w1), len(w2)
                min_n = min(n1, n2)
                j = 0
                # find the first letter that w1[j] != w2[j]
                while j < min_n and w1[j] == w2[j]:
                    j += 1

                if n1 > j == n2:  # for example, w1 = abc, w2 = ab, it's illegal, so return empty
                    return {}

                if j < min_n:
                    graph[w1[j]].add(w2[j])
                if j == n1 <= n2 > 0:  # if w1 = ab, w2 = abc, then all vertexes have no adjacent vertexes.
                    graph[w1[j - 1]] = set([])
            return graph

        def calculate_indegree(word_list: List[str], graph: Dict[str, set]) -> dict[str, int]:
            indegree = {}
            # init indegree
            for w in word_list:
                for c in w:
                    indegree[c] = 0
            # calculate indegree for all chars
            for char_vert in graph.values():
                for c in char_vert:
                    indegree[c] += 1

            return indegree

        graph = init_graph(words)
        if not graph:
            return ""
        indegree = calculate_indegree(words, graph)
        q = deque()
        # put all vertexes whose indegree is 0 into queue
        for k, v in indegree.items():
            if v == 0:
                q.append(k)

        # topological sort
        ans = []
        while len(q) > 0:
            v = q.popleft()
            ans.append(v)

            for i in graph[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        if len(ans) < len(indegree):
            return ""

        return "".join(ans)


class TestCases(TestCase):
    def test_1(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        expected = "wertf"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_2(self):
        words = ["z", "x"]
        expected = "zx"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_3(self):
        words = ["z", "x", "z"]
        expected = ""
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_4(self):
        words = ["z", "z"]
        expected = "z"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_5(self):
        words = ["z", "x", "a", "zb", "zx"]
        expected = ""
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_6(self):
        words = ["wnlb"]
        expected = "wnlb"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)
