package main

import (
	"container/heap"
)

type Item struct {
	value    int // The value of the item; arbitrary.
	priority int // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	if pq[i].priority == pq[j].priority {
		return pq[i].value < pq[j].value
	}
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func getOneNum(ones []int) int {
	num := 0
	for i := 0; i < len(ones); i++ {
		if ones[i] == 1 {
			num++
		} else {
			break
		}
	}
	return num
}

func kWeakestRows(mat [][]int, k int) []int {
	pq := make(PriorityQueue, len(mat))
	for i := 0; i < len(mat); i++ {
		pq[i] = &Item{
			value:    i,
			priority: getOneNum(mat[i]),
			index:    i,
		}
	}
	heap.Init(&pq)
	var ret []int
	for i := 0; i < k; i++ {
		item := heap.Pop(&pq).(*Item)
		ret = append(ret, item.value)
	}
	return ret
}
