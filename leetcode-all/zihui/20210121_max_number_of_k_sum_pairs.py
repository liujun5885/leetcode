class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        seen = set()
        ret = 0
        for val, cnt in d.items():
            diff = k - val
            if diff in seen:
                continue
            if diff == val:
                ret += cnt // 2
            else:
                ret += min(cnt, d.get(diff, 0))
                seen.add(val)
        return ret