class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        if (pushed.length != popped.length)
            return false;
        
        Stack <Integer> stack = new Stack <Integer>();
        int i = 0;
        for (int j: pushed) {
            while (!stack.isEmpty() && stack.peek() == popped[i]) {
                stack.pop();
                i++;
            }
            stack.push(j);
        }
        while (!stack.isEmpty()) {
            if (stack.pop() != popped[i])
                return false;
            i++;
        }
        return true;
    }
}
