from typing import List


class Solution:
    def find_dry_pos(self, can_dry, pos):
        for n in can_dry:
            if n > pos:
                return n
        return None

    def avoidFlood(self, rains: List[int]) -> List[int]:
        rained = {}
        can_dry = []
        res = []
        for i, rain in enumerate(rains):
            if rain > 0:
                rain_pos = rained.get(rain, None)
                if rain_pos is not None:
                    dry_pos = self.find_dry_pos(can_dry, rain_pos)
                    if dry_pos is None:
                        return []
                    can_dry.remove(dry_pos)
                    res[dry_pos] = rain
                rained[rain] = i
                res.append(-1)
            else:
                res.append(1)
                can_dry.append(i)
        return res


if __name__ == '__main__':
    Solution().avoidFlood([69,0,0,0,69])
