package solution

func isValid(s string) bool {
	stack := make([]int32, 0, len(s))
	for _, v := range s {
		if v == '(' || v == '{' || v == '[' {
			stack = append(stack, v)
		} else if v == ')' && len(stack) > 0 && stack[len(stack)-1] == '(' {
			stack = stack[:len(stack)-1]
		} else if v == '}' && len(stack) > 0 && stack[len(stack)-1] == '{' {
			stack = stack[:len(stack)-1]
		} else if v == ']' && len(stack) > 0 && stack[len(stack)-1] == '[' {
			stack = stack[:len(stack)-1]
		} else if v == ']' || v == '}' || v == ')' {
			return false
		}
	}
	if len(stack) > 0 {
		return false
	} else {
		return true
	}
}
