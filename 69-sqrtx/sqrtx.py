class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 1:
            for i in range(1,x):
                if (i * i <= x) and (i+1)*(i+1) > x:
                    return i
        return x
        