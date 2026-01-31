class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n > 0:
            if n % 2 ==0:
                s = self.myPow(x, n /2)
                return s * s
            else:
                s = self.myPow(x, (n-1)/2)
                return x * s * s
        else:
            return self.myPow(1/x, -n)