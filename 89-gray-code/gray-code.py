class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        prev = self.grayCode(n-1)
        add = 1 << (n-1)
        
        result = prev + [x + add for x in reversed(prev)]
        return result