package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func backtrace(s, p string, sIndex, pIndex int, memo map[int]bool) bool {
	index := sIndex*len(p) + pIndex

	if v, ok := memo[index]; ok {
		return v
	}

	if sIndex == len(s) {
		memo[index] = pIndex == len(p) || pIndex < len(p)-1 && p[pIndex+1] == '*' && backtrace(s, p, sIndex, pIndex+2, memo)
		return memo[index]
	}
	if pIndex == len(p) {
		return false
	}

	if s[sIndex] == p[pIndex] || p[pIndex] == '.' {
		if pIndex < len(p)-1 && p[pIndex+1] == '*' {
			memo[index] = backtrace(s, p, sIndex+1, pIndex, memo) || backtrace(s, p, sIndex+1, pIndex+2, memo) || backtrace(s, p, sIndex, pIndex+2, memo)
		} else {
			memo[index] = backtrace(s, p, sIndex+1, pIndex+1, memo)
		}
		return memo[index]
	} else {
		if pIndex < len(p)-1 && p[pIndex+1] == '*' {
			memo[index] = backtrace(s, p, sIndex, pIndex+2, memo)
		} else {
			memo[index] = false
		}
		return memo[index]
	}
}

func isMatch(s string, p string) bool {
	memo := map[int]bool{}
	return backtrace(s, p, 0, 0, memo)
}

func main() {
	s := "bbbba"
	p := ".*a*a"
	output := isMatch(s, p)
	expected := true
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	s = "aa"
	p = "a*"
	output = isMatch(s, p)
	expected = true
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	s = "ab"
	p = ".*"
	output = isMatch(s, p)
	expected = true
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	s = "aab"
	p = "c*a*b"
	output = isMatch(s, p)
	expected = true
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	s = "mississippi"
	p = "mis*is*p*."
	output = isMatch(s, p)
	expected = false
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
