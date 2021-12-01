package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{2, 5, 6, 0, 0, 1, 2}
	target := 0

	output := search(nums, target)
	expected := true
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
