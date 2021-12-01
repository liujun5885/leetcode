class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == -2147483648 && divisor == -1)
            return 2147483647;
        
        int res = 0;
        int a = Math.abs(dividend), b = Math.abs(divisor);
        while (a - b >= 0) {
            int x = 0;
            while (a - (b << 1 << x) >= 0) {
                x++;
            }
            res += 1 << x;
            a -= b << x;
        }
        if (dividend > 0 == divisor > 0)
            return res;
        return -res;
    }
}
