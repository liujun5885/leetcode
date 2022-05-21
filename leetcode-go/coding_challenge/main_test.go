package main

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	c.inc("a")
	actual := c.get("a")
	expected := 1

	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
