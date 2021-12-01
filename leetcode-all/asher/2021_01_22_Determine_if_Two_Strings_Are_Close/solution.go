package main

import (
	"sort"
)

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	mapWord1 := map[int]int{}
	mapWord2 := map[int]int{}

	for i := 0; i < len(word1); i++ {
		mapWord1[int(word1[i])]++
		mapWord2[int(word2[i])]++
	}

	valueList1 := make([]int, 0, len(word1))
	valueList2 := make([]int, 0, len(word2))
	keyList1 := make([]int, 0, len(word1))
	keyList2 := make([]int, 0, len(word2))

	for k, v := range mapWord1 {
		keyList1 = append(keyList1, k)
		valueList1 = append(valueList1, v)
	}
	for k, v := range mapWord2 {
		keyList2 = append(keyList2, k)
		valueList2 = append(valueList2, v)
	}

	sort.Ints(valueList1)
	sort.Ints(valueList2)
	sort.Ints(keyList1)
	sort.Ints(keyList2)

	for i := 0; i < len(valueList1); i++ {
		if valueList1[i] != valueList2[i] || keyList1[i] != keyList2[i] {
			return false
		}
	}

	return true
}
