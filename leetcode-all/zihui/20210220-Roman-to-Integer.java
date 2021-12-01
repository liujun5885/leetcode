class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> roman_int_mapping = new HashMap<Character, Integer>();
        roman_int_mapping.put('I', 1);
        roman_int_mapping.put('V', 5);
        roman_int_mapping.put('X', 10);
        roman_int_mapping.put('L', 50);
        roman_int_mapping.put('C', 100);
        roman_int_mapping.put('D', 500);
        roman_int_mapping.put('M', 1000);
        
        int len = s.length();
        int result = roman_int_mapping.get(s.charAt(len - 1));
        
        for (int i = len - 2; i >= 0; i--) {
            if (roman_int_mapping.get(s.charAt(i)) >= roman_int_mapping.get(s.charAt(i + 1)))
                result += roman_int_mapping.get(s.charAt(i));
            else
                result -= roman_int_mapping.get(s.charAt(i));
        }
        return result;
    }
}
