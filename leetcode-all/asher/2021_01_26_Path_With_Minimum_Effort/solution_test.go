package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	heights := [][]int{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}
	expected := 2
	actual := minimumEffortPath(heights)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	heights := [][]int{{1, 2, 3}, {3, 8, 4}, {5, 3, 5}}
	expected := 1
	actual := minimumEffortPath(heights)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	heights := [][]int{{1, 2, 1, 1, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 1, 1, 2, 1}}
	expected := 0
	actual := minimumEffortPath(heights)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	heights := [][]int{{3}, {3}, {7}, {2}, {9}, {9}, {3}, {7}, {10}}
	expected := 7
	actual := minimumEffortPath(heights)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
