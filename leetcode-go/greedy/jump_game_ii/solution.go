// Package jump_game_ii https://leetcode-cn.com/problems/jump-game-ii/
package jump_game_ii

func findPrev(num []int, end int) int {
	for i := 0; i < len(num); i++ {
		if i+num[i] >= end {
			return i
		}
	}
	return 0
}

func jump(nums []int) int {
	end := len(nums) - 1
	step := 0

	for end > 0 {
		end = findPrev(nums, end)
		step++
	}

	return step
}
