package main

func getSmallestString(n int, k int) string {
	result := make([]byte, n, n)

	rest := k
	left := n
	end := n
	for ; end > 0; end-- {
		if rest < left+26 {
			break
		}
		result[end-1] = 'z'
		rest -= 26
		left--
	}

	start := 0
	for ; start < end-1; start++ {
		result[start] = 'a'
		rest -= 1
	}
	result[start] = 'a' + byte(rest-1)

	return string(result)
}
