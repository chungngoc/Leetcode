class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 0 and num < 4000:
            values = {
                1000: "M",
                900: "CM",
                500: "D",
                400: "CD",
                100: "C",
                90: "XC",
                50: "L",
                40: "XL",
                10: "X",
                9: "IX",
                5: "V",
                4: "IV",
                1: "I",
            }
            for k in list(values.keys()):
                if num >= k:
                    return values[k] + self.intToRoman(num-k)
        
        return ''
            
        