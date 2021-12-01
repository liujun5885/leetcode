package main

func kLengthApart(nums []int, k int) bool {
	pillar := -1
	for i := 0; i < len(nums); i++ {
		if nums[i] != 1 {
			continue
		}
		if pillar >= 0 && i-pillar-1 < k {
			return false
		}
		pillar = i
	}
	return true
}
