class Solution(object):
    def is_valid(self,x):
        if (x >= -pow(2,31)) and (x <= pow(2,31) -1):
            return True
        else:
            return False

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = True
        str_x = str(x)
        reverse_str_x = str_x[::-1]

        if reverse_str_x[-1] == '-':
            positive = False
            reverse_str_x = reverse_str_x[: len(reverse_str_x) -1]
        reverse_x = int(reverse_str_x) if positive else 0-int(reverse_str_x)
        reverse_x = reverse_x if self.is_valid(reverse_x) else 0

        return reverse_x
        