package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func reconstructQueue(people [][]int) (result [][]int) {
	if len(people) < 2 {
		return people
	}
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] < people[j][0] {
			return true
		} else if people[i][0] > people[j][0] {
			return false
		} else {
			return people[i][1] < people[j][1]
		}
	})

	highVsCount := map[int]int{}
	for i := 0; i < len(people); i++ {
		if _, ok := highVsCount[people[i][0]]; ok {
			highVsCount[people[i][0]]++
		} else {
			highVsCount[people[i][0]] = 1
		}
	}

	for i := len(people) - 1; i >= 0; i-- {
		highVsCount[people[i][0]]--
		index := people[i][1] - highVsCount[people[i][0]]
		result = append(result[:index], append([][]int{people[i]}, result[index:]...)...)
	}
	return
}

func reconstructQueueII(people [][]int) (result [][]int) {
	if len(people) < 2 {
		return people
	}
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] > people[j][0] {
			return true
		} else if people[i][0] < people[j][0] {
			return false
		} else {
			return people[i][1] < people[j][1]
		}
	})

	for i := 0; i < len(people); i++ {
		if people[i][1] >= len(result) {
			result = append(result, people[i])
		} else {
			result = append(result[:people[i][1]], append([][]int{people[i]}, result[people[i][1]:]...)...)
		}
	}
	return
}

func main() {
	input := [][]int{{8, 2}, {4, 1}, {0, 3}, {3, 2}, {8, 1}, {4, 0}, {7, 0}, {6, 2}, {8, 0}, {4, 7}}

	output := reconstructQueueII(input)
	expected := [][]int{{4, 0}, {4, 1}, {3, 2}, {0, 3}, {7, 0}, {8, 0}, {6, 2}, {8, 1}, {8, 2}, {4, 7}}

	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
