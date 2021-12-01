package main

import (
	"fmt"
	"math"
	"sort"
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

func minimumEffortPath(heights [][]int) int {
	h := len(heights)
	w := len(heights[0])

	edges := make([][]int, (w-1)*h+(h-1)*w)
	uf := make([]int, h*w)
	edgesCount := 0
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			index := i*w + j
			uf[index] = index
			if j < w-1 {
				edges[edgesCount] = []int{index, index + 1, int(math.Abs(float64(heights[i][j]) - float64(heights[i][j+1])))}
				edgesCount++
			}
			if i < h-1 {
				edges[edgesCount] = []int{index, index + w, int(math.Abs(float64(heights[i][j]) - float64(heights[i+1][j])))}
				edgesCount++
			}
		}
	}
	sort.SliceStable(edges, func(i, j int) bool {
		return edges[i][2] < edges[j][2]
	})
	for i := 0; i < edgesCount; i++ {
		union(uf, edges[i][0], edges[i][1])
		rootX := find(uf, 0)
		rootY := find(uf, h*w-1)
		if rootX == rootY {
			return edges[i][2]
		}
	}

	return 0
}

func main() {
	input := [][]int{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}
	output := minimumEffortPath(input)
	expected := 2
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
