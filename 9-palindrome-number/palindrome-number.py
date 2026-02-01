class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_digits = [i for i in str(x)]
       
        for i in range((len(list_digits) + 1) // 2):
            print(list_digits[i],list_digits[-(1+i)] )
            if list_digits[i] != list_digits[-(1+i)]:
                return False
        return True

        # if x < 0:
        #     return False
        # if x == 0:
        #     return True

        # k = 10**int(math.log10(x))
        # first_d = x // k
        # last_d = x % 10

        # if x == last_d:
        #     return True
        # else:
        #     if first_d != last_d:
        #         return False
        #     else:
        #         new_x = (x % k - last_d) / 10
        #         print(new_x)
        #         return self.isPalindrome(new_x)
        