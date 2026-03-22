class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        n = len(strs)
        x = ""
        for i in range(0,len(strs[0])):
            if strs[0][i] == strs[n-1][i]:
                x = x + strs[0][i]
            else:
                    break
        return x
        