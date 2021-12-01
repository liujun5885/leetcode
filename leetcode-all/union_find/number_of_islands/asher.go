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

func numIslands(grid [][]byte) int {
	h := len(grid)
	l := len(grid[0])
	count := 0
	uf := make([]int, h*l)

	for i := 0; i < h; i++ {
		for j := 0; j < l; j++ {
			if grid[i][j] == '1' {
				uf[i*l+j] = i*l + j
				count += 1
			}
		}
	}

	for i := 0; i < h; i++ {
		for j := 0; j < l; j++ {
			if grid[i][j] == '1' {
				grid[i][j] = '0'
				if i-1 >= 0 && grid[i-1][j] == '1' {
					if union(uf, i*l+j, (i-1)*l+j) {
						count -= 1
					}
				}
				if i+1 < h && grid[i+1][j] == '1' {
					if union(uf, i*l+j, (i+1)*l+j) {
						count -= 1
					}
				}
				if j-1 >= 0 && grid[i][j-1] == '1' {
					if union(uf, i*l+j, i*l+j-1) {
						count -= 1
					}
				}
				if j+1 < l && grid[i][j+1] == '1' {
					if union(uf, i*l+j, i*l+j+1) {
						count -= 1
					}
				}
			}
		}
	}
	return count
}

func main() {
	input := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	}
	expected := 1
	output := numIslands(input)
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
