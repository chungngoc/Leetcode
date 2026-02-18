class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        k = len(s) -1
        while k > 0:
            if d[s[k]] > d[s[k-1]]:
                sum += d[s[k]] - d[s[k-1]]
                k-=2
            else:
                sum += d[s[k]]
                k -=1
        if k == 0:
            sum += d[s[0]]
        return sum
        