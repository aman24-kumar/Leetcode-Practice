class Solution(object):
    def twoSum(self, nums, target):
        new = []
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i] +nums[j] == target:
                    new.append(i)
                    new.append(j)
        return new
                    



        