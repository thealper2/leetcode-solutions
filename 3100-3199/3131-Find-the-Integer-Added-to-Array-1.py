from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return int((sum(nums2) - sum(nums1)) / len(nums2))