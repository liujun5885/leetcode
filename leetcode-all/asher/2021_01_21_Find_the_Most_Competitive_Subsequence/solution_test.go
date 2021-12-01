package solution

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	nums := []int{3, 5, 2, 6}
	k := 2
	expected := []int{2, 6}
	actual := mostCompetitive(nums, k)
	if !cmp.Equal(expected, actual) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	nums := []int{2, 4, 3, 3, 5, 4, 9, 6}
	k := 4
	expected := []int{2, 3, 3, 4}
	actual := mostCompetitive(nums, k)

	if !cmp.Equal(expected, actual) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	nums := []int{2, 4, 3, 3, 5, 4, 1, 1, 6}
	k := 4
	expected := []int{2, 1, 1, 6}
	actual := mostCompetitive(nums, k)

	if !cmp.Equal(expected, actual) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
