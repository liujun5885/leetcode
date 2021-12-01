package main

import (
	"fmt"
)

func find(uf []int, id int) int {
	if uf[id] == id {
		return id
	}
	uf[id] = find(uf, uf[id])
	return uf[id]
}

func union(uf []int, x, y int) bool {
	rootX := find(uf, x)
	rootY := find(uf, y)
	if rootX != rootY {
		uf[rootY] = rootX
		return true
	}
	return false
}

func longestConsecutive(nums []int) int {
	uf := make([]int, len(nums))
	hashMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		uf[i] = i
		hashMap[nums[i]] = i
	}

	for k, v := range hashMap {
		if _, exist := hashMap[k+1]; exist {
			union(uf, v, hashMap[k+1])
		}
	}

	rootCount := make(map[int]int)
	max := 0
	// compress path
	for _, v := range hashMap {
		root := find(uf, v)
		if _, exist := rootCount[root]; exist {
			rootCount[root] += 1
		} else {
			rootCount[root] = 1
		}
		if rootCount[root] > max {
			max = rootCount[root]
		}
	}

	return max
}

func main() {
	nums := []int{100, 4, 200, 1, 3, 2}
	output := longestConsecutive(nums)
	expected := 4
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	nums = []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}
	output = longestConsecutive(nums)
	expected = 9
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
