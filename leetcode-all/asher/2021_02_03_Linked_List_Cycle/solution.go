package main

/**
 * Definition for singly-linked list.

 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	var p *ListNode
	m := map[*ListNode]bool{}

	for p = head; p != nil; p = p.Next {
		if _, exists := m[p]; exists {
			return true
		}
		m[p] = true
	}
	return false
}
