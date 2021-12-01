package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func lowBit(num int) int {
	return num & -num
}

func Constructor(n int) []int {
	bit := make([]int, n+1)

	for i := 0; i < n; i++ {
		Update(bit, i, 0)
	}
	return bit
}

func Sum(bit []int, index int) int {
	total := 0

	for index += 1; index > 0; index -= lowBit(index) {
		total += bit[index]
	}

	return total
}

func Update(bit []int, index int, diff int) {
	for index = index + 1; index < len(bit); index += lowBit(index) {
		bit[index] += diff
	}
}

func countSmaller(nums []int) []int {
	numSet := map[int]bool{}
	for _, n := range nums {
		numSet[n] = true
	}

	deduplicatedNums := make([]int, len(numSet))
	i := 0
	for k, _ := range numSet {
		deduplicatedNums[i] = k
		i++
	}

	sort.Ints(deduplicatedNums)
	numVsIndex := map[int]int{}

	for i, v := range deduplicatedNums {
		numVsIndex[v] = i
	}

	bit := Constructor(len(numVsIndex))
	result := make([]int, len(nums))

	for i := len(nums) - 1; i >= 0; i-- {
		result[i] = Sum(bit, numVsIndex[nums[i]]-1)
		Update(bit, numVsIndex[nums[i]], 1)
	}

	return result
}

func main() {

	nums := []int{5, 2, 6, 1}
	output := countSmaller(nums)
	expected := []int{2, 1, 1, 0}
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
