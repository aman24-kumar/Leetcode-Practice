class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        
        for ch in s:
            if ch.isalnum():# used to check weather the character contain only alphabet and number 
                x += ch.lower()
        
        return x == x[::-1]