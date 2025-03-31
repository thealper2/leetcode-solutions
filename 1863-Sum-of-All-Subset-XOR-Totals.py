from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(1, 1 << len(nums)):
            current_xor = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    current_xor ^= nums[j]

            result += current_xor

        return result