class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        if nums[0] <= nums[-1]:
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True
        else:
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    return False
            return True
        # l = sorted(nums)
        # if nums == l or nums == l[::-1]:
        #     return True
        # return False
        