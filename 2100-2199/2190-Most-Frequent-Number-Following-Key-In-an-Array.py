from collections import defaultdict
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        max_key = None
        max_val = 0

        for i in range(n):
            if nums[i] == key and i < n - 1:
                count[nums[i + 1]] += 1
                if count[nums[i + 1]] > max_val:
                    max_val = count[nums[i + 1]]
                    max_key = nums[i + 1]

        return max_key