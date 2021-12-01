package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	input := "()"

	output := scoreOfParentheses(input)
	expected := 1
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase02(t *testing.T) {
	input := "(())"

	output := scoreOfParentheses(input)
	expected := 2
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase03(t *testing.T) {
	input := "()()"

	output := scoreOfParentheses(input)
	expected := 2
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase04(t *testing.T) {
	input := "(()(()))"

	output := scoreOfParentheses(input)
	expected := 6
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase05(t *testing.T) {
	input := "((((((())))()())))"

	output := scoreOfParentheses(input)
	expected := 80
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase06(t *testing.T) {
	input := "AB"

	output := scoreOfParentheses(input)
	expected := 131
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
