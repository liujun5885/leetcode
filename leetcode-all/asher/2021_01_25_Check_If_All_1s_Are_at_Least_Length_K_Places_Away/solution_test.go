package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{1, 0, 0, 0, 1, 0, 0, 1}
	k := 2
	expected := true
	actual := kLengthApart(nums, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums := []int{1, 0, 0, 1, 0, 1}
	k := 2
	expected := false
	actual := kLengthApart(nums, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	nums := []int{1, 1, 1, 1, 1}
	k := 0
	expected := true
	actual := kLengthApart(nums, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	nums := []int{0, 1, 0, 1}
	k := 1
	expected := true
	actual := kLengthApart(nums, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
