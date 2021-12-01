package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"math"
)

func minOperations(nums []int, x int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum < x {
		return -1
	}
	diff := sum - x

	windowSum := 0
	min := len(nums) + 1

	for left, right := 0, 0; right < len(nums); right++ {
		windowSum += nums[right]
		for ; windowSum > diff; left++ {
			windowSum -= nums[left]
		}

		if windowSum == diff {
			min = int(math.Min(float64(min), float64(len(nums)-right+left-1)))
		}
	}

	if min == len(nums)+1 {
		return -1
	} else {
		return min
	}
}

func main() {
	nums := []int{1, 1, 4, 2, 3}
	x := 5
	output := minOperations(nums, x)
	expected := 2
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
