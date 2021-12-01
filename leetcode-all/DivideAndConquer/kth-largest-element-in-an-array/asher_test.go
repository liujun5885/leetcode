package kth_largest_element_in_an_array

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	input1 := []int{3, 2, 1, 5, 6, 4}
	input2 := 2
	expected := 5
	actual := findKthLargest(input1, input2)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	input1 := []int{3, 2, 3, 1, 2, 4, 5, 5, 6}
	input2 := 4
	expected := 4
	actual := findKthLargest(input1, input2)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	input1 := []int{2, 2, 2, 1, 1, 1}
	input2 := 2
	expected := 2
	actual := findKthLargest(input1, input2)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}
