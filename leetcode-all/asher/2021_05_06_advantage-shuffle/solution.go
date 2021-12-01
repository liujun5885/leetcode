package main

import (
	"sort"
)

func advantageCount(A []int, B []int) (ans []int) {
	sortedA := append([]int(nil), A...)
	sortedB := append([]int(nil), B...)

	advBs := map[int][]int{}
	dis := []int{}

	sort.Ints(sortedA)
	sort.Ints(sortedB)

	i := 0
	for _, v := range sortedA {
		if v > sortedB[i] {
			if _, ok := advBs[sortedB[i]]; ok {
				advBs[sortedB[i]] = append(advBs[sortedB[i]], v)
			} else {
				advBs[sortedB[i]] = []int{v}
			}
			i++
		} else {
			dis = append(dis, v)
		}
	}

	for _, b := range B {
		if v, ok := advBs[b]; ok {
			ans = append(ans, v[len(v)-1])
			if len(v) > 1 {
				advBs[b] = v[:len(v)-1]
			} else {
				delete(advBs, b)
			}
		} else {
			ans = append(ans, dis[len(dis)-1])
			dis = dis[:len(dis)-1]
		}
	}
	return
}
