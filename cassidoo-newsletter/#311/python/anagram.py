# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise
def is_anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())
