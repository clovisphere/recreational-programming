// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise

import Foundation

func IsAnagram(_ s: String, _ t: String) -> Bool {
    s.lowercased().sorted() == t.lowercased().sorted()
}
