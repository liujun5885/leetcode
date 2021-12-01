class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lens = len(nums)
        i=0
        while i<lens-1:
            if nums[i+1] < nums[i]:
                break
            i+=1
        if i == lens - 1:
            return 0
        j = lens-1
        while j>i:
            if nums[j] < nums[j-1]:
                break
            j-=1
        subarray = nums[i:j+1]
        min_ = min(subarray)
        max_ = max(subarray)
        k=0
        while k<i:
            if nums[k]>min_:
                i=k
                break
            k+=1
        k = lens - 1
        while k>j:
            if nums[k]<max_:
                j=k
                break
            k-=1
        return j-i+1