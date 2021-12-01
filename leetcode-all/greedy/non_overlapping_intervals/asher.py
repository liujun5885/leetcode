from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        new_intervals = sorted(intervals, key=lambda x: x[1])
        count = 0

        starter = new_intervals[0]
        for i in new_intervals[1:]:
            if i[0] < starter[1]:
                count += 1
                continue

            starter = i

        return count


def test_case1():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expected = 1
    actual = Solution().eraseOverlapIntervals(intervals)
    assert actual == expected


def test_case2():
    intervals = [[1, 2], [1, 2], [1, 2]]
    expected = 2
    actual = Solution().eraseOverlapIntervals(intervals)
    assert actual == expected


def test_case3():
    intervals = [[1, 2], [2, 3]]
    expected = 0
    actual = Solution().eraseOverlapIntervals(intervals)
    assert actual == expected


def test_case4():
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    expected = 2
    actual = Solution().eraseOverlapIntervals(intervals)
    assert actual == expected
