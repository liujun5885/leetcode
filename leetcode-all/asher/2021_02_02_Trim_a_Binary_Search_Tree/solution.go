package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func initTreeNode(dataSet []int) *TreeNode {
	if len(dataSet) == 0 {
		return nil
	}

	q := make([]*TreeNode, len(dataSet), len(dataSet))
	for i := 0; i < len(q); i++ {
		q[i] = &TreeNode{}
	}

	for i := 0; i < len(dataSet); i++ {
		if dataSet[i] == -1 {
			continue
		}
		node := q[i]
		// assign value
		node.Val = dataSet[i]
		if i == 0 {
			continue
		}
		if (i-1)%2 == 1 {
			q[(i-1)/2].Right = node
		} else {
			q[(i-1)/2].Left = node
		}
	}
	return q[0]
}

func nodeToSlice(root *TreeNode) []int {
	var result []int

	var q []*TreeNode
	q = append(q, root)

	for i := 0; i < len(q); i++ {
		node := q[i]
		if node == nil {
			continue
		}
		result = append(result, node.Val)
		q = append(q, node.Left)
		q = append(q, node.Right)
	}

	return result
}

func trimBST(root *TreeNode, low int, high int) *TreeNode {

	if root == nil {
		return nil
	}

	if root.Val < low {
		root = trimBST(root.Right, low, high)
	} else if root.Val >= low && root.Val <= high {
		root.Left = trimBST(root.Left, low, high)
		root.Right = trimBST(root.Right, low, high)
	} else {
		root = trimBST(root.Left, low, high)
	}

	return root
}
