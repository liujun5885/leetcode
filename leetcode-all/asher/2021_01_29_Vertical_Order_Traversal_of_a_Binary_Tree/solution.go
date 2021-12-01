package main

import (
	"fmt"
	"sort"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func printTree(root *TreeNode) {
	if root == nil {
		return
	}

	queue := []*TreeNode{}
	queue = append(queue, root)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		fmt.Println(node.Val)

		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

}

func initTreeNode(dataSet []int) *TreeNode {
	if len(dataSet) == 0 {
		return nil
	}

	queue := make([]*TreeNode, len(dataSet), len(dataSet))
	for i := 0; i < len(queue); i++ {
		queue[i] = &TreeNode{}
	}

	for i := 0; i < len(dataSet); i++ {
		if dataSet[i] == -1 {
			continue
		}
		node := queue[i]
		// assign value
		node.Val = dataSet[i]
		if i == 0 {
			continue
		}
		if (i-1)%2 == 1 {
			queue[(i-1)/2].Right = node
		} else {
			queue[(i-1)/2].Left = node
		}
	}

	return queue[0]
}

func buildMapping(node *TreeNode, x int, y int, mapping map[int]map[int][]int) {
	if node == nil {
		return
	}

	if mapping[x] == nil {
		mapping[x] = map[int][]int{y: {node.Val}}
	} else {
		mapping[x][y] = append(mapping[x][y], node.Val)
	}

	buildMapping(node.Left, x-1, y-1, mapping)
	buildMapping(node.Right, x+1, y-1, mapping)
}

func verticalTraversal(root *TreeNode) [][]int {
	mapping := map[int]map[int][]int{}
	result := map[int][]int{}
	var ret [][]int

	buildMapping(root, 0, 0, mapping)

	var keys []int
	for k, v := range mapping {
		keys = append(keys, k)

		var ks []int
		var block []int
		for kk, _ := range v {
			ks = append(ks, kk)
		}
		sort.Sort(sort.Reverse(sort.IntSlice(ks)))
		for _, kk := range ks {
			sort.Ints(v[kk])
			block = append(block, v[kk]...)
		}
		result[k] = block
	}

	sort.Ints(keys)
	for _, k := range keys {
		ret = append(ret, result[k])
	}

	return ret
}
