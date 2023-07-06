package leetcode

import (
	"reflect"
	"testing"
)

var tests = []struct {
	nums     []int
	target   int
	expected []int
}{
	// test cases here
	{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
	{[]int{3, 2, 4}, 6, []int{1, 2}},
	{[]int{3, 3}, 6, []int{0, 1}},
}

func TestTwoSum(t *testing.T) {
	for _, tc := range tests {
		if got := twoSum(tc.nums, tc.target); !reflect.DeepEqual(got, tc.expected) {
			t.Fatalf("expected: %v, got: %v", tc.expected, got)
		}
	}
}
