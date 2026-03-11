class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs, key = len)
        print(strs)

        start = strs[0]

        for i in range(1, len(start)+1):
            for w in strs:
                print(i, start[:i], w[:i])
                if start[:i] != w[:i]:
                   return start[:i-1] if i > 0 else ""
            common_prefix = start[:i]
        return common_prefix
        
