class Solution:
    def reverseWords(self, s: str) -> str:
        ### Algorithm without using build-in python's function
        res = []
        i = len(s) - 1

        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            # the end of the word
            j = i

            # Move to the start of the word
            while i >= 0 and s[i] != ' ':
                i -= 1

            # Append the word
            res.append(s[i+1:j+1])

        return " ".join(res)


        