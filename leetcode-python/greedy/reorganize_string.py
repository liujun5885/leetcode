from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = Counter(s)
        max_len = len(s)

        if any(map(lambda x: x[1] > (max_len + 1) // 2, s_counter.items())):
            return ""

        ans = []
        q = [(-i[1], i[0]) for i in s_counter.items()]
        heapq.heapify(q)
        while len(q) > 1:
            _, char1 = heapq.heappop(q)
            _, char2 = heapq.heappop(q)
            # print(char1, char2)
            ans.append(char1)
            ans.append(char2)
            s_counter[char1] -= 1
            s_counter[char2] -= 1
            if s_counter[char1] > 0:
                q.append((-s_counter[char1], char1))
            if s_counter[char2] > 0:
                q.append((-s_counter[char2], char2))
            heapq.heapify(q)
        if q:
            ans.append(q[0][1])

        return ''.join(ans)


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        s = "aab"
        actual = Solution().reorganizeString(s)
        expected = "aba"
        self.assertEqual(actual, expected)

    def test_case_02(self):
        s = "vvvlo"
        actual = Solution().reorganizeString(s)
        expected = "vlvov"
        self.assertEqual(actual, expected)
