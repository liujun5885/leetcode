package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"sort"
)

func dfs(board [][]byte, visited [][]byte, i, j int, trie map[byte]interface{}, wordList *[]string) {
	if visited[i][j] == 1 {
		return
	}

	node, ok := trie[board[i][j]]
	if !ok {
		return
	}

	cur := node.(map[byte]interface{})
	if word, ok := cur['$']; ok {
		*wordList = append(*wordList, word.(string))
		delete(cur, '$')
	}

	visited[i][j] = 1

	if i < len(board)-1 {
		dfs(board, visited, i+1, j, cur, wordList)
	}
	if i > 0 {
		dfs(board, visited, i-1, j, cur, wordList)
	}
	if j < len(board[0])-1 {
		dfs(board, visited, i, j+1, cur, wordList)
	}
	if j > 0 {
		dfs(board, visited, i, j-1, cur, wordList)
	}
	visited[i][j] = 0
}

func findWords(board [][]byte, words []string) []string {

	trie := map[byte]interface{}{}
	wordList := make([]string, 0, len(words))
	visited := make([][]byte, len(board))
	for i := 0; i < len(board); i++ {
		visited[i] = make([]byte, len(board[0]))
	}
	for _, word := range words {
		node := trie
		for _, char := range word {
			if _, ok := node[byte(char)]; !ok {
				node[byte(char)] = map[byte]interface{}{}
			}
			node = node[byte(char)].(map[byte]interface{})
		}
		node['$'] = word
	}

	for m := 0; m < len(board); m++ {
		for n := 0; n < len(board[m]); n++ {
			dfs(board, visited, m, n, trie, &wordList)
		}
	}
	return wordList
}

func main() {
	board := [][]byte{
		{'o', 'a', 'a', 'n'},
		{'e', 't', 'a', 'e'},
		{'i', 'h', 'k', 'r'},
		{'i', 'f', 'l', 'v'},
	}
	word := []string{"oath", "pea", "eat", "rain"}
	output := findWords(board, word)
	expected := []string{"eat", "oath"}
	sort.Strings(output)
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
