package main

import "fmt"

type NumArray struct {
	nums []int
	bit  []int
}

func lowBit(num int) int {
	return num & -num
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	arr := NumArray{
		nums: make([]int, n),
		bit:  make([]int, n+1),
	}
	for i := 0; i < n; i++ {
		arr.Update(i, nums[i])
	}
	return arr
}

func (this *NumArray) Sum(index int) int {
	total := 0

	for index += 1; index > 0; index -= lowBit(index) {
		total += this.bit[index]
	}

	return total
}

func (this *NumArray) Update(index int, val int) {
	diff := val - this.nums[index]
	this.nums[index] = val

	for index = index + 1; index < len(this.bit); index += lowBit(index) {
		this.bit[index] += diff
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.Sum(right) - this.Sum(left-1)
}

func main() {
	/*
		["STNumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
		[[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
	*/
	nums := []int{0, 9, 5, 7, 3}
	obj := Constructor(nums)
	fmt.Println(obj.SumRange(4, 4))
}
