from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        def take_start(elem):
            return elem[0]

        intervals.sort(key=take_start)
        j = 0
        for interval in intervals[1:]:
            if interval[0] <= intervals[j][1]:
                intervals[j][1] = max(interval[1], intervals[j][1])
            else:
                j += 1
                intervals[j][0] = interval[0]
                intervals[j][1] = interval[1]
        return intervals[:j + 1]


if __name__ == '__main__':
    v = [[1, 4], [4, 5]]
    print(Solution().merge(v))
