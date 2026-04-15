class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0 
        x = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != x[i]:
                count += 1
        return count 
        