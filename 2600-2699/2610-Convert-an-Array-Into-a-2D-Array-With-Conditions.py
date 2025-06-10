from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        max_key = 0
        count = defaultdict(int)
        nums.sort()

        for num in nums:
            count[num] += 1
            if count[num] > max_key:
                max_key = count[num]

        result = [[] for _ in range(max_key)]

        n = len(nums)
        for i in range(n):
            result[i % max_key].append(nums[i])

        return result