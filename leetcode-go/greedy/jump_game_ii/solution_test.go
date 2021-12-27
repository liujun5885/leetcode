package jump_game_ii

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	input := []int{2, 3, 1, 1, 4}
	actual := jump(input)
	expected := 2
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
