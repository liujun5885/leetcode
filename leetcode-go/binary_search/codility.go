package binary_search

//func min(n1, n2 int) int {
//	if n1 < n2 {
//		return n1
//	} else {
//		return n2
//	}
//}

func Solution(A []int) int {
	ans := len(A)
	visited := map[int]bool{}
	total := 0

	if len(A) == 0 {
		return 0
	}

	for _, i := range A {
		if _, ok := visited[i]; !ok {
			visited[i] = true
			total += 1
		}
	}

	for start := 0; start < len(A); start++ {
		visited = map[int]bool{}
		for end := start; end < len(A); end++ {
			location := A[end]
			visited[location] = true
			if len(visited) == total {
				ans = min(ans, end-start+1)
			}
		}
	}

	return ans
}
