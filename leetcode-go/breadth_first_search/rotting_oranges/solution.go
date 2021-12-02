// Package rotting_oranges https://leetcode-cn.com/problems/rotting-oranges/
package rotting_oranges

func orangesRotting(grid [][]int) int {
	var stack [][]int
	orangesNum := 0
	ans := 0
	m := len(grid)
	n := len(grid[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				stack = append(stack, []int{i, j})
				orangesNum += 1
			} else if grid[i][j] == 1 {
				orangesNum += 1
			}
		}
	}

	for i := 0; i < len(stack); {
		curLength := len(stack)
		for ; i < curLength; i++ {
			r, c := stack[i][0], stack[i][1]
			// up
			if r-1 >= 0 && grid[r-1][c] == 1 {
				stack = append(stack, []int{r - 1, c})
				grid[r-1][c] = 2
			}
			// left
			if c-1 >= 0 && grid[r][c-1] == 1 {
				stack = append(stack, []int{r, c - 1})
				grid[r][c-1] = 2
			}
			// down
			if r+1 < m && grid[r+1][c] == 1 {
				stack = append(stack, []int{r + 1, c})
				grid[r+1][c] = 2
			}
			// right
			if c+1 < n && grid[r][c+1] == 1 {
				stack = append(stack, []int{r, c + 1})
				grid[r][c+1] = 2
			}
		}

		ans += 1
	}
	if orangesNum == len(stack) {
		if ans == 0 {
			return ans
		} else {
			return ans - 1
		}
	}
	return -1
}
