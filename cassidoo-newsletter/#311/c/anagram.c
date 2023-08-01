// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise
#include <stdbool.h>

#define HISTOGRAM_SIZE 256

bool is_anagram(char *s, char *t) {
  int histogram[HISTOGRAM_SIZE] = {0}, i = 0;

  for (; s[i] && t[i]; i++) {
    histogram[s[i] - 'a']++;
    histogram[t[i] - 'a']--;
  }
  // if 's' and 't' are of different length, they cannot be anagram
  // 💡 this little trick checks if `s` and `t` have the same size or length
  if (s[i] || t[i])
    return false;
  // valid anagram should have the `histogram` filled with `0s`:-)
  for (i = 0; i < HISTOGRAM_SIZE; i++) {
    if (histogram[i])
      return false;
  }
  return true;
}
