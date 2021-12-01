class Solution:

    def sumRight(self, nums, x):
        total = 0
        operation = 0
        for i in range(len(nums) - 1, -1, -1):
            if total > x:
                return -1
            elif total == x:
                return operation
            else:
                total += nums[i]
                operation += 1
        if total == x:
            return operation
        else:
            return 0

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        operation_list = []
        left_operation = 0
        left_total = 0

        for i in range(len(nums)):
            if left_total < x:
                right_operation = self.sumRight(nums[i:], x - left_total)
                if right_operation > 0:
                    operation_list.append(left_operation + right_operation)
            elif left_total == x:
                operation_list.append(left_operation)
                break
            else:
                break

            left_total += nums[i]
            left_operation += 1

        if not operation_list:
            return -1
        return min(operation_list)


def test_case1():
    nums = [1, 1, 4, 2, 3]
    x = 5
    expected = 2

    actual = Solution().minOperations(nums, x)
    assert actual == expected


def test_case2():
    nums = [5, 6, 7, 8, 9]
    x = 4
    expected = -1

    actual = Solution().minOperations(nums, x)
    assert actual == expected


def test_case3():
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    expected = 5

    actual = Solution().minOperations(nums, x)
    assert actual == expected


def test_case4():
    nums = [5, 2, 3, 1, 1]
    x = 5
    expected = 1
    actual = Solution().minOperations(nums, x)
    assert actual == expected


def test_case5():
    nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
    x = 134365
    expected = 16
    actual = Solution().minOperations(nums, x)
    assert actual == expected
