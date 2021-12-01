package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (t *TreeNode) toSlice() []int {
	if t == nil {
		return []int{}
	}
	var ret []int
	ret = append(ret, t.Left.toSlice()...)
	ret = append(ret, t.Right.toSlice()...)
	ret = append(ret, t.Val)
	return ret
}

func build(preorder []int, inorder []int, preLeft, preRight, inLeft, inRight int, index map[int]int) *TreeNode {
	if preLeft == preRight {
		return nil
	}
	rootVal := preorder[preLeft]
	rootInorderIndex := index[rootVal]
	leftSize := rootInorderIndex - inLeft

	root := TreeNode{Val: rootVal}
	root.Left = build(preorder, inorder, preLeft+1, preLeft+leftSize+1, inLeft, rootInorderIndex, index)
	root.Right = build(preorder, inorder, preLeft+leftSize+1, preRight, rootInorderIndex+1, inRight, index)

	return &root
}

func buildTree(preorder []int, inorder []int) *TreeNode {

	index := map[int]int{}
	for i := 0; i < len(inorder); i++ {
		index[inorder[i]] = i
	}

	return build(preorder, inorder, 0, len(preorder), 0, len(inorder), index)
}
