class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_paren = []
        for i in range(len(s)):
            if s[i] == "(":
                open_paren.append(i)
            if s[i] == ")":
                in_paren = s[open_paren[-1] + 1 : i]
                s = s[:open_paren[-1]] + '_' + in_paren[::-1] + '_' + s[i+1:]
                del open_paren[-1]
        s = s.replace('_', '')
        return s
        
               