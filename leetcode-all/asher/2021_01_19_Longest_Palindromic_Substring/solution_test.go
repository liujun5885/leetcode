package solution

import (
	"testing"
)

func TestCase01(t *testing.T) {
	s := "babad"
	expected := "bab"
	actual := longestPalindrome(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	s := "cbbd"
	expected := "bb"
	actual := longestPalindrome(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	s := "a"
	expected := "a"
	actual := longestPalindrome(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	s := "ac"
	expected := "a"
	actual := longestPalindrome(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase05(t *testing.T) {
	s := "abcba"
	expected := "abcba"
	actual := longestPalindrome(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
