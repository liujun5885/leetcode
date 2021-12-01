package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	height := []int{1, 2, 3, 4}
	output := numberOfArithmeticSlices(height)
	expected := 3
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
