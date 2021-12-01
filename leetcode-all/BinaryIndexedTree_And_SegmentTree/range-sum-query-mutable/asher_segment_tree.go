package main

import (
	"fmt"
	"math"
)

type STNumArray struct {
	nums        []int
	segmentTree []int
}

func STConstructor(nums []int) STNumArray {
	/*
		the length of segment tree is 2 * 2**⌈log2(n)⌉ - 1
	*/
	segmentTreeLen := 2*int(math.Pow(2, math.Ceil(math.Log2(float64(len(nums)))))) - 1
	arr := STNumArray{nums: append([]int(nil), nums...), segmentTree: make([]int, segmentTreeLen)}
	arr.Build(0, 0, len(nums)-1)
	return arr
}

func (this *STNumArray) Build(i, start, end int) {
	mid := (start + end) / 2
	left := 2*i + 1
	right := 2*i + 2

	if start == end {
		this.segmentTree[i] = this.nums[start]
		return
	}
	this.Build(left, start, mid)
	this.Build(right, mid+1, end)
	this.segmentTree[i] = this.segmentTree[left] + this.segmentTree[right]
}

func (this *STNumArray) sumSegmentTree(i, start, end, left, right int) int {
	if right < start || left > end {
		return 0
	} else if start == end || (left == start && right == end) {
		return this.segmentTree[i]
	}

	mid := (start + end) / 2
	if mid < left {
		return this.sumSegmentTree(2*i+2, mid+1, end, left, right)
	} else if mid+1 > right {
		return this.sumSegmentTree(2*i+1, start, mid, left, right)
	} else {
		return this.sumSegmentTree(2*i+1, start, mid, left, mid) + this.sumSegmentTree(2*i+2, mid+1, end, mid+1, right)
	}
}

func (this *STNumArray) Update(index int, val int) {
	diff := val - this.nums[index]
	this.nums[index] = val

	for i, start, end := 0, 0, len(this.nums)-1; i < len(this.segmentTree); {
		mid := (start + end) / 2
		this.segmentTree[i] = this.segmentTree[i] + diff
		if start == end {
			break
		}
		if index <= mid {
			end = mid
			i = 2*i + 1
		} else {
			start = mid + 1
			i = 2*i + 2
		}
	}
}

func (this *STNumArray) SumRange(left int, right int) int {
	if left > right {
		return 0
	}
	return this.sumSegmentTree(0, 0, len(this.nums)-1, left, right)
}

func main() {

	nums := []int{0, 9, 5, 7, 3}
	obj := STConstructor(nums)
	fmt.Println(obj.segmentTree)
	fmt.Println(obj.SumRange(2, 4))
}
