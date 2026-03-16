class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return i

        