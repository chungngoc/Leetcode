class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = [i for i in s]
        T = [i for i in t]
        for i in S:
            if i not in T:
                return False
            j = T.index(i)
            T = T[j+1:]
        return True
        