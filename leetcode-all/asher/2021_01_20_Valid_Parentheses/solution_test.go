package solution

import (
	"testing"
)

func TestCase01(t *testing.T) {
	s := "()"
	expected := true
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	s := "()[]{}"
	expected := true
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	s := "(]"
	expected := false
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	s := "([)]"
	expected := false
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase05(t *testing.T) {
	s := "{[]}"
	expected := true
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase06(t *testing.T) {
	s := "("
	expected := false
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase07(t *testing.T) {
	s := "(("
	expected := false
	actual := isValid(s)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
