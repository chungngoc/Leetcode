import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # There are m-1 steps down and n-1 steps right
        len_path = m+n-2

        return int(math.factorial(len_path) / math.factorial(m-1) / math.factorial(n-1))

        