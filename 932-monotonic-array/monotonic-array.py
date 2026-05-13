class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = sorted(nums)
        if nums == l or nums == l[::-1]:
            return True
        return False
        