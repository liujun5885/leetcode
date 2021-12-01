package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func permuteUnique(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	visited := make([]bool, n)
	row := make([]int, 0, n)

	var backtrace func(int)
	backtrace = func(start int) {
		if start == n {
			ans = append(ans, append([]int(nil), row...))
			return
		}

		for i, v := range nums {
			if visited[i] || (i > 0 && nums[i] == nums[i-1] && !visited[i-1]) {
				continue
			}
			visited[i] = true
			row = append(row, v)
			backtrace(start + 1)
			row = row[:len(row)-1]
			visited[i] = false
		}

	}
	backtrace(0)
	return
}

func main() {
	input := []int{1, 1, 2}
	output := permuteUnique(input)
	expected := [][]int{
		{1, 1, 2},
		{1, 2, 1},
		{2, 1, 1},
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
