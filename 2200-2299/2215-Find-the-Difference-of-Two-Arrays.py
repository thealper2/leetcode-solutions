from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]

        for num in nums1:
            if num not in nums2:
                result[0].append(num)
        
        for num in nums2:
            if num not in nums1:
                result[1].append(num)

        result[0] = list(set(result[0]))
        result[1] = list(set(result[1]))

        return result