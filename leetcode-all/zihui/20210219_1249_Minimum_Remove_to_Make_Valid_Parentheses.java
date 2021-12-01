class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> stack = new Stack();
        String[] array = s.split("");
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals("(")) {
                stack.push(i);
            }
            if (array[i].equals(")")) {
                if (stack.empty() == false) {
                    stack.pop();
                } else {
                    array[i] = "";
                }
            }
        }

        while (stack.empty() == false) {
            array[stack.pop()] = "";
        }
        return String.join("", array);
    }
}
