import sys


class Solution():
    dp_table = {}

    def superEggDrop(self, K, N):
        if N == 0: return 0
        if K == 1: return N
        result = sys.maxsize
        start = 1
        end = N
        if (K, N) in self.dp_table:
            return self.dp_table[(K, N)]
        while start <= end:
            middle = (start + end) // 2
            broken = self.superEggDrop(K - 1, middle - 1)
            not_broken = self.superEggDrop(K, N - middle)

            if broken > not_broken:
                end = middle - 1
            else:
                start = middle + 1

            result = min(result, max(not_broken, broken) + 1)

        self.dp_table[(K, N)] = result
        return result


def test_case1():
    K = 1
    N = 2
    expected = 2
    actual = Solution().superEggDrop(K, N)
    assert actual == expected


def test_case2():
    K = 2
    N = 6
    expected = 3
    actual = Solution().superEggDrop(K, N)
    assert actual == expected


def test_case3():
    K = 3
    N = 14
    expected = 4
    actual = Solution().superEggDrop(K, N)
    assert actual == expected
