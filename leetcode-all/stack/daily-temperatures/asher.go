package main

func dailyTemperatures(temperatures []int) []int {
	var stack []int
	ans := make([]int, len(temperatures))

	for i, v := range temperatures {
		n := len(stack)
		if n == 0 || v <= temperatures[stack[n-1]] {
			stack = append(stack, i)
		} else {
			for nn := len(stack); nn > 0 && temperatures[stack[nn-1]] < v; nn = len(stack) {
				ans[stack[nn-1]] = i - stack[nn-1]
				stack = stack[:nn-1]
			}
			stack = append(stack, i)
		}
	}

	return ans
}
