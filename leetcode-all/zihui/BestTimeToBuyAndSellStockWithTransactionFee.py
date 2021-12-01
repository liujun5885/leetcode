class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        T_ik0 = 0
        T_ik1 = float('-inf')
        for price in prices:
            old_T_ik0 = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price - fee)
            T_ik1 = max(T_ik1, old_T_ik0 - price)
        return T_ik0
