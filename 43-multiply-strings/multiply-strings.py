class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len1):
            for j in range(len2):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                result[i + j] += digit1 * digit2
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result = result[::-1]
        return ''.join(map(str, result))
          