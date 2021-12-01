# Copyright (c) 2020 App Annie Inc. All rights reserved.
from typing import List


class Solution:
    def __init__(self):
        self.free_days=[]

    def find_first_available_day(self, rain_day):
        for i in self.free_days:
            if i > rain_day:
                return i
        return None

    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry = {}
        free_days = self.free_days
        full_lakes = {}
        for i, r in enumerate(rains):
            if r == 0:
                free_days.append(i)
                continue
            if r not in full_lakes:
                full_lakes[r] = i
            else:
                available_day = self.find_first_available_day(full_lakes[r])
                if not available_day:
                    return []
                dry[available_day] = r
                full_lakes[r] = i
                free_days.remove(available_day)
        res = []
        for i, r in enumerate(rains):
            if r > 0:
                res.append(-1)
            elif i in dry:
                res.append(dry[i])
            else:
                res.append(1)
        return res

