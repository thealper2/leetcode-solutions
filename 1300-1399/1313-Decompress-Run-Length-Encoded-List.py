from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums), 2):
            result += nums[i - 1] * [nums[i]]

        return result