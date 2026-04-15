class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                if nums2[j] not in x:
                    x.append(nums2[j])
        return x 