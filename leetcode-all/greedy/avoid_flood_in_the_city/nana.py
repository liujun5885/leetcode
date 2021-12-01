from typing import List


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1 for _ in range(len(rains))]
        lake_water = {}
        tmp_cache = []
        for i, rain in enumerate(rains):
            if rain:
                res[i] = -1
                if rain not in lake_water:
                    lake_water[rain] = i
                else:
                    day = lake_water[rain]
                    lake_water[rain] = i
                    if tmp_cache:
                        left = 0
                        right = len(tmp_cache) - 1
                        while left < right:
                            mid = left + (right - left) // 2
                            if tmp_cache[mid] > day:
                                right = mid
                            else:
                                left = mid + 1
                        if tmp_cache[left] > day:
                            res[tmp_cache[left]] = rain
                            tmp_cache.remove(tmp_cache[left])
                        else:
                            return []
                    else:
                        return []
            else:
                tmp_cache.append(i)
        return res


if __name__ == '__main__':
    tc = ([1, 2, 3, 4], [1, 2, 0, 1, 2], [1, 3, 0, 0, 1, 3], [69, 0, 0, 0, 69], [10, 20, 30])
    for item in tc:
        t = Solution().avoidFlood(item)
        print(item, t)

