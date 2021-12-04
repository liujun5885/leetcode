package meeting_rooms_ii

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	intervals := [][]int{{0, 30}, {5, 10}, {15, 20}}
	actual := minMeetingRooms(intervals)
	expected := 2
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
