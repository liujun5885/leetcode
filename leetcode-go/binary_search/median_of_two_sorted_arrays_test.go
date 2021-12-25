package binary_search

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestGetKthCase01(t *testing.T) {
	nums1 := []int{1, 3}
	nums2 := []int{2}
	actual := getKth(nums1, nums2, 2)
	expected := 2
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestGetKthCase02(t *testing.T) {
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	actual := getKth(nums1, nums2, 3)
	expected := 3
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestGetKthCase03(t *testing.T) {
	nums1 := []int{0, 0}
	nums2 := []int{0, 0}
	actual := getKth(nums1, nums2, 3)
	expected := 0
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase01(t *testing.T) {
	nums1 := []int{1, 3}
	nums2 := []int{2}
	actual := findMedianSortedArrays(nums1, nums2)
	expected := 2.0
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	actual := findMedianSortedArrays(nums1, nums2)
	expected := 2.5
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	nums1 := []int{0, 0}
	nums2 := []int{0, 0}
	actual := findMedianSortedArrays(nums1, nums2)
	expected := 2.5
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
