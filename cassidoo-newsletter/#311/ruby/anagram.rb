# given two strings `s` and `t` returns `true` if they're anagrams,
# false otherwise

def is_anagram?(s, t) = s.downcase.chars.sort.join == t.downcase.chars.sort.join
