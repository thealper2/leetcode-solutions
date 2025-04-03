from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        n1 = sum(1 for num in nums1 if num in s2)
        n2 = sum(1 for num in nums2 if num in s1)
        return [n1, n2]