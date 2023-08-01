// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise
extern crate itertools;
use itertools::Itertools;

/// Returns the sorted alphabetic symbols of a string in lowercase
fn transform(w: &str) -> Vec<char> {
    w.chars()
        .flap_map(char::to_lowercase)
        .filter(|c| c.is_alphabetic())
        .sorted();
}

pub fn is_anagram(s: &str, t: &str) -> bool {
    transform(s) == transform(b)
}
