class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        x = set(nums1)
        for i in x:
            c1 = nums1.count(i)
            c2 = nums2.count(i)
            m = min(c1, c2)
            res.extend([i]*m)
        return res