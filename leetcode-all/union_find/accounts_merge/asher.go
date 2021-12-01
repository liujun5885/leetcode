package main

import (
	"fmt"
	"sort"
)
import "github.com/google/go-cmp/cmp"

func find(uf []int, id int) int {
	if uf[id] == id {
		return id
	}
	uf[id] = find(uf, uf[id])
	return uf[id]
}

func union(uf []int, x, y int) bool {
	rootX := find(uf, x)
	rootY := find(uf, y)
	if rootX != rootY {
		uf[rootY] = rootX
		return true
	}
	return false
}

func accountsMerge(accounts [][]string) [][]string {
	emailIndex := 0
	emailVsIndex := make(map[string]int)
	emailVsName := make(map[string]string)
	for i := 0; i < len(accounts); i++ {
		for j := 1; j < len(accounts[i]); j++ {
			if _, ok := emailVsIndex[accounts[i][j]]; ok {
				continue
			}
			emailVsIndex[accounts[i][j]] = emailIndex
			emailIndex++
			emailVsName[accounts[i][j]] = accounts[i][0]
		}
	}
	uf := make([]int, emailIndex)
	for i := 0; i < emailIndex; i++ {
		uf[i] = i
	}

	for i := 0; i < len(accounts); i++ {
		for j := 2; j < len(accounts[i]); j++ {
			union(uf, emailVsIndex[accounts[i][1]], emailVsIndex[accounts[i][j]])
		}
	}

	indexVsEmails := make(map[int][]string)
	for k, _ := range emailVsIndex {
		if _, ok := indexVsEmails[find(uf, emailVsIndex[k])]; ok {
			indexVsEmails[find(uf, emailVsIndex[k])] = append(indexVsEmails[find(uf, emailVsIndex[k])], k)
		} else {
			indexVsEmails[find(uf, emailVsIndex[k])] = []string{k}
		}
	}

	result := make([][]string, len(indexVsEmails))
	i := 0
	for _, emails := range indexVsEmails {
		sort.Strings(emails)
		result[i] = append([]string{emailVsName[emails[0]]}, emails...)
		i++
	}

	return result
}

func main() {
	input := [][]string{
		{"John", "john00@mail.com", "johnsmith@mail.com"},
		{"John", "johnnybravo@mail.com"},
		{"John", "john_newyork@mail.com", "johnsmith@mail.com"},
		{"Mary", "mary@mail.com"},
	}
	expected := [][]string{
		{"John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"},
		{"John", "johnnybravo@mail.com"},
		{"Mary", "mary@mail.com"},
	}
	output := accountsMerge(input)
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
