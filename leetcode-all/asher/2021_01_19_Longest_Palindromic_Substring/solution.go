package solution

func longestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}
	var maxLen = 1
	var start = 0
	var status = make([][]bool, len(s))
	for i := range status {
		status[i] = make([]bool, len(s))
	}
	for i := 0; i < len(s); i++ {
		status[i][i] = true
	}

	for i := 1; i < len(s); i++ {
		for j := 0; j < i; j++ {
			if s[i] != s[j] {
				status[i][j] = false
			} else {
				if i-j <= 2 {
					status[i][j] = true
				} else {
					status[i][j] = status[i-1][j+1]
				}
			}
			if status[i][j] && i-j+1 > maxLen {
				maxLen = i - j + 1
				start = j
			}
		}
	}

	return s[start : start+maxLen]
}
