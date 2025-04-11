from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        for num in stack:
            next_greater[num] = -1
        
        r = []
        for num in nums1:
            r.append(next_greater[num])

        return r