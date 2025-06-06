from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        result = []
        n = len(nums)

        for num in nums:
            for x in num:
                count[x] += 1
                if count[x] >= n:
                    result.append(x)

        return sorted(result)