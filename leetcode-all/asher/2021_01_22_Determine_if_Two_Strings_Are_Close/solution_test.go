package main

import (
	"testing"
)

func TestCase01(t *testing.T) {
	word1 := "abc"
	word2 := "bca"
	expected := true
	actual := closeStrings(word1, word2)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	word1 := "a"
	word2 := "aa"
	expected := false
	actual := closeStrings(word1, word2)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	word1 := "cabbba"
	word2 := "abbccc"
	expected := true
	actual := closeStrings(word1, word2)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase04(t *testing.T) {
	word1 := "cabbba"
	word2 := "aabbss"
	expected := false
	actual := closeStrings(word1, word2)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase05(t *testing.T) {
	word1 := "uau"
	word2 := "ssx"
	expected := false
	actual := closeStrings(word1, word2)
	if actual != expected {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
