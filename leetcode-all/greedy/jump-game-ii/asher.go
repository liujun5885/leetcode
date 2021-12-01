package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

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

func main() {
	input := []int{2, 3, 1, 1, 4}
	output := jump(input)
	expected := 2
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
