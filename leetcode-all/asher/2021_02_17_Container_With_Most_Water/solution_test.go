package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	height := []int{1, 1}
	output := maxArea(height)
	expected := 1
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase02(t *testing.T) {
	height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	output := maxArea(height)
	expected := 49
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase03(t *testing.T) {
	height := []int{4, 3, 2, 1, 4}
	output := maxArea(height)
	expected := 16
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase04(t *testing.T) {
	height := []int{1, 2, 1}
	output := maxArea(height)
	expected := 2
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
