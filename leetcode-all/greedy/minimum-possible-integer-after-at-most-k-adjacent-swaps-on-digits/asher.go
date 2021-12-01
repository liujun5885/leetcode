package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
)

func lowBit(num int) int {
	return num & -num
}

func Constructor(n int) []int {
	bit := make([]int, n+1)

	for i := 0; i < n; i++ {
		Update(bit, i, 1)
	}
	return bit
}

func Sum(bit []int, index int) int {
	total := 0

	for index += 1; index > 0; index -= lowBit(index) {
		total += bit[index]
	}

	return total
}

func Update(bit []int, index int, diff int) {
	for index = index + 1; index < len(bit); index += lowBit(index) {
		bit[index] += diff
	}
}

func minInteger(num string, k int) string {
	sortedNums := []byte{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
	numVsIndex := map[byte][]int{}
	for i := 0; i < len(num); i++ {
		if _, ok := numVsIndex[num[i]]; ok {
			numVsIndex[num[i]] = append(numVsIndex[num[i]], i)
		} else {
			numVsIndex[num[i]] = []int{i}
		}
	}
	n := len(num)
	bit := Constructor(n)

	var result []byte

	move := 0

	for j := 0; move < k && j < n; j++ {
		for i := 0; i < 10; i++ {
			if _, ok := numVsIndex[sortedNums[i]]; !ok {
				continue
			}
			index := Sum(bit, numVsIndex[sortedNums[i]][0]-1)

			if index+move <= k {
				move += index
				result = append(result, sortedNums[i])
				Update(bit, numVsIndex[sortedNums[i]][0], -1)
				numVsIndex[sortedNums[i]] = numVsIndex[sortedNums[i]][1:]
				if len(numVsIndex[sortedNums[i]]) == 0 {
					delete(numVsIndex, sortedNums[i])
				}
				num = num[:index] + num[index+1:]
				break
			}
		}
	}

	return string(result) + num
}

func main() {
	num := "294984148179"
	k := 11
	output := minInteger(num, k)
	expected := "124498948179"
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	num = "9438957234785635408"
	k = 23
	output = minInteger(num, k)
	expected = "0345989723478563548"
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	num = "4321"
	k = 4
	output = minInteger(num, k)
	expected = "1342"
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}

	num = "36789"
	k = 1000
	output = minInteger(num, k)
	expected = "36789"
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
