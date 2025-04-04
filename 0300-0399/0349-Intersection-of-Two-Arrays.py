from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []
        for n1 in nums1:
            if n1 in nums2:
                result.append(n1)
                
        return result