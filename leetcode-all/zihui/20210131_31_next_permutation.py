class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = None
        for a in range(len(nums) - 1):
            if nums[a] < nums[a + 1]:
                i = a
        if i is None :
            nums[:] = nums[::-1]
            return
        for a in range(i + 1, len(nums)):
            if nums[a] > nums[i]:
                j = a
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return
