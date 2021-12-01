package main

func scoreOfParentheses(S string) int {
	var stack []int32

	for _, v := range S {
		if v != ')' {
			if v == '(' {
				stack = append(stack, -1)
			} else {
				stack = append(stack, v)
			}
			continue
		}

		if len(stack) < 1 {
			return 0
		}

		var p int32
		i := len(stack) - 1
		for ; i >= 0; i-- {
			if stack[i] == -1 {
				if i == len(stack)-1 {
					p = 1
				} else {
					p = 2 * p
				}
				break
			}
			p += stack[i]
		}
		stack = stack[:i]
		stack = append(stack, p)
	}

	var result int32

	for i := 0; i < len(stack); i++ {
		result += stack[i]
	}

	return int(result)
}
