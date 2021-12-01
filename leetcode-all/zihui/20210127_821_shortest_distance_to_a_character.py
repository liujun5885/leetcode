class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # 1. traverse S from left to right, record distance
        # 2. traverse S inversely and update shortest distance
        prev = None
        res = []
        for idx, s in enumerate(S):
            if s == C:
                prev = idx
            if prev is None:
                res.append(float('inf'))
            else:
                res.append(idx - prev)
        
        n = len(S)
        prev = None
        for idx, s in enumerate(S[::-1]):
            if s == C:
                prev = idx
            if prev is not None:
                res[n-idx-1] = min(res[n-idx-1], abs(idx - prev)) 
        return res
