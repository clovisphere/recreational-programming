// Given two strings s and t, return true if t is an anagram of s,
// and false otherwise.
#include <string>
#include <unordered_map>

bool isAnagram(std::string s, std::string t) {
  if (s.length() != t.length()) {
    return false;
  }
  std::unordered_map<char, int> histogram;
  for (int i = 0; i < s.size(); i++) {
    histogram[s[i]]++;
    histogram[t[i]]--;
  }
  for (auto it : histogram) {
    if (it.second)
      return false;
  }
  return true;
}
