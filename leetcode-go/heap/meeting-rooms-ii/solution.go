// Package meeting_rooms_ii https://leetcode-cn.com/problems/meeting-rooms-ii/
package meeting_rooms_ii

import (
	"container/heap"
	"sort"
)

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minMeetingRooms(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	h := &IntHeap{}
	for _, i := range intervals {
		if h.Len() == 0 {
			heap.Push(h, i[1])
			continue
		}
		if (*h)[0] <= i[0] {
			heap.Pop(h)
		}
		heap.Push(h, i[1])
	}
	return h.Len()
}
