from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for num in nums:
            position += num
            if position == 0:
                count += 1
                
        return count