class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # There are 2 options to choose i and j
        # i = 0 and j = 2 OR i = 1 and j = 3
        for (i,j) in [(0,2), (1,3)]:
            set1 = set([s1[i], s1[j]])
            set2 = set([s2[i], s2[j]])
            if len(set1.difference(set2)) > 0:
                return False
        return True