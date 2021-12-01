package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func dfs(digits string, cur int, numVsChar map[byte][]byte, seg []byte) []string {
	if cur == len(digits) {
		return append([]string(nil), string(seg))
	}
	var ret []string
	for _, c := range numVsChar[digits[cur]] {
		seg = append(seg, c)
		ret = append(ret, dfs(digits, cur+1, numVsChar, seg)...)
		seg = seg[:len(seg)-1]
	}
	return ret
}

func letterCombinations(digits string) []string {
	numVsChar := map[byte][]byte{
		'2': {'a', 'b', 'c'},
		'3': {'d', 'e', 'f'},
		'4': {'g', 'h', 'i'},
		'5': {'j', 'k', 'l'},
		'6': {'m', 'n', 'o'},
		'7': {'p', 'q', 'r', 's'},
		'8': {'t', 'u', 'v'},
		'9': {'w', 'x', 'y', 'z'},
	}
	if len(digits) == 0 {
		return []string{}
	}

	return dfs(digits, 0, numVsChar, nil)
}

func main() {
	digits := "23"
	output := letterCombinations(digits)
	expected := []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}

	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
