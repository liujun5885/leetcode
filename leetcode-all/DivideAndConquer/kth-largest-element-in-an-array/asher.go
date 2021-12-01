package kth_largest_element_in_an_array

import (
	"math/rand"
	"time"
)

func partition(nums []int, start, end int) int {
	if start == end {
		return start
	}
	r := rand.Int()%(end-start+1) + start
	x := nums[r]
	nums[end], nums[r] = nums[r], nums[end]

	p := start
	for i := start; i <= end; i++ {
		if nums[i] >= x {
			nums[p], nums[i] = nums[i], nums[p]
			p++
		}
	}

	return p - 1
}

func findKthLargest(nums []int, k int) int {
	start := 0
	end := len(nums) - 1
	rand.Seed(time.Now().UnixNano())
	cur := partition(nums, start, end)
	for ; cur != k-1; cur = partition(nums, start, end) {
		if cur < k-1 {
			start = cur + 1
		} else {
			end = cur - 1
		}
	}
	return nums[cur]
}
