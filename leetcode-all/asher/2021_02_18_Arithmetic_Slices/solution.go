package main

func isArithmeticSlice(A []int) (int, bool) {
	if len(A) < 3 {
		return 0, false
	}
	diff := A[0] - A[1]
	for i := 0; i < len(A)-1; i++ {
		if A[i]-A[i+1] != diff {
			return diff, false
		}
	}
	return diff, true
}

func numberOfArithmeticSlices1(A []int) int {
	if len(A) < 3 {
		return 0
	}

	result := 0

	for i := 0; i < len(A)-2; i++ {
		if diff, ok := isArithmeticSlice(A[i : i+3]); ok == true {
			result++
			for j := i + 2; j < len(A)-1 && A[j]-A[j+1] == diff; j++ {
				result++
			}
		}
	}

	return result
}

func numberOfArithmeticSlices(A []int) int {
	if len(A) < 3 {
		return 0
	}

	var dp = make([]int, len(A))

	for i := 2; i < len(A); i++ {
		if A[i]-A[i-1] == A[i-1]-A[i-2] {
			dp[i] += dp[i-1] + 1
		}
	}

	result := 0

	for i := 0; i < len(dp); i++ {
		result += dp[i]
	}

	return result
}
