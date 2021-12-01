package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{1, 3, 2, 2, 5, 2, 3, 7}
	expected := 5
	actual := findLHS(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	expected := 2
	actual := findLHS(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
