from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        i = 0
        for element in intervals[1:]:
            if element[1] < result[i][1]:
                continue
            elif element[0] <= result[i][1] <= element[1]:
                result[i][1] = element[1]
            else:
                result.append(element)
                i += 1

        return result


def test_case1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    actual = Solution().merge(intervals)
    assert actual == expected


def test_case2():
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    actual = Solution().merge(intervals)
    assert actual == expected
