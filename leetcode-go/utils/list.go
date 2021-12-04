package utils

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) append(n *ListNode) {
	l.Next = n
}

func (l *ListNode) print() {
	for i := l; i != nil; i = i.Next {
		fmt.Print(i.Val)
	}
	fmt.Println()
}

func (l *ListNode) cmp(t *ListNode) bool {
	s1, s2 := l, t
	for ; s1 != nil && s2 != nil; s1, s2 = s1.Next, s2.Next {
		if s1.Val != s2.Val {
			return false
		}
	}
	if s1 == nil && s2 == nil {
		return true
	} else {
		return false
	}
}

func convert(l *ListNode) []int {
	if l == nil {
		return []int{}
	}
	result := make([]int, 0)
	for i := l; i != nil; i = i.Next {
		result = append(result, i.Val)
	}
	return result
}

func initListNode(list []int) *ListNode {
	if len(list) == 0 {
		return nil
	}
	root := &ListNode{}

	if len(list) == 0 {
		return root
	}

	root.Val = list[0]

	for i, start := 1, root; i < len(list); i, start = i+1, start.Next {
		start.Next = &ListNode{Val: list[i]}
	}

	return root
}
