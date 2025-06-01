from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = nums[0]
        
        for num in nums[1:]:
            if abs(num) < abs(closest_num):
                closest_num = num
                
            elif abs(num) == abs(closest_num):
                closest_num = max(num, closest_num)
        
        return closest_num