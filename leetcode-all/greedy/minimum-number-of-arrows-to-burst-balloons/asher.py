from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        new_points = sorted(points, key=lambda x: x[1])
        count = 1
        start = new_points[0]
        for i in new_points:
            if i[0] <= start[1]:
                continue

            start = i
            count += 1

        return count


def test_case1():
    intervals = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected = 2
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected


def test_case2():
    intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected = 4
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected


def test_case3():
    intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expected = 2
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected


def test_case4():
    intervals = [[1, 2]]
    expected = 1
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected


def test_case5():
    intervals = [[2, 3], [2, 3]]
    expected = 1
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected


def test_case6():
    intervals = []
    expected = 0
    actual = Solution().findMinArrowShots(intervals)
    assert actual == expected
