from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        min_distance = float('inf')

        for i in range(n):
            if nums[i] == target:
                min_distance = min(min_distance, abs(i - start))

        return min_distance