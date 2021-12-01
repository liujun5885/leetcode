class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int[] farthestIdx = new int[n];

        for (int i = 0; i < n; i ++) {
            farthestIdx[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            int curr_gas = gas[i];
            if (curr_gas < cost[i]) {
                farthestIdx[i] = i;
            } else {
                int j = i;
                if (farthestIdx[i] > -1) {
                    j = farthestIdx[i];
                }
                while (curr_gas >= cost[j]) {
                    curr_gas = curr_gas - cost[j] + gas[(j + 1) % n];
                    j = (j + 1) % n;
                    if (j == i) {
                        return i;
                    } else {
                        farthestIdx[j] = j;
                    }
                }
            }
        }
        return -1;
    }
}
