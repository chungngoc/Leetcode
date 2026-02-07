class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 0 and num < 4000:
            R = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"}
            subtractive_form = {4 : "IV", 9 : "IX", 40 : "XL", 90 : "XC", 400 : "CD", 900 : "CM"}
            
            str_num = str(num)
            roman = ''

            if str_num[0] == '4' or str_num[0] == '9':
                for k in list(subtractive_form.keys())[::-1]:
                    if num // k == 1:
                        return subtractive_form[k] + self.intToRoman(num-k)

            for k in list(R.keys())[::-1]:
                if num // k >= 1:
                    print(k, num-k)
                    return R[k] + self.intToRoman(num-k)
        
        return ''
            
        