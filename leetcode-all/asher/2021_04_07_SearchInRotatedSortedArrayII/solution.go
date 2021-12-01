package main

func search(nums []int, target int) bool {
	if len(nums) == 0 {
		return false
	}
	if target == nums[0] {
		return true
	} else if target < nums[0] {
		for i := len(nums) - 1; i >= 0 && nums[i] <= nums[0]; i -= 1 {
			if nums[i] == target {
				return true
			}
		}
	} else {
		for i := 0; i < len(nums) && nums[i] >= nums[0]; i += 1 {
			if nums[i] == target {
				return true
			}
		}
	}

	return false
}
