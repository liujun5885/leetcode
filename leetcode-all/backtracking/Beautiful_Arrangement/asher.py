class Solution:
    count = 0

    def backtrace(self, arr, start):
        if start == len(arr):
            self.count += 1
            return
        for i in range(start, len(arr)):
            if arr[i] % (start + 1) != 0 and (start + 1) % arr[i] != 0:
                continue
            arr[i], arr[start] = arr[start], arr[i]
            self.backtrace(arr, start + 1)
            arr[i], arr[start] = arr[start], arr[i]

    def countArrangement(self, n: int) -> int:
        arr = [i + 1 for i in range(n)]
        self.backtrace(arr, 0)

        return self.count


def test_case01():
    n = 2
    expected = 2
    actual = Solution().countArrangement(n)
    assert expected == actual


def test_case02():
    n = 1
    expected = 1
    actual = Solution().countArrangement(n)
    assert expected == actual


def test_case03():
    n = 3
    expected = 3
    actual = Solution().countArrangement(n)
    assert expected == actual


if __name__ == '__main__':
    print(Solution().countArrangement(3))
