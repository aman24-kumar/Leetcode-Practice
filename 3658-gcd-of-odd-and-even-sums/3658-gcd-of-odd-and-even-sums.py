class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        x = 0
        y = 0 
        for i in range(0,n):
            x += 1 + 2*i
        for i in range(1,n+1):
            y += 2*i
        return y-x
        