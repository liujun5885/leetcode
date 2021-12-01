package main

import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minimumDeviation(nums []int) int {
	min := 1000000000
	h := &IntHeap{}
	for _, num := range nums {
		if num%2 == 1 {
			num *= 2
		}
		heap.Push(h, num)
		if num < min {
			min = num
		}
	}

	result := 1000000000
	max := 0

	for max%2 == 0 {
		max = heap.Pop(h).(int)
		if max-min < result {
			result = max - min
		}
		if max%2 == 0 {
			k := max / 2
			heap.Push(h, k)
			if k < min {
				min = k
			}
		}
	}

	return result
}
