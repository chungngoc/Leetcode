import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:      
        # DP solution
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
        
        # Mathematics solution
        # # There are m-1 steps down and n-1 steps right
        # return int(math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1))


    