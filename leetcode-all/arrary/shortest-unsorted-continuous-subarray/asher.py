class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)

        i = 0
        j = len(nums) - 1

        while i < j:
            if sorted_nums[i] == nums[i]:
                i += 1
            if sorted_nums[j] == nums[j]:
                j -= 1

            if sorted_nums[i] != nums[i] and sorted_nums[j] != nums[j]:
                break

        if i == j:
            return 0
        else:
            return j - i + 1


def test_case1():
    nums = [2, 6, 4, 8, 10, 9, 15]
    expected = 5
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected


def test_case2():
    nums = [1, 2, 3, 4]
    expected = 0
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected


def test_case3():
    nums = [1]
    expected = 0
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected


def test_case4():
    nums = [1, 2, 3, 4, 5]
    expected = 0
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected


def test_case5():
    nums = [1, 3, 2, 4, 5]
    expected = 2
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected


def test_case6():
    nums = [2, 6, 4, 8, 10, 9, 15]
    expected = 5
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected
