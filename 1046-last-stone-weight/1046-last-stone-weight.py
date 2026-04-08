class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x = len(stones)
        while len(stones) >1 :
            stones = sorted(stones)
            z = stones[-1] -stones[-2]
            stones.pop()
            stones.pop()
            if z != 0:
                stones.append(z)
        if not stones:
            return 0
        else:
            return stones.pop()
        
        