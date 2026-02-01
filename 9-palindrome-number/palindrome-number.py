class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_digits = [i for i in str(x)]
       
        for i in range((len(list_digits) + 1) // 2):
            if list_digits[i] != list_digits[-(1+i)]:
                return False
        return True