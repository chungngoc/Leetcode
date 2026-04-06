class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split(" ")
        for i in k[::-1]:
            if len(i) > 0:
                return len(i)
        