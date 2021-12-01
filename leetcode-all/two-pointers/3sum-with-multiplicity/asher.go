package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func threeSumMulti(arr []int, target int) int {

	numVsIndex := map[int][]int{}
	for i := 0; i < len(arr); i++ {
		if _, ok := numVsIndex[arr[i]]; ok {
			numVsIndex[arr[i]] = append(numVsIndex[arr[i]], i)
		} else {
			numVsIndex[arr[i]] = []int{i}
		}
	}
	nums := make([]int, len(numVsIndex))
	i := 0
	for k, _ := range numVsIndex {
		nums[i] = k
		i++
	}
	sort.Ints(nums)

	total := 0
	for i := 0; i < len(nums); i++ {
		for m, n := i, len(nums)-1; m <= n; {
			if nums[i]+nums[m]+nums[n] < target {
				m++
			} else if nums[i]+nums[m]+nums[n] > target {
				n--
			} else {
				if i != m && m != n {
					total += len(numVsIndex[nums[i]]) * len(numVsIndex[nums[m]]) * len(numVsIndex[nums[n]])
				} else if i != m && m == n {
					total += len(numVsIndex[nums[i]]) * len(numVsIndex[nums[m]]) * (len(numVsIndex[nums[m]]) - 1) / 2
				} else if i == m && m != n {
					total += len(numVsIndex[nums[i]]) * (len(numVsIndex[nums[i]]) - 1) * len(numVsIndex[nums[n]]) / 2
				} else {
					total += len(numVsIndex[nums[i]]) * (len(numVsIndex[nums[i]]) - 1) * (len(numVsIndex[nums[i]]) - 2) / 6
				}
				m++
				n--
			}
		}
	}
	return total
}

func main() {
	A := []int{2, 2, 2, 2}
	target := 6
	output := threeSumMulti(A, target)
	expected := 12
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
