package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	a := []int{2, 7, 11, 15}
	b := []int{1, 10, 4, 11}

	actual := advantageCount(a, b)
	expected := []int{2, 11, 7, 15}
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	a := []int{12, 24, 8, 32}
	b := []int{13, 25, 32, 11}

	actual := advantageCount(a, b)
	expected := []int{24, 32, 8, 12}
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	a := []int{28, 47, 45, 8, 2, 10, 25, 35, 43, 37, 33, 30, 33, 20, 33, 42, 43, 36, 34, 3, 16, 23, 15, 10, 19, 42, 13, 47, 0, 21, 36, 38, 0, 5, 3, 28, 4, 20, 14, 5, 19, 22, 29, 17, 3, 16, 35, 0, 26, 0}
	b := []int{44, 10, 27, 4, 27, 40, 46, 40, 45, 0, 41, 2, 44, 50, 36, 30, 37, 4, 44, 4, 12, 13, 35, 20, 19, 25, 38, 42, 43, 14, 2, 4, 5, 38, 4, 38, 0, 35, 12, 32, 38, 33, 3, 1, 19, 46, 23, 13, 24, 41}

	actual := advantageCount(a, b)
	expected := []int{35, 15, 29, 13, 28, 47, 35, 45, 33, 3, 47, 4, 30, 23, 37, 33, 38, 10, 22, 10, 16, 19, 36, 21, 20, 28, 43, 0, 0, 19, 3, 8, 14, 43, 5, 42, 2, 36, 16, 33, 42, 34, 5, 3, 20, 0, 25, 17, 26, 0}
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
