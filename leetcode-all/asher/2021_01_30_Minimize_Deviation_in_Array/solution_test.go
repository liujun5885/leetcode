package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	expected := 1
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums := []int{4, 1, 5, 20, 3}
	expected := 3
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	nums := []int{2, 10, 8}
	expected := 3
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	nums := []int{3, 5}
	expected := 1
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase05(t *testing.T) {
	nums := []int{10, 4, 3}
	expected := 2
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase06(t *testing.T) {
	nums := []int{2, 8, 6, 1, 6}
	expected := 1
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase07(t *testing.T) {
	nums := []int{399, 908, 648, 357, 693, 502, 331, 649, 596, 698}
	expected := 315
	actual := minimumDeviation(nums)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
