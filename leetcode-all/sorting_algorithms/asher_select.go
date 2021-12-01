package main

import "fmt"

func selectPartition(arr []int, start, end int) int {
	p := start - 1
	middle := arr[end-1]

	for i := start; i < end-1; i++ {
		if arr[i] <= middle {
			p++
			arr[p], arr[i] = arr[i], arr[p]
		}
	}
	arr[p+1], arr[end-1] = arr[end-1], arr[p+1]
	return p + 1
}

func selectIth(arr []int, start, end, i int) int {
	if start == end {
		return arr[start]
	}

	p := selectPartition(arr, start, end)

	if p == i {
		return arr[i]
	} else if p < i {
		return selectIth(arr, p+1, end, i)
	} else {
		return selectIth(arr, start, p, i)
	}
}

func main() {
	arr := []int{4, 1, 3, 9, 7, 9, 10, 0, 1, 6}
	i := 5
	fmt.Printf("the %d smallest is: %d\n", i, selectIth(arr, 0, len(arr), i-1))
	fmt.Println(arr)
}
