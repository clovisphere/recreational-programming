// Given two strings s and t, return true if t is an anagram of s,
// and false otherwise.
#include <string>
#include <unordered_map>

bool isAnagram(std::string s, std::string t) {
  if (s.length() != t.length()) {
    return false;
  }
  std::unordered_map<char, int> freq;
  for (int i = 0; i < s.size(); i++) {
    freq[s[i]]++;
    freq[t[i]]--;
  }
  for (auto it : freq) {
    if (it.second)
      return false;
  }
  return true;
}
