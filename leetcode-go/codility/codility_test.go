package codility

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func Test01(t *testing.T) {
	A := []int{2, 1, 1, 3, 2, 1, 1, 3}
	actual := Solution(A)
	expected := 3
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func Test02(t *testing.T) {
	A := []int{7, 5, 2, 7, 2, 7, 4, 7}
	actual := Solution(A)
	expected := 6
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
