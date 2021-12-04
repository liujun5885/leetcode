// Package copy_list_with_random_pointer https://leetcode-cn.com/problems/copy-list-with-random-pointer/
package main

import "fmt"

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	startNode := &Node{}

	nodeMap := map[string][]*Node{}

	ptr1 := head
	ptr2 := startNode
	for ptr1 != nil {
		n := &Node{Val: ptr1.Val}
		addr := fmt.Sprintf("%p", ptr1)
		nodeMap[addr] = []*Node{ptr1, n}
		ptr2.Next = n
		ptr1 = ptr1.Next
		ptr2 = ptr2.Next
	}

	ptr1 = head
	ptr2 = startNode.Next
	for ptr1 != nil {
		if ptr1.Random == nil {
			ptr1 = ptr1.Next
			ptr2 = ptr2.Next
			continue
		}
		addr := fmt.Sprintf("%p", ptr1.Random)
		ptr2.Random = nodeMap[addr][1]

		ptr1 = ptr1.Next
		ptr2 = ptr2.Next
	}

	return startNode.Next
}
