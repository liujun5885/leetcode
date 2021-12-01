package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
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

func numIslands2(m int, n int, positions [][]int) []int {
	count := 0
	uf := make([]int, m*n)
	grid := make([]int, m*n)
	output := []int{}

	for _, position := range positions {
		i := position[0]
		j := position[1]

		if grid[i*n+j] == 1 {
			output = append(output, count)
			continue
		}

		grid[i*n+j] = 1
		uf[i*n+j] = i*n + j
		count += 1
		if i-1 >= 0 && grid[(i-1)*n+j] == 1 {
			if union(uf, i*n+j, (i-1)*n+j) {
				count -= 1
			}
		}
		if i+1 < m && grid[(i+1)*n+j] == 1 {
			if union(uf, i*n+j, (i+1)*n+j) {
				count -= 1
			}
		}
		if j-1 >= 0 && grid[i*n+j-1] == 1 {
			if union(uf, i*n+j, i*n+j-1) {
				count -= 1
			}
		}
		if j+1 < n && grid[i*n+j+1] == 1 {
			if union(uf, i*n+j, i*n+j+1) {
				count -= 1
			}
		}
		output = append(output, count)
	}

	return output
}

func main() {
	m := 3
	n := 3
	positions := [][]int{
		{0, 0},
		{0, 1},
		{1, 2},
		{2, 1},
	}
	output := numIslands2(m, n, positions)
	fmt.Print(output)
	expected := []int{1, 1, 2, 3}
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
