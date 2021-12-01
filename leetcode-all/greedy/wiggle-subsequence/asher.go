package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func wiggleMaxLength(nums []int) int {
	n := len(nums)
	if len(nums) < 2 {
		return n
	}
	up, down := 1, 1
	for i := 1; i < n; i++ {
		if nums[i]-nums[i-1] > 0 {
			up = down + 1
		} else if nums[i]-nums[i-1] < 0 {
			down = up + 1
		}
	}
	if down > up {
		return down
	} else {
		return up
	}
}

func main() {
	input := []int{1, 7, 4, 9, 2, 5}
	output := wiggleMaxLength(input)
	expected := 6
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	input = []int{1, 17, 5, 10, 13, 15, 10, 5, 16, 8}
	output = wiggleMaxLength(input)
	expected = 7
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	input = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	output = wiggleMaxLength(input)
	expected = 2
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
