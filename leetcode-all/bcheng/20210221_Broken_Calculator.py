class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ops=0
        while Y>X:
            ops+=1
            if Y%2==0:
                Y//=2
            else:
                Y+=1
        return ops+X-Y

