package main

import (
	"sort"
)

func findLHS(nums []int) int {
	result := 0
	mapping := map[int]int{}

	for i := 0; i < len(nums); i++ {
		mapping[nums[i]]++
	}

	keys := []int{}
	for k, _ := range mapping {
		keys = append(keys, k)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(keys)))

	for i := 0; i < len(keys)-1; i++ {
		if keys[i]-keys[i+1] == 1 {
			if mapping[keys[i]]+mapping[keys[i+1]] > result {
				result = mapping[keys[i]] + mapping[keys[i+1]]
			}
		}
	}
	return result
}
