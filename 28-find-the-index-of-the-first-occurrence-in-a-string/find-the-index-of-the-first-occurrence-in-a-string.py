class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        k = len(needle)
        for i in range(0, len(haystack)):
            if needle == haystack[i: i+k]:
                return i 
        