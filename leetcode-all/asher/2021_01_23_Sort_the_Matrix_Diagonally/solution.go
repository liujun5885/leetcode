package solution

func diagonalSort(mat [][]int) [][]int {
	for x := 0; x < len(mat); x++ {
		for y := 0; y < len(mat[0]); y++ {
			for xStart, yStart := x, y; xStart > 0 && yStart > 0; xStart, yStart = xStart-1, yStart-1 {
				if mat[xStart][yStart] < mat[xStart-1][yStart-1] {
					mat[xStart][yStart], mat[xStart-1][yStart-1] = mat[xStart-1][yStart-1], mat[xStart][yStart]
				}
			}
		}
	}

	return mat
}
