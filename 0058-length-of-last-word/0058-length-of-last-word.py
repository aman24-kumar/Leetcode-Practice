class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        x = ""
        for i in range(n-1,-1,-1):
            if s[i] != " ":
                x = x + s[i]
                if s[i-1] == " ":
                    break
        return len(x)


        