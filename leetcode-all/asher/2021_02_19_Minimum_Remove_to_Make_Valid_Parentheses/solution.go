package main

func minRemoveToMakeValid(s string) string {

	var stack []int
	var removed []int

	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else if s[i] == ')' {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			} else {
				removed = append(removed, i)
			}
		}
	}

	removed = append(removed, stack...)
	if len(removed) == 0 {
		return s
	}

	result := s[:removed[0]]
	i := 1
	for ; i < len(removed); i++ {
		result += s[removed[i-1]+1 : removed[i]]
	}
	result += s[removed[i-1]+1:]

	return result
}
