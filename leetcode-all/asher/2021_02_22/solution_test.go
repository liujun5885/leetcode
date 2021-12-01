package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	s := "abpcplea"
	d := []string{"ale", "apple", "abple", "monkey", "plea"}
	output := findLongestWord(s, d)
	expected := "abple"
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
