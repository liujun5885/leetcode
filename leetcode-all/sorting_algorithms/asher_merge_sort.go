package main

import "fmt"

func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	m := len(arr) / 2

	l := make([]int, m)
	copy(l, arr[0:m])
	r := make([]int, len(arr)-m)
	copy(r, arr[m:])
	mergeSort(l)
	mergeSort(r)

	i, p, j := 0, 0, 0
	for ; i < m && j < len(arr)-m; p++ {
		if l[i] < r[j] {
			arr[p] = l[i]
			i++
		} else {
			arr[p] = r[j]
			j++
		}
	}
	for ; i < m; i, p = i+1, p+1 {
		arr[p] = l[i]
	}
	for ; j < len(arr)-m; j, p = j+1, p+1 {
		arr[p] = r[j]
	}

	return arr
}

func main() {
	arr := []int{4, 1, 3, 9, 7, 9, 10, 0, 1}
	arr = mergeSort(arr)
	fmt.Println(arr)
}
