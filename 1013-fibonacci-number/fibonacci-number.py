class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = [0,1]
        for i in range(2, n+1):
            r.append(r[i-1]+r[i-2])
        return r[n]
        