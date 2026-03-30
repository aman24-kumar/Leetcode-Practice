class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        
        for ch in s:
            if ch.isalnum():
                x += ch.lower()
        
        return x == x[::-1]