package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	dataSet := []int{3, 9, 20, -1, -1, 15, 7}
	root := initTreeNode(dataSet)
	expected := [][]int{{9}, {3, 15}, {20}, {7}}
	actual := verticalTraversal(root)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	dataSet := []int{1, 2, 3, 4, 5, 6, 7}
	root := initTreeNode(dataSet)
	expected := [][]int{{4}, {2}, {1, 5, 6}, {3}, {7}}
	actual := verticalTraversal(root)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
