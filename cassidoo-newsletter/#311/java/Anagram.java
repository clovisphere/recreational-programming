// given two strings `s` and `t` returns `true` if they're anagrams,
// false otherwise

class Anagram {
    private static int HISTOGRAM_SIZE = 256;

    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int histogram[] = new int[HISTOGRAM_SIZE];
        for(int i = 0; i < s.length(); i++) {
            histogram[s.charAt(i)]++;
            histogram[t.charAt(i)]--;
        }
        // valid anagram should have the `histogram` filled with `0s`:-)
        for(int e: histogram) {
            if (e != 0) return false;
        }
        return true;
    }
}
