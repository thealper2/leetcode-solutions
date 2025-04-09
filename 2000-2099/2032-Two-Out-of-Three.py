from typing import List
     
        
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        
        result = (set1 & set2) | (set1 & set3) | (set2 & set3)
        
        return list(result)