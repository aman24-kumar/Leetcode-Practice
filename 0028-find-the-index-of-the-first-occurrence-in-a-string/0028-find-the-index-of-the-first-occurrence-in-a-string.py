class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        n = len(haystack)
        m = len(needle)
        for i in range(0,n):
            if haystack[i:i+m] == needle:
                return i 
                    

        

        