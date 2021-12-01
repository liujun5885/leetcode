from typing import List


class Solution:
    def overlaps(self, interval_1, interval_2):
        if interval_2[0] <= interval_1[1]:
            return True
        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]

        for item in intervals[1:]:
            if not self.overlaps(item, res[-1]):
                res.append(item)
            else:
                res[-1] = [res[-1][0], max(res[-1][1], item[1])]
        return res
