package solution

import "sort"

func maxOperations(nums []int, k int) int {
	count := 0

	sort.Ints(nums)

	for s, e := 0, len(nums)-1; s < e; {
		if nums[s]+nums[e] == k {
			s += 1
			e -= 1
			count += 1
		} else if nums[s]+nums[e] < k {
			s += 1
		} else {
			e -= 1
		}
	}

	return count
}

func maxOperationsMethod1(nums []int, k int) int {
	count := 0
	dict := map[int]bool{}

	for i, v1 := range nums {
		if _, ok := dict[i]; ok {
			println(i)
			continue
		}

		for j, v2 := range nums[i+1:] {
			if _, ok := dict[j+i+1]; ok {
				continue
			}
			if v1+v2 == k {
				count += 1
				dict[i] = true
				dict[j+i+1] = true
				break
			}
		}
	}

	return count
}
