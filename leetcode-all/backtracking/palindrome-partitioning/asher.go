package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func dfs(s string, start, end int, seg []string, isPalindrome [][]bool) [][]string {
	if start == end {
		return [][]string{append([]string{}, seg...)}
	}
	var res [][]string
	for i := start + 1; i < end+1; i++ {
		if isPalindrome[start][i-1] {
			seg = append(seg, s[start:i])
			ret := dfs(s, i, end, seg, isPalindrome)
			res = append(res, ret...)
			seg = seg[:len(seg)-1]
		}
	}
	return res
}

func partition(s string) [][]string {
	var seg []string
	isPalindrome := make([][]bool, len(s))
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, len(s))
		for j := range isPalindrome[i] {
			isPalindrome[i][j] = true
		}
	}
	for i := len(s) - 1; i >= 0; i-- {
		for j := i + 1; j < len(s); j++ {
			isPalindrome[i][j] = s[i] == s[j] && isPalindrome[i+1][j-1]
		}
	}

	return dfs(s, 0, len(s), seg, isPalindrome)
}

func main() {
	s := "aab"
	output := partition(s)
	expected := [][]string{{"a", "a", "b"}, {"aa", "b"}}

	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
