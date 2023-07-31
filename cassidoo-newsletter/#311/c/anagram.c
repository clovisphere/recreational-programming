// Given two strings s and t, return true if t is an anagram of s,
// and false otherwise.
#include <stdbool.h>

#define NUMBER_OF_CHAR 26

bool isAnagram(char *s, char *t) {
  int freqS[NUMBER_OF_CHAR] = {0}, freqT[NUMBER_OF_CHAR] = {0}, i;
  for (i = 0; s[i] && t[i]; i++) {
    freqS[s[i] - 'a']++;
    freqT[t[i] - 'a']++;
  }
  // if 's' and 't' are of different length, they cannot be anagram
  if (s[i] || s[i]) {
    return false;
  }
  // for an anagram, both 's' and 't' should have the same value in their
  // respective frequency, i.e 'freqS' & 'freqT'
  for (i = 0; i < NUMBER_OF_CHAR; i++) {
    if (freqS[i] != freqT[i]) {
      return false;
    }
  }
  return true;
}
