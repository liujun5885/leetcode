package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	n, k := 3, 27
	expected := "aay"
	actual := getSmallestString(n, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	n, k := 5, 73
	expected := "aaszz"
	actual := getSmallestString(n, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	n, k := 5, 130
	expected := "zzzzz"
	actual := getSmallestString(n, k)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
