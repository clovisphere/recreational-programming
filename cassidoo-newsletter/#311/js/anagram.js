// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise

const isAnagram = (s, t) =>
  s.toLowerCase().split('').sort().join('') == t.toLowerCase().split('').sort().join('');
