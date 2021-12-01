class Solution {
    public boolean isMatch(String s, String p) {
        if (p.length() == 0) {
            return s.length() == 0;
        }
        if (p.length() > 1 && p.charAt(1) == '*') {
            return isMatch(s, p.substring(2)) || (s.length() > 0 && hasSameFirstLetters(s, p) && isMatch(s.substring(1), p));
        } else {
            return s.length() > 0 && hasSameFirstLetters(s, p) && isMatch(s.substring(1), p.substring(1));
        }
    }

    public boolean hasSameFirstLetters(String s, String p) {
        return s.charAt(0) == p.charAt(0) || p.charAt(0) == '.';
    }
}
