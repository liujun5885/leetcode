package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	data := []int{1, 0, 2}
	root := initTreeNode(data)
	low := 1
	high := 2
	expected := []int{1, 2}
	actual := trimBST(root, low, high)
	if !cmp.Equal(nodeToSlice(actual), expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	data := []int{3, 0, 4, -1, 2, -1, -1, 1}
	root := initTreeNode(data)
	low := 1
	high := 3
	expected := []int{3, 2, 1}
	actual := trimBST(root, low, high)
	if !cmp.Equal(nodeToSlice(actual), expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
