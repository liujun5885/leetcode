// Package binary_search https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
package binary_search

func min(n1, n2 int) int {
	if n1 < n2 {
		return n1
	} else {
		return n2
	}
}

func getKth(nums1 []int, nums2 []int, k int) int {
	len1 := len(nums1)
	len2 := len(nums2)

	index1 := 0
	index2 := 0

	for {
		if index1 >= len1 {
			return nums2[index2+k-1]
		}
		if index2 >= len2 {
			return nums1[index1+k-1]
		}
		if k == 1 {
			return min(nums1[index1], nums2[index2])
		}

		halfK := k / 2

		half1 := min(index1+halfK, len1) - 1
		half2 := min(index2+halfK, len2) - 1

		pivot1 := nums1[half1]
		pivot2 := nums2[half2]

		if pivot1 < pivot2 {
			k -= half1 - index1 + 1
			index1 = half1 + 1
		} else {
			k -= half2 - index2 + 1
			index2 = half2 + 1
		}
	}

}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	len1 := len(nums1)
	len2 := len(nums2)
	total := len1 + len2
	if total%2 == 1 {
		return float64(getKth(nums1, nums2, total/2+1))
	} else {
		return float64(getKth(nums1, nums2, total/2)+getKth(nums1, nums2, total/2+1)) / 2.0
	}
}
