package main

import "math"

func maxArea(height []int) int {
	result := 0

	start := 0

	for i := 0; i < len(height)-1; i++ {
		if result > 0 && height[i] <= height[start] {
			continue
		}
		for j := i + 1; j < len(height); j++ {
			size := int(math.Abs(float64((j - i) * int(math.Min(float64(height[j]), float64(height[i]))))))
			if size > result {
				result = size
				start = i
			}
		}
	}

	return result
}
