package meeting_rooms_ii

import (
	"github.com/google/go-cmp/cmp"
	"testing"
)

func TestCase01(t *testing.T) {
	intervals := [][]int{{5, 10}, {15, 20}, {0, 30}}
	actual := minMeetingRooms(intervals)
	expected := 2
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase02(t *testing.T) {
	intervals := [][]int{{6, 15}, {13, 20}, {6, 17}}
	actual := minMeetingRooms(intervals)
	expected := 3
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}

func TestCase03(t *testing.T) {
	intervals := [][]int{{13, 15}, {1, 13}}
	actual := minMeetingRooms(intervals)
	expected := 1
	if !cmp.Equal(actual, expected) {
		t.Errorf("actual: %v != expected: %v", actual, expected)
	}
}
