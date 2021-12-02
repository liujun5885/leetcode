package critical_connections_in_a_network

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	n := 4
	connections := [][]int{{0, 1}, {1, 2}, {2, 0}, {1, 3}}
	actual := criticalConnections(n, connections)
	expected := [][]int{{3, 1}}
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	n := 4
	connections := [][]int{{0, 1}, {1, 2}, {2, 3}, {3, 0}}
	actual := criticalConnections(n, connections)
	var expected [][]int
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
