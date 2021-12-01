package solution

import (
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	k := 5
	expected := 2
	actual := maxOperations(nums, k)
	if actual != expected {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums := []int{3, 1, 3, 4, 3}
	k := 6
	expected := 1
	actual := maxOperations(nums, k)
	if actual != expected {
		t.Errorf("actual: %d != expected: %d", actual, expected)
	}
}
