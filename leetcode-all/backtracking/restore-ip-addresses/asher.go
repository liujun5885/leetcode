package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"strconv"
	"strings"
)

func bfs(s string, seg []string) []string {
	if s == "" && len(seg) == 4 {
		return []string{strings.Join(seg, ".")}
	}

	if len(s) == 0 || len(seg) > 4 {
		return []string{}
	}

	if s[0] == '0' {
		seg = append(seg, s[:1])
		return bfs(s[1:], seg)
	}

	var result []string

	for i := 0; i < len(s); i++ {
		num, _ := strconv.Atoi(s[:i+1])
		if num > 255 {
			break
		}
		seg = append(seg, s[:i+1])
		result = append(result, bfs(s[i+1:], seg)...)
		seg = seg[:len(seg)-1]
	}
	return result
}

func restoreIpAddresses(s string) []string {
	var seg []string
	return bfs(s, seg)
}

func main() {
	s := "25525511135"
	output := restoreIpAddresses(s)
	expected := []string{"255.255.11.135", "255.255.111.35"}

	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
