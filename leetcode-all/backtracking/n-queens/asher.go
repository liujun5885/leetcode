package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func genString(board []int) []string {
	n := len(board)
	result := make([]string, n)
	for i := 0; i < n; i++ {
		row := make([]byte, n)
		for j := 0; j < n; j++ {
			row[j] = '.'
		}
		row[board[i]] = 'Q'
		result[i] = string(row)
	}
	return result
}

func backtrack(board []int, r int, columns, diagonals1, diagonals2 map[int]bool) [][]string {
	if r == len(board) {
		return [][]string{genString(board)}
	}

	result := [][]string{}

	for c := 0; c < len(board); c++ {
		if _, ok := columns[c]; ok {
			continue
		}
		if _, ok := diagonals1[c-r]; ok {
			continue
		}
		if _, ok := diagonals2[c+r]; ok {
			continue
		}
		columns[c] = true
		diagonals1[c-r] = true
		diagonals2[c+r] = true
		board[r] = c
		result = append(result, backtrack(board, r+1, columns, diagonals1, diagonals2)...)
		//board[r] = 0
		delete(columns, c)
		delete(diagonals1, c-r)
		delete(diagonals2, c+r)
	}
	return result
}

func solveNQueens(n int) [][]string {
	board := make([]int, n)
	columns := map[int]bool{}
	diagonals1 := map[int]bool{}
	diagonals2 := map[int]bool{}
	return backtrack(board, 0, columns, diagonals1, diagonals2)
}

func main() {
	n := 4
	output := solveNQueens(n)
	expected := [][]string{
		{".Q..", "...Q", "Q...", "..Q."},
		{"..Q.", "Q...", "...Q", ".Q.."},
	}
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
