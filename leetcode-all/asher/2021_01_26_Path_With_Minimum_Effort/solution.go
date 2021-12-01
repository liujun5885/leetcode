package main

import (
	"math"
)

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func dfs(heights [][]int, x int, y int, target int, visited *[][]bool) bool {
	(*visited)[x][y] = true
	if x == len(heights)-1 && y == len(heights[0])-1 {
		return true
	}
	directions := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	for _, d := range directions {
		x1 := x + d[0]
		y1 := y + d[1]
		if x1 >= 0 && x1 < len(heights) && y1 >= 0 && y1 < len(heights[0]) &&
			!(*visited)[x1][y1] && abs(heights[x][y]-heights[x1][y1]) <= target {
			if dfs(heights, x1, y1, target, visited) {
				return true
			}
		}
	}
	return false
}

func minimumEffortPath(heights [][]int) int {
	if len(heights) == 0 || (len(heights) == 1 && len(heights[0]) == 1) {
		return 0
	}
	directions := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	min, max := math.MaxInt32, 0

	for i := 0; i < len(heights); i++ {
		for j := 0; j < len(heights[i]); j++ {
			for _, d := range directions {
				x1, y1 := i+d[0], j+d[1]
				if x1 >= 0 && x1 < len(heights) && y1 >= 0 && y1 < len(heights[0]) {
					absV := abs(heights[i][j] - heights[x1][y1])
					if max < absV {
						max = absV
					}
					if min > absV {
						min = absV
					}
				}
			}
		}
	}

	for min < max {
		middle := (max + min) / 2

		visited := make([][]bool, len(heights))
		for i := 0; i < len(heights); i++ {
			visited[i] = make([]bool, len(heights[i]))
		}

		if dfs(heights, 0, 0, middle, &visited) {
			max = middle
		} else {
			min = middle + 1
		}
	}

	return min
}
