package main

import "fmt"

func heapify(arr []int, i int) {
	left := i*2 + 1
	right := i*2 + 2
	max := i

	if left < len(arr) && arr[left] > arr[max] {
		max = left
	}
	if right < len(arr) && arr[right] > arr[max] {
		max = right
	}
	if max != i {
		arr[i], arr[max] = arr[max], arr[i]
		heapify(arr, max)
	}
}

func heapSort(arr []int) []int {
	for i := len(arr) / 2; i >= 0; i-- {
		heapify(arr, i)
	}
	for i := len(arr) - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr[:i], 0)
	}
	return arr
}

func main() {
	arr := []int{4, 1, 3, 9, 7, 9, 10, 0, 1, 6}
	heapSort(arr)
	fmt.Println(arr)
}
