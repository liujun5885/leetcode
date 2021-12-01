package solution

import (
	"math"
)

func mostCompetitive(nums []int, k int) []int {
	result := make([]int, 0, k)
	resultLen := 0

	for i, v := range nums {
		for resultLen > 0 && v < result[resultLen-1] && len(nums)-i+resultLen > k {
			resultLen--
		}
		result = result[:resultLen]
		result = append(result, v)
		resultLen++
	}

	return result[:k]
}

func mostCompetitive_v2(nums []int, k int) []int {
	result := make([]int, 0, k)
	min := math.MaxInt32
	minKey := 0

	for j := k; j > 0; j-- {
		for i := minKey; i <= len(nums)-j; i++ {
			if nums[i] < min {
				min = nums[i]
				minKey = i + 1
			}
		}
		result = append(result, min)
		min = math.MaxInt32
	}

	return result
}
