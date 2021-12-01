package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	/*
		Input: lists = [[1,4,5],[1,3,4],[2,6]]
		Output: [1,1,2,3,4,4,5,6]
	*/
	list := [][]int{{4, 1, 5}, {1, 4, 3}, {6, 2}}
	input := make([]*ListNode, 0, len(list))
	for _, v := range list {
		input = append(input, initListNode(v))
	}
	expected := initListNode([]int{1, 1, 2, 3, 4, 4, 5, 6})
	actual := mergeKLists(input)
	if !actual.cmp(expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	var lists []*ListNode
	expected := (*ListNode)(nil)
	actual := mergeKLists(lists)
	if !actual.cmp(expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	lists := []*ListNode{nil}
	expected := (*ListNode)(nil)
	actual := mergeKLists(lists)
	if !actual.cmp(expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
