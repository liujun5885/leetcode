package main

func isMatch(s, d string) bool {
	i, j := 0, 0
	for ; i < len(s) && j < len(d); i++ {
		if s[i] == d[j] {
			j++
		}
	}
	return j == len(d)
}

func findLongestWord(s string, d []string) string {
	var result string
	for _, v := range d {
		if isMatch(s, v) == true && (len(result) == 0 || len(v) > len(result) || (len(v) == len(result) && v < result)) {
			result = v
		}
	}
	return result
}
