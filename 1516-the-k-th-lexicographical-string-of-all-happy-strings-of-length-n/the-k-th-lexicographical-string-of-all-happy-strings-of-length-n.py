class Solution:
    def getListHappyString(self, n: int) -> list:
        if n == 1:
            return ["a", "b", "c"]
        prev_ = self.getListHappyString(n-1)
        result = []
        for k in prev_:
            for x in ["a", "b", "c"]:
                if x != k[-1]:
                    result.append(k+x)
        return result
        
    def getHappyString(self, n: int, k: int) -> str:
        l = self.getListHappyString(n)
        if k > len(l):
            return ""
        return l[k-1]
        