package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)

	for i := 0; i < n; i++ {
		can := gas[i] - cost[i]
		if can < 0 {
			continue
		}
		j := (i + 1) % n
		for ; j != i; j = (j + 1) % n {
			can += gas[j] - cost[j]
			if can < 0 {
				break
			}
		}
		if j == i {
			return i
		}
	}

	return -1
}

func main() {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	output := canCompleteCircuit(gas, cost)
	expected := 3
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
