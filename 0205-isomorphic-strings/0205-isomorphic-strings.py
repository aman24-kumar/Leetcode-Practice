class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        set_a = {}
        set_b = {}
        for i in range(0,len(s)):
            s1 = s[i]
            t1 = t[i]
            if s1 not in set_a:
                set_a[s1] =i
            if t1 not in set_b:
                set_b[t1] =i
            if set_a[s1] != set_b[t1]:
                return False
        return True
