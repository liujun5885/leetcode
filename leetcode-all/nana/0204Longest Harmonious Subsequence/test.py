class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #         nums_count = {}
        #         for num in nums:
        #             nums_count[num] = nums_count.get(num, 0) + 1

        #         result = 0
        #         for num in nums_count:
        #             count = nums_count[num]
        #             if nums_count.get(num+1):
        #                 result = max(result, count + nums_count[num+1])
        #         return result

        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        result = 0
        for num in nums_count:
            count = nums_count[num]
            if nums_count.get(num + 1):
                result = max(result, count + nums_count[num + 1])
        return result