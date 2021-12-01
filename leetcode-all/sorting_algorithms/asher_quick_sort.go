package main

import (
	"fmt"
)

func partition(arr []int, start, end int) int {
	x := arr[end]
	p := start - 1
	for i := start; i < end; i++ {
		if arr[i] <= x {
			p = p + 1
			arr[i], arr[p] = arr[p], arr[i]
		}
	}
	arr[p+1], arr[end] = arr[end], arr[p+1]

	return p + 1
}

func _quickSort(arr []int, start, end int) {
	if start >= end {
		return
	}
	q := partition(arr, start, end)
	_quickSort(arr, start, q-1)
	_quickSort(arr, q+1, end)
}

func quickSort(arr []int) {
	_quickSort(arr, 0, len(arr)-1)
}

func main() {
	arr := []int{4, 1, 3, 9, 7, 9, 10, 0, 1, 6}
	quickSort(arr)
	fmt.Println(arr)
}
