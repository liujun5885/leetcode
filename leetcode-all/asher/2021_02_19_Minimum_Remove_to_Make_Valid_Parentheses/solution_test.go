package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	s := "lee(t(c)o)de)"
	output := minRemoveToMakeValid(s)
	expected := "lee(t(c)o)de"
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase02(t *testing.T) {
	s := "a)b(c)d"
	output := minRemoveToMakeValid(s)
	expected := "ab(c)d"
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase03(t *testing.T) {
	s := "))(("
	output := minRemoveToMakeValid(s)
	expected := ""
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase04(t *testing.T) {
	s := "(a(b(c)d)"
	output := minRemoveToMakeValid(s)
	expected := "a(b(c)d)"
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}

func TestCase05(t *testing.T) {
	s := "())()((("
	output := minRemoveToMakeValid(s)
	expected := "()()"
	if !cmp.Equal(output, expected) {
		t.Errorf("actual: %v != expected: %v", output, expected)
	}
}
