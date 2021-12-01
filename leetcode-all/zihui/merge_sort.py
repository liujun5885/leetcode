from typing import List


def merge_sort(nums: List[int]):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    nums = [1, 7, 0, 4, 3, 5, 6, 2]
    print(f'Originally, nums is {nums}')
    merge_sort(nums)
    assert nums == [0, 1, 2, 3, 4, 5, 6, 7]
    print(f'After sorting, nums becomes {nums}')

    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f'Originally, nums is {nums}')
    merge_sort(nums)
    assert nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'After sorting, nums becomes {nums}')