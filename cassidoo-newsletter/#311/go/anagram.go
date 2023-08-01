// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise
package anagram

import (
	"sort"
	"strings"
)

// Returns the sorted alphabetic symbols of a string in lowercase
func transform(w string) string {
	xs := strings.Split(strings.ToLower(w), "")
	sort.Strings(xs)
	return strings.Join(xs, "")
}

func IsAnagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}
	return transform(s) == transform(t)
}
