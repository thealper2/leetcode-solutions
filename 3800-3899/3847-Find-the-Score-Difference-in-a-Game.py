from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        swap = False
        p1 = p2 = 0
        n = len(nums)
        for i in range(n):
            point = nums[i]
            if (point % 2 == 1):
                swap = not swap
            
            if (i > 0 and (i + 1) % 6 == 0):
                    swap = not swap
            
            if swap:
                p2 += point
            else:
                p1 += point

        return p1 - p2
