package solution

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	mat := [][]int{{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}}
	expected := [][]int{{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}}
	actual := diagonalSort(mat)
	if !cmp.Equal(expected, actual) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
