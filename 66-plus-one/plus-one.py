class Solution:
    #Add to github
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9: 
            if len(digits) > 1:
                return self.plusOne(digits[:-1]) + [0]
            else:
                return [1,0]
        else:
            return digits[:-1] + [digits[-1] + 1]
