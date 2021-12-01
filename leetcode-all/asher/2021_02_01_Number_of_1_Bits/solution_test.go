package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	n := uint32(0b1011)
	expected := 3
	actual := hammingWeight(n)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	n := uint32(0b10000000)
	expected := 1
	actual := hammingWeight(n)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	n := uint32(0b11111111111111111111111111111101)
	expected := 31
	actual := hammingWeight(n)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	n := uint32(0b0)
	expected := 0
	actual := hammingWeight(n)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase05(t *testing.T) {
	n := uint32(0b11111111111111111111111111111111)
	expected := 32
	actual := hammingWeight(n)
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
