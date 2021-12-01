package main

func searchMatrix(matrix [][]int, target int) bool {
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == target {
				return true
			} else if matrix[i][j] > target {
				break
			}
		}
	}
	return false
}
