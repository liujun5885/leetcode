package main

import "fmt"

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

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	uf := make([]int, n)
	count := n

	for i := 0; i < n; i++ {
		uf[i] = i
	}

	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if isConnected[i][j] == 1 {
				if union(uf, i, j) {
					count -= 1
				}
			}
		}
	}

	return count
}

func main() {
	input := [][]int{
		{1, 1, 0},
		{1, 1, 0},
		{0, 0, 1},
	}
	expected := 2
	output := findCircleNum(input)
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
