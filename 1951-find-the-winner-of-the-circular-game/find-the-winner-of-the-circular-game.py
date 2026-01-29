class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = list(range(1,n+1))
        while len(arr) > 1:
            l = k % len(arr)
            if l == 0:
                arr.pop(len(arr)-1)
            else:
                print(type(arr))
                arr = arr[l:] + arr[:l-1]
        return arr[0] 
        