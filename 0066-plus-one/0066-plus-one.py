class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ""
        n = len(digits)
        for i in range(0,n):
            x = x + str(digits[i])
        z = int(x)
        a = z+1
        b = str(a)
        c = []
        for i in range(0,len(b)):
            c.append(int(b[i]))
        return c 
