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

func Test03(t *testing.T) {
	A := []int{7}
	actual := Solution(A)
	expected := 1
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func Test04(t *testing.T) {
	A := []int{7, 3, 7, 3, 1, 3, 4, 1}
	actual := Solution(A)
	expected := 5
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func Test05(t *testing.T) {
	A := []int{7, 3}
	actual := Solution(A)
	expected := 2
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func Test06(t *testing.T) {
	A := []int{7, 7}
	actual := Solution(A)
	expected := 1
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
