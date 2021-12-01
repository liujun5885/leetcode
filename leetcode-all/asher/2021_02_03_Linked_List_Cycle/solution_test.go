package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	root := &ListNode{
		Val:  3,
		Next: nil,
	}
	node1 := &ListNode{
		Val:  2,
		Next: nil,
	}
	root.Next = node1
	node2 := &ListNode{
		Val:  0,
		Next: nil,
	}
	node1.Next = node2
	node3 := &ListNode{
		Val:  -4,
		Next: node1,
	}
	node2.Next = node3
	expected := true
	actual := hasCycle(root)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
