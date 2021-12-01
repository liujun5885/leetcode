package main

func numberOfBits(n int) int {
	total := 0
	for i := n; i > 0; i = i >> 1 {
		total++
	}
	return total
}

func concatenatedBinary(n int) int {
	total := 0
	shift := 0
	multi := 1
	for i := n; i > 0; i-- {
		multi *= 1 << shift
		multi = multi % 1000000007
		total += i * multi
		total = total % 1000000007
		shift = numberOfBits(i)
	}
	return total
}
