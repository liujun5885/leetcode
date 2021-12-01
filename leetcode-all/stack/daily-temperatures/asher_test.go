package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	expected := []int{1, 1, 4, 2, 1, 1, 0, 0}
	actual := dailyTemperatures(temperatures)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	temperatures := []int{34, 80, 80, 34, 34, 80, 80, 80, 80, 34}
	expected := []int{1, 0, 0, 2, 1, 0, 0, 0, 0, 0}
	actual := dailyTemperatures(temperatures)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}
