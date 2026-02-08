class Solution:
    def isHappy(self, n: int) -> bool:
        list_sum = [n]
        while 1:
            N=0
            for i in str(n):
                N += int(i)**2
            if N==1:
                return True
            if N in list_sum:
                return False
            list_sum.append(N)
            n = N
            
