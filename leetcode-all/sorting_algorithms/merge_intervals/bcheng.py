# Copyright (c) 2020 App Annie Inc. All rights reserved.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if cur[0] <= i[0] <= cur[1]:
                cur = [cur[0], max(i[1], cur[1])]
            else:
                res.append(cur)
                cur = i
        res.append(cur)
        return res
