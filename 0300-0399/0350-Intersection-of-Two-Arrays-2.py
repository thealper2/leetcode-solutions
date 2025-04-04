from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        result = []
        
        for num in nums1:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for num in nums2:
            if num in nums1:
                if d[num] > 0:
                    result.append(num)
                    d[num] -= 1
        
        return result