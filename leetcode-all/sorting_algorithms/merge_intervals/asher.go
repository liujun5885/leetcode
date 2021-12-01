package main

func merge(intervals [][]int) [][]int {
	var result [][]int
	result = append(result, intervals[0])

	for i, element := range intervals[1:] {
		if element[1] < result[i][1] {
			continue
		} else if element[0] <= result[i][1] && result[i][1] <= element[1] {
			result[i][1] = element[1]
		} else {
			result = append(result, element)
			i += 1
		}
	}
	return result
}
