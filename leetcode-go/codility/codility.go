package codility

func min(n1, n2 int) int {
	if n1 < n2 {
		return n1
	} else {
		return n2
	}
}

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

	start := 0
	visitedCount := map[int]int{}
	for end := 0; end < len(A); end++ {
		location := A[end]
		visitedCount[location] += 1
		if len(visitedCount) == total {
			for ; len(visitedCount) == total; start++ {
				s := A[start]
				visitedCount[s] -= 1
				if visitedCount[s] == 0 {
					delete(visitedCount, s)
				}
			}
			ans = min(ans, end-start+2)
		}
	}

	return ans
}
