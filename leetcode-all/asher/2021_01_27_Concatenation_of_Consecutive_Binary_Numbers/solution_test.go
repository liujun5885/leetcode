package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	n := 1
	expected := 1
	actual := concatenatedBinary(n)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	n := 3
	expected := 27
	actual := concatenatedBinary(n)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	n := 12
	expected := 505379714
	actual := concatenatedBinary(n)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	n := 42
	expected := 727837408
	actual := concatenatedBinary(n)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
