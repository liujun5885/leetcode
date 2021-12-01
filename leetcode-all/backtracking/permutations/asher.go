package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func _permute(nums []int, start int) [][]int {
	if start == len(nums) {
		return [][]int{append([]int(nil), nums...)}
	}

	var result [][]int

	for i := start; i < len(nums); i++ {
		nums[i], nums[start] = nums[start], nums[i]
		result = append(result, _permute(nums, start+1)...)
		nums[i], nums[start] = nums[start], nums[i]
	}
	return result
}

func permute(nums []int) [][]int {
	return _permute(nums, 0)
}

func main() {
	input := []int{1, 2, 3}
	output := permute(input)
	expected := [][]int{
		{1, 2, 3},
		{1, 3, 2},
		{2, 1, 3},
		{2, 3, 1},
		{3, 1, 2},
		{3, 2, 1},
	}
	sort.Slice(output, func(i, j int) bool {
		for n := 0; n < len(output[i]); n++ {
			if output[i][n] < output[j][n] {
				return true
			} else if output[i][n] > output[j][n] {
				return false
			}
		}
		return true
	})
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
