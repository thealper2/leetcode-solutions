from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        
        nums = []
        for num in s1:
            if num in s2:
                nums.append(num)
        
        if nums:
            return min(nums)
        
        m1 = min(nums1)
        m2 = min(nums2)

        return min(m1 * 10 + m2, m2 * 10 + m1)