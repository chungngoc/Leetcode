class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # for (i,j) in [(0,2), (1,3)]:
        #     set1 = set([s1[i], s1[j]])
        #     set2 = set([s2[i], s2[j]])
        #     if len(set1.difference(set2)) > 0:
        #         return False
        # return True

        return (
            sorted(s1[::2]) == sorted(s2[::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )