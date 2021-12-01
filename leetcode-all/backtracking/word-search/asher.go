package main

import "fmt"

func dfs(board [][]byte, visited [][]byte, i, j int, word string, wordIndex int) bool {
	if visited[i][j] == 1 {
		return false
	}
	if board[i][j] != word[wordIndex] {
		return false
	}
	if wordIndex == len(word)-1 {
		return true
	}
	visited[i][j] = 1
	result := false

	if i < len(board)-1 {
		result = result || dfs(board, visited, i+1, j, word, wordIndex+1)
	}
	if i > 0 {
		result = result || dfs(board, visited, i-1, j, word, wordIndex+1)
	}
	if j < len(board[0])-1 {
		result = result || dfs(board, visited, i, j+1, word, wordIndex+1)
	}
	if j > 0 {
		result = result || dfs(board, visited, i, j-1, word, wordIndex+1)
	}
	if result == false {
		visited[i][j] = 0
	}
	return result
}

func exist(board [][]byte, word string) bool {
	visited := make([][]byte, len(board))
	for i := 0; i < len(board); i++ {
		visited[i] = make([]byte, len(board[0]))
	}

	for m := 0; m < len(board); m++ {
		for n := 0; n < len(board[m]); n++ {
			for i := 0; i < len(board); i++ {
				visited[i] = make([]byte, len(board[0]))
			}
			result := dfs(board, visited, m, n, word, 0)
			if result {
				return result
			}
		}
	}
	return false
}

func main() {
	board := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
	word := "ABCCED"
	output := exist(board, word)
	expected := true
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	board = [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
	word = "ABCB"
	output = exist(board, word)
	expected = false
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	board = [][]byte{{'a', 'b'}, {'c', 'd'}}
	word = "cdba"
	output = exist(board, word)
	expected = true
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	board = [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'E', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	word = "ABCESEEEFS"
	output = exist(board, word)
	expected = true
	if output != expected {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
